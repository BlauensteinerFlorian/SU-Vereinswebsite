#!/usr/bin/env python3
from pathlib import Path

PFINGST_CSS = '''
    .pfingstturnier-content {
      max-width: 900px;
      margin: 0 auto;
    }

    .info-card {
      background: var(--bg-card);
      padding: 40px;
      border-radius: 12px;
      margin-bottom: 30px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }

    .info-card h2 {
      color: var(--color-primary);
      margin-bottom: 20px;
      font-size: 28px;
    }

    .info-card p {
      color: var(--text-secondary);
      line-height: 1.6;
      margin-bottom: 15px;
    }

    .info-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      margin-bottom: 30px;
    }

    .info-box {
      background: var(--bg-card);
      padding: 30px;
      border-radius: 12px;
      text-align: center;
      border-left: 4px solid var(--color-primary);
    }

    .info-box h3 {
      font-size: 20px;
      margin-bottom: 10px;
      color: var(--text-primary);
    }

    .info-box p {
      color: var(--text-secondary);
    }

    .btn {
      display: inline-block;
      padding: 12px 24px;
      background: var(--color-primary);
      color: white;
      text-decoration: none;
      border-radius: 8px;
      font-weight: 600;
      transition: all 0.3s;
      margin-top: 10px;
    }

    .btn:hover {
      background: white;
      color: var(--color-primary);
    }

    .mt-8 {
      margin-top: 40px;
    }

    @media (max-width: 640px) {
      .info-grid {
        grid-template-columns: 1fr;
      }
    }
'''

# Footer CSS (wie gehabt)
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
    }
'''

# Fix Pfingstturnier Seite
pfingst_file = Path('src/pfingstturnier.html')
if pfingst_file.exists():
    content = pfingst_file.read_text(encoding='utf-8')
    if '.pfingstturnier-content' not in content:
        content = content.replace('</style>', PFINGST_CSS + FOOTER_CSS + '\n  </style>')
        pfingst_file.write_text(content, encoding='utf-8')
        print("✓ Added CSS to pfingstturnier.html")

print("✅ Pfingstturnier CSS added!")
