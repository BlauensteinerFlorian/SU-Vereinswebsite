#!/usr/bin/env python3
import paramiko
from pathlib import Path
import re

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Neue Navigation (verkleinert)
new_nav = '''      <!-- Navigation Links -->
      <ul class="nav-menu" id="navMenu">
        <li><a href="/team/" class="nav-link">Team</a></li>
        <li><a href="/pfingstturnier/" class="nav-link">Pfingstturnier</a></li>
        <li><a href="/events/" class="nav-link">Events</a></li>
        <li><a href="/fanshop/" class="nav-link">Fanshop</a></li>
      </ul>'''

pages = ['team', 'erfolge', 'geschichte', 'spielstaette', 'vorstand', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social']

for page in pages:
    try:
        # Download original from server
        remote_path = f"/demo-suwebsite/{page}/index.html"
        local_path = f"./src/{page}.html"
        sftp.get(remote_path, local_path)
        
        # Read and update navigation only
        content = Path(local_path).read_text()
        
        # Replace navigation section
        pattern = r'<!-- Navigation Links -->.*?<ul class="nav-menu" id="navMenu">.*?</ul>'
        content = re.sub(pattern, new_nav.strip(), content, flags=re.DOTALL)
        
        # Save updated file
        Path(local_path).write_text(content)
        
        # Upload back
        sftp.put(local_path, remote_path)
        print(f"Restored and updated: {page}")
    except Exception as e:
        print(f"Error with {page}: {e}")

sftp.close()
transport.close()
print("\nAll pages restored with new navigation!")
