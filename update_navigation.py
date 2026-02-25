#!/usr/bin/env python3
import re
from pathlib import Path

# Neue Navigation
new_nav = '''      <!-- Navigation Links -->
      <ul class="nav-menu" id="navMenu">
        <li><a href="/team/" class="nav-link{% if page.url == '/team/' %} active{% endif %}">Team</a></li>
        <li><a href="/pfingstturnier/" class="nav-link{% if page.url == '/pfingstturnier/' %} active{% endif %}">Pfingstturnier</a></li>
        <li><a href="/events/" class="nav-link{% if page.url == '/events/' %} active{% endif %}">Events</a></li>
        <li><a href="/fanshop/" class="nav-link{% if page.url == '/fanshop/' %} active{% endif %}">Fanshop</a></li>
      </ul>'''

# Einfache Navigation ohne Template-Syntax für statische HTML
new_nav_simple = '''      <!-- Navigation Links -->
      <ul class="nav-menu" id="navMenu">
        <li><a href="/team/" class="nav-link">Team</a></li>
        <li><a href="/pfingstturnier/" class="nav-link">Pfingstturnier</a></li>
        <li><a href="/events/" class="nav-link">Events</a></li>
        <li><a href="/fanshop/" class="nav-link">Fanshop</a></li>
      </ul>'''

pages = ['team', 'erfolge', 'geschichte', 'spielstaette', 'vorstand', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social']

for page in pages:
    filepath = Path(f"./src/{page}.html")
    if filepath.exists():
        content = filepath.read_text()
        
        # Finde und ersetze den Navigationsbereich
        pattern = r'<!-- Navigation Links -->.*?<ul class="nav-menu" id="navMenu">.*?</ul>'
        content = re.sub(pattern, new_nav_simple.strip(), content, flags=re.DOTALL)
        
        filepath.write_text(content)
        print(f"Updated: {page}.html")

print("\nAll pages updated!")
