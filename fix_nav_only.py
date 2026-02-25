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

# Einheitliche Navigation (HTML only)
def get_nav(active_page):
    items = [
        ('/team/', 'Team'),
        ('/vorstand/', 'Vorstand'),
        ('/pfingstturnier/', 'Pfingstturnier'),
        ('/events/', 'Events'),
        ('/fanshop/', 'Fanshop')
    ]
    
    nav_html = '      <ul class="nav-menu" id="navMenu">\n'
    for href, label in items:
        active_class = ' active' if href == f'/{active_page}/' else ''
        nav_html += f'        <li><a href="{href}" class="nav-link{active_class}">{label}</a></li>\n'
    nav_html += '      </ul>'
    
    return nav_html

pages = ['team', 'erfolge', 'geschichte', 'spielstaette', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social', 'vorstand']

for page in pages:
    try:
        remote_path = f"/demo-suwebsite/{page}/index.html"
        local_path = f"./src/{page}.html"
        
        sftp.get(remote_path, local_path)
        
        with open(local_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Only replace the nav-menu ul, nothing else
        old_pattern = r'<ul class="nav-menu" id="navMenu">.*?</ul>'
        new_nav = get_nav(page)
        
        content = re.sub(old_pattern, new_nav, content, flags=re.DOTALL)
        
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        sftp.put(local_path, remote_path)
        print(f"✓ {page}")
        
    except Exception as e:
        print(f"✗ {page}: {e}")

sftp.close()
transport.close()
print("\n✅ Navigation unified on all pages!")
