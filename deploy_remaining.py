import paramiko
t = paramiko.Transport(("access831383027.webspace-data.io", 22))
t.connect(username="u101215843-1", password="OpenClawAssistant@SFTP")
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put("./src/events.html", "/demo-suwebsite/events/index.html")
sftp.put("./src/pfingstturnier.html", "/demo-suwebsite/pfingstturnier/index.html")
print("Done!")
sftp.close()
t.close()
