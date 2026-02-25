#!/usr/bin/env python3
import paramiko
import re

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Standard Navigation für alle Seiten
def get_nav_for_page(page_name):
    pages = {
        'team': ('Team', True),
        'vorstand': ('Vorstand', True),
        'pfingstturnier': ('Pfingstturnier', True),
        'events': ('Events', True),
        'fanshop': ('Fanshop', True)
    }
    
    nav_items = []
    for page, (label, active_check) in pages.items():
        is_active = 'active' if page == page_name else ''
        nav_items.append(f'<li><a href="/{page}/" class="nav-link {is_active}">{label}</a></li>')
    
    return '''      <!-- Navigation Links -->
      <ul class="nav-menu" id="navMenu">
        ''' + '\n        '.join(nav_items) + '''
      </ul>'''

pages = ['index', 'team', 'erfolge', 'geschichte', 'spielstaette', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social', 'vorstand']

for page in pages:
    try:
        # Determine filename
        if page == 'index':
            remote_path = "/demo-suwebsite/index.html"
            local_path = "./src/index.html"
        else:
            remote_path = f"/demo-suwebsite/{page}/index.html"
            local_path = f"./src/{page}.html"
        
        # Download
        sftp.get(remote_path, local_path)
        
        with open(local_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace navigation with standard one
        old_nav_pattern = r'<!-- Navigation Links -->.*?<ul class="nav-menu" id="navMenu">.*?</ul>'
        
        # Determine active page
        if page == 'index':
            active_page = None
        else:
            active_page = page
        
        new_nav = get_nav_for_page(active_page)
        content = re.sub(old_nav_pattern, new_nav, content, flags=re.DOTALL)
        
        # Write and upload
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        sftp.put(local_path, remote_path)
        print(f"✓ Updated: {page}")
        
    except Exception as e:
        print(f"✗ Error with {page}: {e}")

sftp.close()
transport.close()
print("\n✅ All pages have unified navigation!")
