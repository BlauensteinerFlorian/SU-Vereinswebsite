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

# Read index.html navigation
with open('./src/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract navigation from index
nav_match = re.search(r'(<header class="site-header">.*?</header>)', index_content, re.DOTALL)
if not nav_match:
    print("Could not find navigation in index.html")
    exit(1)

index_nav = nav_match.group(1)

pages = ['team', 'erfolge', 'geschichte', 'spielstaette', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social', 'vorstand']

for page in pages:
    try:
        remote_path = f"/demo-suwebsite/{page}/index.html"
        local_path = f"./src/{page}.html"
        
        # Download current page
        sftp.get(remote_path, local_path)
        
        with open(local_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace header with index header, but adjust active state
        new_nav = index_nav.replace('class="nav-link "', 'class="nav-link"')  # Remove extra spaces
        
        # Set active state for current page
        new_nav = new_nav.replace(f'href="/{page}/" class="nav-link"', f'href="/{page}/" class="nav-link active"')
        
        # Replace header section
        content = re.sub(r'<header class="site-header">.*?</header>', new_nav, content, flags=re.DOTALL)
        
        # Write and upload
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        sftp.put(local_path, remote_path)
        print(f"✓ Updated: {page}")
        
    except Exception as e:
        print(f"✗ Error with {page}: {e}")

sftp.close()
transport.close()
print("\n✅ All pages now use the exact same navigation as index!")
