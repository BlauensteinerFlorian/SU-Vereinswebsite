#!/usr/bin/env python3
import paramiko

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Wenn Server-Versionen gut sind, lade sie herunter
pages = ['team', 'erfolge', 'geschichte', 'spielstaette', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social', 'vorstand']

for page in pages:
    try:
        remote_path = f"/demo-suwebsite/{page}/index.html"
        local_path = f"./src/{page}.html"
        
        # Lade vom Server herunter (vorheriger Zustand)
        sftp.get(remote_path, local_path)
        print(f"✓ Restored: {page}")
    except Exception as e:
        print(f"✗ Error: {page}: {e}")

sftp.close()
transport.close()
