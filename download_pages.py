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

pages = ['team', 'erfolge', 'geschichte', 'spielstaette', 'vorstand', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social']

for page in pages:
    try:
        remote_path = f"/demo-suwebsite/{page}/index.html"
        local_path = f"./src/{page}.html"
        sftp.get(remote_path, local_path)
        print(f"Downloaded: {page}/index.html")
    except Exception as e:
        print(f"Error downloading {page}: {e}")

sftp.close()
transport.close()
print("Done!")
