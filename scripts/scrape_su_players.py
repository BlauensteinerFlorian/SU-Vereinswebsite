#!/usr/bin/env python3
"""
Web Scraper for Hobbyliga Zwettl - SU Rudmanns Player Data
Extracts player data from images and table structure
"""

import argparse
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_page(url):
    """Fetch page with headers to avoid blocking"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # Try HTTP first (site has no SSL)
    urls = [url]
    if url.startswith('https://'):
        urls.insert(0, url.replace('https://', 'http://', 1))
    
    for url_attempt in urls:
        try:
            print(f"Fetching {url_attempt}...")
            response = requests.get(url_attempt, headers=headers, timeout=30, verify=False)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error with {url_attempt}: {e}")
            continue
    return None

def parse_players(html, base_url):
    """Parse player data from HTML - images have format: NUMBER_NAME"""
    soup = BeautifulSoup(html, 'html.parser')
    players = []
    
    # Find all images with player data
    images = soup.find_all('img')
    print(f"Found {len(images)} images")
    
    for img in images:
        src = img.get('src', '')
        alt = img.get('alt', '')
        
        # Skip non-player images (logos, banners, etc.)
        if not alt or any(skip in src.lower() for skip in ['logo', 'banner', 'icon', 'header']):
            continue
        
        # Pattern: NUMBER_NAME (e.g., "1_DANGL", "7_GRETZ")
        # Extract number and name from alt text or filename
        match = re.match(r'(\d+)_(.+)', alt)
        if match:
            number = match.group(1)
            name = match.group(2).replace('_', ' ').title()
            
            player = {
                'number': number,
                'name': name,
                'image_url': urljoin(base_url, src),
                'birthdate': '',
                'position': ''
            }
            players.append(player)
            print(f"Found player: #{number} {name}")
    
    # Also try to find additional data from table if present
    table = soup.find('table')
    if table and players:
        rows = table.find_all('tr')
        print(f"\nFound table with {len(rows)} rows - matching with player data...")
        
        # Match table rows with players by name or number
        for i, player in enumerate(players):
            if i < len(rows):
                row = rows[i]
                cells = row.find_all(['td', 'th'])
                
                # Look for birthdate pattern in row text
                row_text = row.get_text()
                date_match = re.search(r'(\d{1,2})[\.\/](\d{1,2})[\.\/](\d{2,4})', row_text)
                if date_match:
                    player['birthdate'] = date_match.group(0)
                
                # Look for position
                positions = ['TW', 'Tor', 'LV', 'RV', 'IV', 'ZM', 'ZDM', 'LM', 'RM', 'ST', 'HS']
                for pos in positions:
                    if pos in row_text.upper():
                        player['position'] = pos
                        break
    
    return players

def save_csv(players, output_file):
    """Save to CSV"""
    if not players:
        print("No player data to save")
        return False
    
    fieldnames = ['number', 'name', 'image_url', 'birthdate', 'position']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(players)
    
    print(f"\n✅ Saved {len(players)} players to {output_file}")
    return True

def download_images(players, output_dir):
    """Download player images"""
    if not players:
        return
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    downloaded = 0
    for player in players:
        if player['image_url']:
            try:
                response = requests.get(player['image_url'], headers=headers, timeout=10, verify=False)
                if response.status_code == 200:
                    safe_name = f"{player['number']}_{player['name'].replace(' ', '_')}.jpg"
                    filepath = os.path.join(output_dir, safe_name)
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                    downloaded += 1
                    print(f"Downloaded: {safe_name}")
            except Exception as e:
                print(f"Failed to download image for {player['name']}: {e}")
    
    print(f"\n✅ Downloaded {downloaded}/{len(players)} images to {output_dir}")

def main():
    parser = argparse.ArgumentParser(description='Scrape SU Rudmanns player data')
    parser.add_argument('--url', default='http://www.hobbyliga-zwettl.at/kader-su-rudmannsstift-zwettl', help='URL to scrape')
    parser.add_argument('--output', default='players.csv', help='Output CSV file')
    parser.add_argument('--download-images', action='store_true', help='Also download player images')
    parser.add_argument('--image-dir', default='player_images', help='Directory for downloaded images')
    args = parser.parse_args()
    
    html = fetch_page(args.url)
    if not html:
        print("Failed to fetch page")
        return
    
    print("\nParsing player data...")
    players = parse_players(html, args.url)
    
    if players:
        save_csv(players, args.output)
        
        if args.download_images:
            download_images(players, args.image_dir)
    else:
        print("No players found")

if __name__ == '__main__':
    import os
    main()
