#!/usr/bin/env python3
import paramiko
transport = paramiko.Transport(("access831383027.webspace-data.io", 22))
transport.connect(username="u101215843-1", password="OpenClawAssistant@SFTP")
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put("./src/css/style.css", "/demo-suwebsite/css/style.css")
print("Uploaded CSS")
sftp.close()
transport.close()
