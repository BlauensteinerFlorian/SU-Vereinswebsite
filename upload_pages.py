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

print(f"Connected to {host}")

pages = ['team', 'erfolge', 'geschichte', 'spielstaette', 'vorstand', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social']

for page in pages:
    local_path = f"./src/{page}.html"
    remote_path = f"/demo-suwebsite/{page}/index.html"
    try:
        sftp.put(local_path, remote_path)
        print(f"Uploaded: {page}/index.html")
    except Exception as e:
        print(f"Error uploading {page}: {e}")

sftp.close()
transport.close()
print("\nAll pages uploaded!")
