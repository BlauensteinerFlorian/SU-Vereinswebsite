#!/usr/bin/env python3
"""
Web Scraper for Hobbyliga Zwettl - SU Rudmanns Player Data
Table structure: 3 columns x N rows (3 players per row group)
"""

import argparse
import csv
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_page(url):
    """Fetch page"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
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
            print(f"Error: {e}")
            continue
    return None

def parse_players(html, base_url):
    """Parse players from 3-column table (3 players per 4-row group)"""
    soup = BeautifulSoup(html, 'html.parser')
    players = []
    
    table = soup.find('table')
    if not table:
        print("No table found")
        return []
    
    rows = table.find_all('tr')
    print(f"Found {len(rows)} rows, processing in groups of 4...")
    
    # Process in groups of 4 rows: [Images, Names, Birthdates, Empty]
    for i in range(0, len(rows), 4):
        if i + 2 >= len(rows):
            break
        
        img_row = rows[i]
        name_row = rows[i+1] if (i+1) < len(rows) else None
        birth_row = rows[i+2] if (i+2) < len(rows) else None
        
        # Get all cells from image row (should be 3)
        img_cells = img_row.find_all(['td', 'th'])
        name_cells = name_row.find_all(['td', 'th']) if name_row else []
        birth_cells = birth_row.find_all(['td', 'th']) if birth_row else []
        
        # Process each column (max 3 players per group)
        for col in range(3):
            player = {
                'number': '',
                'name': '',
                'image_url': '',
                'birthdate': ''
            }
            
            # Get image from column
            if col < len(img_cells):
                img = img_cells[col].find('img')
                if img:
                    src = img.get('src', '')
                    alt = img.get('alt', '')
                    player['image_url'] = urljoin(base_url, src)
                    
                    # Extract number from alt text (e.g., "1_DANGL")
                    match = re.match(r'(\d+)_(.+)', alt)
                    if match:
                        player['number'] = match.group(1)
            
            # Get name from column
            if col < len(name_cells):
                player['name'] = name_cells[col].get_text(strip=True)
            
            # Get birthdate from column
            if col < len(birth_cells):
                player['birthdate'] = birth_cells[col].get_text(strip=True)
            
            # Only add if we have a name
            if player['name']:
                players.append(player)
                print(f"  #{player['number']} {player['name']} - {player['birthdate']}")
    
    return players

def save_csv(players, output_file):
    """Save to CSV"""
    if not players:
        print("No player data to save")
        return False
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['number', 'name', 'image_url', 'birthdate'], delimiter=';')
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
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    downloaded = 0
    
    for player in players:
        if player['image_url'] and player['name']:
            try:
                response = requests.get(player['image_url'], headers=headers, timeout=10, verify=False)
                if response.status_code == 200:
                    # Create safe filename
                    safe_name = re.sub(r'[^\w\s-]', '', player['name']).strip().replace(' ', '_')
                    if player['number']:
                        safe_name = f"{player['number']}_{safe_name}"
                    safe_name += ".jpg"
                    
                    filepath = os.path.join(output_dir, safe_name)
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                    downloaded += 1
                    print(f"  Downloaded: {safe_name}")
            except Exception as e:
                print(f"  Failed for {player['name']}: {e}")
    
    print(f"\n✅ Downloaded {downloaded}/{len(players)} images")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default='http://www.hobbyliga-zwettl.at/kader-su-rudmannsstift-zwettl')
    parser.add_argument('--output', default='players.csv')
    parser.add_argument('--download-images', action='store_true')
    parser.add_argument('--image-dir', default='player_images')
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
    main()
