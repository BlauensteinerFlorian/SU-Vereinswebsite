# Architektur-Entscheidung - SU-Vereinswebsite

## Optionen im Vergleich

### Option A: Plain HTML/CSS/JS (Vanilla)
**Stack:** Statische HTML-Dateien + CSS + Vanilla JS

**Pros:**
- Einfachst möglich
- Kein Build-Step
- Direkt auf dem Server editierbar
- Maximale Kontrolle

**Cons:**
- Wiederholung bei gleichen Komponenten (Header, Footer)
- Manuelle Pflege bei Änderungen
- Keine Templating-Logik

**Empfohlen für:** < 10 Seiten, keine häufigen Änderungen

---

### Option B: Static Site Generator (11ty)
**Stack:** 11ty + Nunjucks Templates + Markdown Content

**Pros:**
- Templating (Header/Footer einmal definieren)
- Markdown für Blog/News
- JSON-Daten für Spieler automatisch einbinden
- Build-Output ist reines HTML (schnell, SEO-freundlich)
- Ein Command: `npm run build`

**Cons:**
- Build-Step notwendig
- Node.js Abhängigkeit

**Empfohlen für:** Blog, häufige Content-Updates, Daten aus JSON

---

### Option C: JavaScript SPA (Alpine.js)
**Stack:** Alpine.js für Interaktivität + JSON-Daten

**Pros:**
- Dynamische Komponenten
- JSON-Daten direkt laden
- Kein Build-Step nötig
- Leichtgewichtig (~15kb)

**Cons:**
- SEO schwieriger (Client-Side Rendering)
- JS-Abhängigkeit

**Empfohlen für:** Hohe Interaktivität, weniger SEO-Fokus

---

## 🏆 Meine Empfehlung: Option B (11ty)

**Warum:**
1. **Blog/News:** Markdown-Files → automatisch HTML
2. **Team:** JSON (74 Spieler) → Template-Loop → HTML
3. **Pflege:** Florian ändert .md oder .json, pushed, deployed
4. **Performance:** Static HTML = schnellster Output
5. **Einfach:** Kein React/Vue lernen nötig

**Projektstruktur:**
```
src/
  ├── _includes/          # Templates
  │   ├── base.njk        # Haupt-Layout
  │   ├── header.njk      # Navigation
  │   └── footer.njk      # Footer + Map
  ├── _data/              # JSON Daten
  │   ├── players.json    # 74 Spieler
  │   ├── schedule.json   # Spielplan
  │   └── sponsors.json   # Sponsoren
  ├── css/
  ├── js/
  ├── index.njk           # Startseite
  ├── team.njk            # Mannschaft
  ├── blog/               # Markdown Posts
  │   ├── 2024-06-01-pokalsieg.md
  │   └── 2024-08-15-neuer-trainer.md
  └── spielplan.njk       # Spielplan
```

**Workflow:**
1. `npm run dev` → Live-Reload lokal
2. Content ändern (Markdown/JSON)
3. `npm run build` → `dist/` Ordner
4. `python scripts/deploy.py` → SFTP-Upload

**Alternative:** Option A (Vanilla) wenn du Build-Tools vermeiden willst.

---

## Entscheidung

| Kriterium | 11ty | Vanilla |
|-----------|------|---------|
| Einfachheit | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Blog/CMS | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| JSON-Daten | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Pflege | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Kein Build | ❌ | ✅ |

**Mein Vorschlag:** Wir starten mit **11ty** (Option B). Wenn du Build-Tools vermeiden willst, gehen wir auf **Vanilla** (Option A) und nutzen JavaScript für die JSON-Daten-Einbindung.

**Was sagst du?**
