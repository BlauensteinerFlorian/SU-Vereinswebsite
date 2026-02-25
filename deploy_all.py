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

def ensure_dir(path):
    dirs = path.strip('/').split('/')
    current = ""
    for d in dirs:
        if not d:
            continue
        current += "/" + d
        try:
            sftp.mkdir(current)
            print(f"Created dir: {current}")
        except:
            pass

# Upload all files
local_dir = Path("./dist")
for file_path in local_dir.rglob('*'):
    if file_path.is_file():
        relative_path = file_path.relative_to(local_dir)
        remote_file = f"/{relative_path}".replace('//', '/')
        remote_folder = str(Path(remote_file).parent)
        
        ensure_dir(remote_folder)
        
        sftp.put(str(file_path), remote_file)
        print(f"Uploaded: {remote_file}")

sftp.close()
transport.close()
print("Deployment complete!")
