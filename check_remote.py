#!/usr/bin/env python3
import paramiko

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

print("Listing root directory:")
try:
    for item in sftp.listdir('/'):
        print(f"  {item}")
except Exception as e:
    print(f"Error: {e}")

print("\nListing /html if exists:")
try:
    for item in sftp.listdir('/html'):
        print(f"  {item}")
except Exception as e:
    print(f"  /html does not exist or error: {e}")

print("\nListing /www if exists:")
try:
    for item in sftp.listdir('/www'):
        print(f"  {item}")
except Exception as e:
    print(f"  /www does not exist or error: {e}")

sftp.close()
transport.close()
