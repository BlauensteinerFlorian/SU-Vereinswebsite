#!/usr/bin/env python3
import paramiko

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Nur Events und Pfingstturnier deployen
sftp.put("./src/events.html", "/demo-suwebsite/events/index.html")
print("Uploaded: events/index.html")

sftp.put("./src/pfingstturnier.html", "/demo-suwebsite/pfingstturnier/index.html")
print("Uploaded: pfingstturnier/index.html")

sftp.close()
transport.close()
print("Done!")
