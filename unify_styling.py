#!/usr/bin/env python3
import paramiko
import re

# Standard CSS das alle Seiten verwenden sollen
STANDARD_CSS = '''  <style>
    :root {
      --color-primary: #FF6600;
      --color-accent: #FFFFFF;
      --bg-primary: #0a0a0a;
      --bg-secondary: #141414;
      --bg-card: #1a1a1a;
      --text-primary: #FFFFFF;
      --text-secondary: #888888;
      --text-muted: #666666;
      --font-size-xs: 0.75rem;
      --font-size-sm: 0.875rem;
      --font-size-base: 1rem;
      --font-size-lg: 1.125rem;
      --font-size-xl: 1.25rem;
      --font-size-2xl: 1.5rem;
      --font-size-3xl: 2rem;
      --space-1: 0.25rem;
      --space-2: 0.5rem;
      --space-3: 0.75rem;
      --space-4: 1rem;
      --space-6: 1.5rem;
      --space-8: 2rem;
      --space-10: 2.5rem;
      --radius-sm: 0.25rem;
      --radius-md: 0.5rem;
      --radius-lg: 0.75rem;
      --radius-full: 9999px;
    }
    
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.6;
    }
    
    .page-wrapper {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }
    
    .main-content {
      flex: 1;
    }
    
    .site-header {
      background-color: var(--color-primary);
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }
    
    .main-nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 70px;
    }
    
    .logo {
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--color-accent);
      font-weight: 800;
      font-size: 20px;
      text-transform: uppercase;
      text-decoration: none;
      letter-spacing: 1px;
    }
    
    .logo-image {
      height: 50px;
    }
    
    .nav-menu {
      display: flex;
      list-style: none;
      gap: 30px;
    }
    
    .nav-link {
      color: var(--color-accent);
      font-weight: 600;
      text-decoration: none;
      padding: 8px 12px;
      border-radius: var(--radius-md);
      transition: background 0.3s;
      text-transform: uppercase;
      font-size: var(--font-size-sm);
      letter-spacing: 0.5px;
    }
    
    .nav-link:hover,
    .nav-link.active {
      background: rgba(255,255,255,0.2);
    }
    
    .mobile-menu-toggle {
      display: none;
      flex-direction: column;
      gap: 5px;
      background: none;
      border: none;
      cursor: pointer;
    }
    
    .mobile-menu-toggle span {
      width: 25px;
      height: 3px;
      background: var(--color-accent);
      border-radius: 2px;
    }
    
    @media (max-width: 768px) {
      .mobile-menu-toggle {
        display: flex;
      }
      
      .nav-menu {
        display: none;
        position: absolute;
        top: 70px;
        left: 0;
        right: 0;
        background: var(--color-primary);
        flex-direction: column;
        padding: 20px;
        gap: 10px;
      }
      
      .nav-menu.active {
        display: flex;
      }
      
      .nav-link {
        display: block;
        text-align: center;
      }
    }
    
    .section {
      padding: 60px 0;
    }
    
    .heading-1 {
      font-size: 48px;
      margin-bottom: 40px;
      color: var(--color-primary);
      text-align: center;
    }
    
    .heading-2 {
      font-size: 36px;
      margin-bottom: 30px;
      color: var(--color-primary);
      text-align: center;
    }
    
    .text-center {
      text-align: center;
    }
    
    .mb-8 {
      margin-bottom: 40px;
    }
    
    @media (max-width: 768px) {
      .heading-1 {
        font-size: 36px;
      }
      
      .heading-2 {
        font-size: 28px;
      }
    }
  </style>'''

host = "access831383027.webspace-data.io"
port = 22
user = "u101215843-1"
password = "OpenClawAssistant@SFTP"

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

pages = ['team', 'erfolge', 'geschichte', 'spielstaette', 'spielplan', 'events', 'galerie', 'pfingstturnier', 'social', 'vorstand']

for page in pages:
    try:
        remote_path = f"/demo-suwebsite/{page}/index.html"
        local_path = f"./src/{page}.html"
        
        sftp.get(remote_path, local_path)
        
        with open(local_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove all existing style tags
        content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
        
        # Add standard CSS after </head>
        content = content.replace('</head>', f'{STANDARD_CSS}\n</head>')
        
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        sftp.put(local_path, remote_path)
        print(f"✓ {page}")
        
    except Exception as e:
        print(f"✗ {page}: {e}")

sftp.close()
transport.close()
print("\n✅ All pages now have identical styling!")
