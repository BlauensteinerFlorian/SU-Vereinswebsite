#!/usr/bin/env python3
import re
from pathlib import Path

# Standard max-width für Hauptcontainer
STANDARD_WIDTH = "1200px"

pages = ['erfolge', 'events', 'galerie', 'geschichte', 'pfingstturnier', 'social', 'spielplan', 'spielstaette', 'vorstand']

for page in pages:
    filepath = Path(f"./src/{page}.html")
    if filepath.exists():
        content = filepath.read_text(encoding='utf-8')
        
        # Ersetze verschiedene max-width Werte für Hauptcontainer
        # container, content, main-content etc.
        patterns = [
            (r'(max-width:\s*)\d+px(\s*;\s*margin:\s*0\s+auto)', f'\\g<1>{STANDARD_WIDTH}\\g<2>'),
            (r'\.container\s*\{[^}]*max-width:\s*\d+px', f'.container {{ max-width: {STANDARD_WIDTH}'),
            (r'max-width:\s*800px\s*;\s*margin:\s*0\s+auto', f'max-width: {STANDARD_WIDTH}; margin: 0 auto'),
            (r'max-width:\s*900px\s*;\s*margin:\s*0\s+auto', f'max-width: {STANDARD_WIDTH}; margin: 0 auto'),
            (r'max-width:\s*1000px\s*;\s*margin:\s*0\s+auto', f'max-width: {STANDARD_WIDTH}; margin: 0 auto'),
            (r'max-width:\s*1024px\s*;\s*margin:\s*0\s+auto', f'max-width: {STANDARD_WIDTH}; margin: 0 auto'),
        ]
        
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)
        
        filepath.write_text(content, encoding='utf-8')
        print(f"Updated: {page}.html")

print(f"\nAll pages normalized to {STANDARD_WIDTH} max-width!")
