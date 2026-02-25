#!/usr/bin/env python3
import os
import sys
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

# Ensure directory exists
def ensure_dir(path):
    dirs = path.strip('/').split('/')
    current = ""
    for d in dirs:
        current += "/" + d
        try:
            sftp.mkdir(current)
            print(f"Created dir: {current}")
        except:
            pass

# Upload instagram images
local_dir = Path("./dist/assets/instagram")
ensure_dir("/assets/instagram")

for f in local_dir.glob("*"):
    remote = f"/assets/instagram/{f.name}"
    sftp.put(str(f), remote)
    print(f"Uploaded: {remote}")

sftp.close()
transport.close()
print("Done!")
