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

pages = ['index', 'team', 'erfolge', 'geschichte', 'spielstaette', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social', 'vorstand']

new_nav = '''      <!-- Navigation Links -->
      <ul class="nav-menu" id="navMenu">
        <li><a href="/team/" class="nav-link">Team</a></li>
        <li><a href="/vorstand/" class="nav-link">Vorstand</a></li>
        <li><a href="/pfingstturnier/" class="nav-link">Pfingstturnier</a></li>
        <li><a href="/events/" class="nav-link">Events</a></li>
        <li><a href="/fanshop/" class="nav-link">Fanshop</a></li>
      </ul>'''

for page in pages:
    try:
        # Download current page
        remote_path = f"/demo-suwebsite/{page}/index.html" if page != 'index' else "/demo-suwebsite/index.html"
        sftp.get(remote_path, f"./temp_{page}.html")
        
        # Update navigation
        with open(f"./temp_{page}.html", 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace navigation section
        pattern = r'<!-- Navigation Links -->.*?<ul class="nav-menu" id="navMenu">.*?</ul>'
        content = re.sub(pattern, new_nav.strip(), content, flags=re.DOTALL)
        
        # Update active state for current page
        if page == 'vorstand':
            content = content.replace('href="/vorstand/" class="nav-link"', 'href="/vorstand/" class="nav-link active"')
        elif page == 'team':
            content = content.replace('href="/team/" class="nav-link"', 'href="/team/" class="nav-link active"')
        elif page == 'pfingstturnier':
            content = content.replace('href="/pfingstturnier/" class="nav-link"', 'href="/pfingstturnier/" class="nav-link active"')
        elif page == 'events':
            content = content.replace('href="/events/" class="nav-link"', 'href="/events/" class="nav-link active"')
        elif page == 'fanshop':
            content = content.replace('href="/fanshop/" class="nav-link"', 'href="/fanshop/" class="nav-link active"')
        else:
            # For other pages, remove any active class
            content = content.replace('class="nav-link active"', 'class="nav-link"')
        
        # Write and upload back
        with open(f"./temp_{page}.html", 'w', encoding='utf-8') as f:
            f.write(content)
        
        sftp.put(f"./temp_{page}.html", remote_path)
        print(f"Updated: {page}")
        
        # Clean up
        import os
        os.remove(f"./temp_{page}.html")
    except Exception as e:
        print(f"Error with {page}: {e}")

sftp.close()
transport.close()
print("\nAll pages updated with new navigation!")
