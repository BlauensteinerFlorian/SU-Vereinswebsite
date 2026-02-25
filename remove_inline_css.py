#!/usr/bin/env python3
import re
from pathlib import Path

pages = ['index', 'team', 'erfolge', 'geschichte', 'spielstaette', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social', 'vorstand']

for page in pages:
    if page == 'index':
        filepath = Path('./src/index.html')
    else:
        filepath = Path(f'./src/{page}.html')
    
    if filepath.exists():
        content = filepath.read_text(encoding='utf-8')
        
        # Remove ALL inline style tags
        content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
        
        # Make sure the link to central CSS exists
        if '/css/style.css' not in content:
            content = content.replace('</head>', '  <link rel="stylesheet" href="/css/style.css">\n</head>')
        
        filepath.write_text(content, encoding='utf-8')
        print(f"✓ Updated: {page}")

print("\n✅ All pages now use central CSS!")
