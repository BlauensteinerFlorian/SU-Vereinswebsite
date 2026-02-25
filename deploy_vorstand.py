#!/usr/bin/env python3
import paramiko

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Upload vorstand page
sftp.put("./src/vorstand.html", "/demo-suwebsite/vorstand/index.html")
print("Uploaded: vorstand/index.html")

sftp.close()
transport.close()
print("Done!")
