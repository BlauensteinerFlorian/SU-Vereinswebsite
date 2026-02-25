#!/usr/bin/env python3
from pathlib import Path

EVENTS_CSS = '''
    .events-list {
      max-width: 800px;
      margin: 0 auto;
    }

    .event-card {
      display: flex;
      gap: 30px;
      background: var(--bg-card);
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.3);
      margin-bottom: 20px;
    }

    .event-date {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: var(--color-primary);
      color: white;
      padding: 20px;
      border-radius: 8px;
      min-width: 100px;
      text-align: center;
    }

    .event-day {
      font-size: 24px;
      font-weight: 800;
    }

    .event-month {
      font-size: 14px;
      text-transform: uppercase;
    }

    .event-content {
      flex: 1;
    }

    .event-title {
      font-size: 24px;
      margin-bottom: 10px;
      color: var(--text-primary);
    }

    .event-desc {
      color: var(--text-secondary);
      margin-bottom: 15px;
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
    }

    .btn:hover {
      background: white;
      color: var(--color-primary);
    }

    @media (max-width: 640px) {
      .event-card {
        flex-direction: column;
      }
      
      .event-date {
        flex-direction: row;
        gap: 10px;
      }
    }
'''

# CSS für Footer (gleich wie bei Vorstand)
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
    }
'''

# Fix Events Seite
events_file = Path('src/events.html')
if events_file.exists():
    content = events_file.read_text(encoding='utf-8')
    if '.events-list' not in content:
        content = content.replace('</style>', EVENTS_CSS + FOOTER_CSS + '\n  </style>')
        events_file.write_text(content, encoding='utf-8')
        print("✓ Added CSS to events.html")

print("✅ Events CSS added!")
