#!/usr/bin/env python3
import paramiko

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Check for backup files or alternate locations
base_path = "/demo-suwebsite"

try:
    print("Listing team directory:")
    for item in sftp.listdir(f"{base_path}/team"):
        print(f"  {item}")
except Exception as e:
    print(f"Error: {e}")

# Check if there are backup files
import re
for page in ['team', 'erfolge', 'geschichte']:
    try:
        dir_path = f"{base_path}/{page}"
        items = sftp.listdir(dir_path)
        backup_files = [f for f in items if '.bak' in f or '.old' in f or '.orig' in f]
        if backup_files:
            print(f"\n{page} backups: {backup_files}")
    except:
        pass

sftp.close()
transport.close()
