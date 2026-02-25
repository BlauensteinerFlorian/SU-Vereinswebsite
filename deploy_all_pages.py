#!/usr/bin/env python3
import paramiko
from pathlib import Path

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

pages = {
    'index': '/demo-suwebsite/index.html',
    'team': '/demo-suwebsite/team/index.html',
    'erfolge': '/demo-suwebsite/erfolge/index.html',
    'geschichte': '/demo-suwebsite/geschichte/index.html',
    'spielstaette': '/demo-suwebsite/spielstaette/index.html',
    'spielplan': '/demo-suwebsite/spielplan/index.html',
    'events': '/demo-suwebsite/events/index.html',
    'galerie': '/demo-suwebsite/galerie/index.html',
    'pfingstturnier': '/demo-suwebsite/pfingstturnier/index.html',
    'social': '/demo-suwebsite/social/index.html',
    'vorstand': '/demo-suwebsite/vorstand/index.html'
}

for page, remote_path in pages.items():
    local_path = f'./src/{page}.html' if page != 'index' else './src/index.html'
    sftp.put(local_path, remote_path)
    print(f"Uploaded: {remote_path}")

sftp.close()
transport.close()
print("\n✅ All pages deployed!")
