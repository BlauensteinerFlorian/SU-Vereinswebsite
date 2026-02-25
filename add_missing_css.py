#!/usr/bin/env python3
from pathlib import Path

# CSS für Vorstand-Seite
VORSTAND_CSS = '''
    .vorstand-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 30px;
      max-width: 1200px;
      margin: 0 auto;
    }

    .vorstand-card {
      background: var(--bg-card);
      padding: 40px;
      border-radius: 12px;
      text-align: center;
      box-shadow: 0 4px 6px rgba(0,0,0,0.3);
      transition: transform 0.3s ease;
    }

    .vorstand-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    }

    .vorstand-bild {
      width: 100px;
      height: 100px;
      background: var(--bg-secondary);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 3rem;
      margin: 0 auto 20px;
    }

    .vorstand-name {
      font-size: 24px;
      font-weight: 700;
      margin-bottom: 10px;
      color: var(--text-primary);
    }

    .vorstand-position {
      display: block;
      color: var(--color-primary);
      font-weight: 600;
      margin-bottom: 15px;
      font-size: 16px;
    }

    .vorstand-email {
      color: var(--text-secondary);
      font-size: 14px;
      word-break: break-all;
      text-decoration: none;
    }

    .vorstand-email:hover {
      color: var(--color-primary);
    }
'''

# CSS für Footer
FOOTER_CSS = '''
    .site-footer {
      background: #0a0a0a;
      padding: 60px 0 30px;
      margin-top: auto;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 40px;
      max-width: 1200px;
      margin: 0 auto 40px;
      padding: 0 20px;
    }

    .footer-section {
      color: var(--text-secondary);
    }

    .footer-heading {
      color: var(--color-primary);
      font-size: 20px;
      font-weight: 700;
      margin-bottom: 20px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .footer-address {
      font-style: normal;
      line-height: 1.8;
    }

    .footer-founded {
      margin-top: 20px;
      color: var(--color-primary);
      font-weight: 600;
    }

    .footer-links {
      list-style: none;
    }

    .footer-links li {
      margin-bottom: 10px;
    }

    .footer-links a {
      color: var(--text-secondary);
      text-decoration: none;
      transition: color 0.3s;
    }

    .footer-links a:hover {
      color: var(--color-primary);
    }

    .social-links {
      display: flex;
      gap: 15px;
    }

    .social-link {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 44px;
      background: var(--bg-card);
      border-radius: 50%;
      color: var(--text-primary);
      transition: all 0.3s;
    }

    .social-link:hover {
      background: var(--color-primary);
      color: var(--color-accent);
      transform: translateY(-2px);
    }

    .map-container {
      border-radius: 8px;
      overflow: hidden;
    }

    .footer-bottom {
      border-top: 1px solid var(--bg-card);
      padding-top: 30px;
      display: flex;
      justify-content: space-between;
      max-width: 1200px;
      margin: 0 auto;
      padding: 30px 20px 0;
      color: var(--text-muted);
      font-size: 14px;
    }

    .footer-legal {
      display: flex;
      gap: 20px;
    }

    .footer-legal a {
      color: var(--text-muted);
      text-decoration: none;
    }

    .footer-legal a:hover {
      color: var(--color-primary);
    }

    @media (max-width: 1024px) {
      .footer-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 640px) {
      .footer-grid {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      
      .footer-bottom {
        flex-direction: column;
        text-align: center;
        gap: 20px;
      }
      
      .footer-legal {
        justify-content: center;
      }
      
      .vorstand-grid {
        grid-template-columns: 1fr;
      }
    }
'''

# Füge CSS zu Vorstand-Seite hinzu
vorstand_file = Path('src/vorstand.html')
if vorstand_file.exists():
    content = vorstand_file.read_text(encoding='utf-8')
    
    # Prüfe ob vorstand-grid CSS fehlt
    if '.vorstand-grid' not in content:
        # Füge vor dem schließenden </style> Tag ein
        content = content.replace('</style>', VORSTAND_CSS + FOOTER_CSS + '\n  </style>')
        vorstand_file.write_text(content, encoding='utf-8')
        print("✓ Added CSS to vorstand.html")

print("✅ Missing CSS added!")
