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

# Delete Galerie and Ansprechpartner directories
for dir in ['galerie', 'ansprechpartner']:
    try:
        sftp.rmdir(f"/demo-suwebsite/{dir}")
        print(f"Deleted: {dir}")
    except Exception as e:
        print(f"Error deleting {dir}: {e}")

sftp.close()
transport.close()
print("\n✅ Pages deleted!")
