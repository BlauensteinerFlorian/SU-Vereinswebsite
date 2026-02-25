#!/usr/bin/env python3
import paramiko

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Download current team page
sftp.get("/demo-suwebsite/team/index.html", "./team_current.html")

# Check content
content = open("./team_current.html").read()

# Find the main content area
import re
match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL)
if match:
    main_content = match.group(1)
    print("Main content found:")
    print(main_content[:1000])
else:
    print("No main tag found, showing body content:")
    match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
    if match:
        print(match.group(1)[:1000])

sftp.close()
transport.close()
