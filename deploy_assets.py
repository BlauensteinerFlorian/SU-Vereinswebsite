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

# Create directories
for dir in ['/demo-suwebsite/css', '/demo-suwebsite/assets/hero', '/demo-suwebsite/assets/sponsors']:
    try:
        sftp.mkdir(dir)
    except:
        pass

# Upload CSS
sftp.put("./src/css/style.css", "/demo-suwebsite/css/style.css")
print("Uploaded: css/style.css")

# Upload hero images
for img in Path("./src/assets/hero").glob("*"):
    sftp.put(str(img), f"/demo-suwebsite/assets/hero/{img.name}")
    print(f"Uploaded: assets/hero/{img.name}")

# Upload sponsor images
for img in Path("./src/assets/sponsors").glob("*"):
    sftp.put(str(img), f"/demo-suwebsite/assets/sponsors/{img.name}")
    print(f"Uploaded: assets/sponsors/{img.name}")

sftp.close()
transport.close()
print("\n✅ All assets deployed!")
