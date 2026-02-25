#!/usr/bin/env python3
import paramiko
transport = paramiko.Transport(("access831383027.webspace-data.io", 22))
transport.connect(username="u101215843-1", password="OpenClawAssistant@SFTP")
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put("./src/index.html", "/demo-suwebsite/index.html")
print("Uploaded index.html")
sftp.close()
transport.close()
