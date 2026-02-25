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

# Check what directories exist in demo-suwebsite
demo_path = "/demo-suwebsite"
print(f"\nListing {demo_path}:")
try:
    for item in sftp.listdir(demo_path):
        try:
            stat = sftp.stat(f"{demo_path}/{item}")
            is_dir = (stat.st_mode & 0o40000) == 0o40000
            print(f"  {item}/" if is_dir else f"  {item}")
        except:
            print(f"  {item} (error)")
except Exception as e:
    print(f"Error: {e}")

sftp.close()
transport.close()
