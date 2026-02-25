#!/usr/bin/env python3
import paramiko

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Create fanshop directory
try:
    sftp.mkdir("/demo-suwebsite/fanshop")
except:
    pass

sftp.put("./src/fanshop.html", "/demo-suwebsite/fanshop/index.html")
print("Uploaded: fanshop/index.html")

sftp.close()
transport.close()
print("Done!")
