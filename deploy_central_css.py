#!/usr/bin/env python3
import paramiko

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Create css directory
try:
    sftp.mkdir("/demo-suwebsite/css")
except:
    pass

# Upload central CSS
sftp.put("./src/css/style.css", "/demo-suwebsite/css/style.css")
print("Uploaded central CSS: /demo-suwebsite/css/style.css")

sftp.close()
transport.close()
print("Done!")
