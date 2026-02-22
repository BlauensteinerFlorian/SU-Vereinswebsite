# GitHub Issues - SU-Vereinswebsite

Diese Issues müssen in GitHub angelegt werden. Sie sind gruppiert nach Arbeitspaketen.

---

## 🏗️ AP-1: Setup & Design-System

### Issue #1: Design-System erstellen (US-017)
**Labels:** `design`, `high-priority`, `MVP`
**Assignee:** Florian
**Story:** US-017 - Dark Theme Design

**Beschreibung:**
- CSS-Variablen mit Farbpalette (#FF6600, Schwarz, Weiß)
- Typografie definieren
- Responsive Breakpoints festlegen
- Komponenten-Library (Buttons, Cards, Navigation)

**Akzeptanzkriterien:**
- [ ] Styleguide existiert in `/src/css/style.css`
- [ ] Farbvariablen implementiert
- [ ] Mobile-First Responsive Design
- [ ] Alle MVP-Komponenten gestylt

---

### Issue #2: Header mit Navigation (US-021)
**Labels:** `component`, `high-priority`, `MVP`, `navigation`
**Assignee:** Florian
**Story:** US-021

**Beschreibung:**
- Orangener Header (#FF6600)
- Menü: Home, Team, Blog, Pfingstturnier, Events, Fanshop
- Mobile Responsive (Hamburger)
- Aktive Seite visuell markiert

**Akzeptanzkriterien:**
- [ ] Header-Component gebaut
- [ ] Hover- und Active-States
- [ ] Mobile Navigation funktioniert

---

### Issue #3: Hero Slider Komponente (US-022)
**Labels:** `component`, `high-priority`, `MVP`

**Beschreibung:**
- Slider mit 3-5 Bildern
- Automatisches Rotieren (5 Sekunden)
- Manuelle Steuerung
- Responsive Bilder

---

## 📄 AP-2: Core Pages - Home & Navigation

### Issue #4: Startseite (Home) (US-001, US-002, US-023, US-024)
**Labels:** `page`, `high-priority`, `MVP`
**Story:** US-001, US-002

**Beschreibung:**
- Hero-Bereich mit Vereinslogo + Name
- News-Übersicht (letzte 3 Beiträge)
- Statisches HTML zuerst, später CMS-fähig

**Akzeptanzkriterien:**
- [ ] Vereinsinfo prominent angezeigt
- [ ] Gründungsjahr 1988 sichtbar
- [ ] Spielstätte vermerkt
- [ ] Letzte News aufgelistet
- [ ] "Sponsoren"-Section integriert

---

### Issue #5: Sponsoren-Section (US-023)
**Labels:** `component`, `high-priority`, `MVP`

**Beschreibung:**
- Auf jeder Seite unter Hauptcontent
- Logo-Grid oder Slider
- Verlinkung zu Sponsoren-Websites
- Responsive (4 Mobil, 6-8 Desktop)

---

### Issue #6: Footer mit Karte (US-024)
**Labels:** `component`, `high-priority`, `MVP`

**Beschreibung:**
- Google Maps / OpenStreetMap Einbettung
- 🚦 Birkenstadion, Stift Zwettl
- 🚦 Social Media Links (Instagram, Facebook)
- Impressum-Link

---

## 👥 AP-3: Team-Präsentation

### Issue #7: Mannschaftsübersicht (US-003, US-025)
**Labels:** `page`, `high-priority`, `MVP`

**Beschreibung:**
- Grid-All-74 Spieler aus CSV-Daten laden
- Bild aus `/data/player_images/`
- Name + Geburtsdatum anzeigen
- Responsive (1-2 mobil, 3-4 Desktop)

**Akzeptanzkriterien:**
- [ ] Alle 74 Spieler aus `hobbyliga_birthdates.json` anzeigen
- [ ] Bilder korrekt verlinkt
- [ ] Grid-Layout funktioniert auf Mobile

---

### Issue #8: Trainer & Betreuer (US-004)
**Labels:** `page`, `high-priority`, `MVP`

**Beschreibung:**
- Separate Section oder eigene Seite?
- Fotos + Namen + Positionen
- Kontaktdaten (E-Mail/Telefon)

---

## ⚽ AP-4: Spielbetrieb

### Issue #9: Spielplan (US-005)
**Labels:** `feature`, `high-priority`, `MVP`

**Beschreibung:**
- Spielplan für Serie H
- Monatsansicht oder Listenansicht
- Filter: Vergangen/Zukünftig
- Manuelle Aktualisierung möglich

---

### Issue #10: Ergebnisse (US-006)
**Labels:** `feature`, `high-priority`, `MVP`

**Beschreibung:**
- Tabelle mit gespielten Spielen
- Ergebnis-Anzeige
- Saisonverlauf

---

### Issue #11: Ligatabelle (US-007)
**Labels:** `feature`, `medium-priority`

**Beschreibung:**
- Serie H-Tabelle integrieren
- Automatisch von Hobbyliga.at scrapen ODER
- Manuelle Pflege (zuerst)

---

### Issue #12: Ansprechpartner (US-010)
**Labels:** `page`, `high-priority`, `MVP`

**Beschreibung:**
- Vorstand + Funktionen
- Trainer-Kontakte
- E-Mail/Telefon-Links

---

## 📜 AP-5: Content-Seiten

### Issue #13: Vereinsgeschichte (US-008)
**Labels:** `content`, `medium-priority`

**Beschreibung:**
- Timeline-Layout (1988 - heute)
- Pokalsieg 2024 hervorgehoben
- Chronologisch sortierbar

---

### Issue #14: Vorstand (US-009)
**Labels:** `content`, `medium-priority`

**Beschreibung:**
- Vorstandsmitglieder mit Fotos
- Funktionen/Aufgabenbereiche
- Kontaktmöglichkeiten

**Hinweis:** Kann mit Issue #12 kombiniert werden

---

### Issue #15: Spielstätte (US-011)
**Labels:** `content`, `medium-priority`

**Beschreibung:**
- Birkenstadion beschreiben
- Anfahrt (Auto, Öffis)
- Parkplatz-Info
- Karte bereits im Footer

---

### Issue #16: Erfolge & Prominente (US-018, US-019)
**Labels:** `content`, `low-priority`

**Beschreibung:**
- Pokalsieg 2024: Bilder + Bericht
- Steger Wuff & Expräsi Bruchsi vorstellen
- Optional: Weitere Meilensteine

---

## 🔥 AP-6: Erweiterte Features (Phase 2)

### Issue #17: Blog mit CMS-Integration (US-026)
**Labels:** `feature`, `medium-priority`, `CMS`, `Phase-2`

**Beschreibung:**
- Übersicht + Detailseiten
- Social Share Buttons (FB, X, WhatsApp)
- Einfache Pflege (Ranking: 1. Static > 2. Headless CMS > 3. Custom)

**Empfohlener Ansatz:** 
- .md-Files in `/content/posts/`
- Build-Script generiert JSON
- Client-Side Rendering

---

### Issue #18: Pfingstturnier-Countdown (US-027)
**Labels:** `feature`, `medium-priority`, `Phase-2`

**Beschreibung:**
- Countdown: Tage, Stunden, Minuten, Sekunden
- Jährlich automatisch reset auf Pfingstsonntag
- Visuell ansprechend

---

### Issue #19: Turnier-Anmeldung (US-028)
**Labels:** `feature`, `medium-priority`, `Phase-2`, `form`

**Beschreibung:**
- Formular: Teamname, Nachricht, E-Mail
- Optional: Telefon
- E-Mail an florian.blauen@gmail.com bei Submit

**Technisch:**
- Netlify Forms, Formspree, oder PHP-Backend

---

### Issue #20: Events-Seite (US-014, US-029)
**Labels:** `feature`, `low-priority`, `Phase-2`

**Beschreibung:**
- Event-Liste mit Datum
- Veranstaltungskalender (optional)
- Kombinierbar mit Turnier-Anmeldung

---

### Issue #21: Fotogalerie (US-012)
**Labels:** `feature`, `medium-priority`, `Phase-2`

**Beschreibung:**
- Lightbox-Integration
- Alben: Spieler, Events, Spiele
- Bildschutz gegen Hotlinking

---

### Issue #22: Instagram Integration (US-016)
**Labels:** `feature`, `medium-priority`, `Phase-2`

**Beschreibung:**
- Instagram Feed (API oder Embed)
- Limit auf z.B. 6 letzte Posts
- Performance: Lazy Loading

---

## 🛒 AP-7: Integration & Commerce

### Issue #23: Fan-Shop (US-015, US-030)
**Labels:** `feature`, `low-priority`, `Phase-2`, `commerce`

**Beschreibung:**
- Artikel-Übersicht
- Preisanzeige
- Variante A: Direkte Zahlung (Stripe/PayPal)
- Variante B: Bestellformular per E-Mail

**Empfohlener MVP-Ansatz:**
- Statische Seite mit "Per Mail bestellen"-Button
- Keine komplexe Payment-Integration

---

### Issue #24: Sponsoren-Präsentation vollständig (US-013)
**Labels:** `content`, `high-priority`, `MVP`

**Beschreibung:**
- Sponsorenlogos hochladen
- Firmenwebsites verlinken
- Grid oder Slider entscheiden

---

## ✅ AP-8: Testing & Go-Live

### Issue #25: Impressum & Datenschutz (US-020)
**Labels:** `legal`, `high-priority`, `MVP`, `blocking`

**Beschreibung:**
- **RECHTLICH ERFORDERLICH VOR GO-LIVE!**
- Impressum (Vereinsname, Adresse, Amtsregister)
- Datenschutzerklärung (DSGVO-konform)
- Cookie-Banner falls nötig

**Quellen:**
- Vereinsdaten vom Fragebogen
- Muster von Vereinswebseiten

---

### Issue #26: Responsive Testing
**Labels:** `QA`, `high-priority`

**Beschreibung:**
- Mobile: iPhone SE, iPhone Pro, Android
- Tablet: iPad Mini, iPad Pro
- Desktop: 1080p, 1440p, Ultrawide
- Browser: Chrome, Safari, Firefox, Edge

---

### Issue #27: Performance Optimierung
**Labels:** `QA`, `medium-priority`

**Beschreibung:**
- Ladezeit < 2 Sekunden
- Lighthouse-Score: >90
- Bilderoptimierung (WebP, Lazy Loading)
- Minification (CSS, JS)

---

### Issue #28: Cross-Browser Testing
**Labels:** `QA`, `high-priority`

**Beschreibung:**
- Chrome/Edge (Chromium)
- Firefox
- Safari (iOS + macOS)
- Keine polyfills für IE erforderlich

---

### Issue #29: Deployment ins Demo-Verzeichnis
**Labels:** `deployment`, `high-priority`, `MVP`

**Beschreibung:**
- `script/deploy.py` anpassen auf `demo-suwebsite/`
- SFTP-Upload testen
- Rollback-Strategie definiert

---

### Issue #30: Domain-Setup & Go-Live
**Labels:** `deployment`, `high-priority`

**Beschreibung:**
- Domain bestellen: surudmanns.at (empfohlen)
- DNS-Einträge konfigurieren
- SSL-Zertifikat (HTTPS)
- 301 Redirects (falls nötig)

---

## 📊 Zusammenfassung

| Arbeitspaket | Issues | Priorität | Timeline |
|-------------|--------|-----------|----------|
| AP-1: Setup & Design | #1-#3 | Hoch | KW 9 |
| AP-2: Core Pages | #4-#6 | Hoch | KW 9-10 |
| AP-3: Team | #7-#8 | Hoch | KW 10 |
| AP-4: Spielbetrieb | #9-#12 | Hoch | KW 10 |
| AP-5: Content | #13-#16 | Mittel | KW 11 |
| AP-6: Features P2 | #17-#22 | Niedrig/Mittel | KW 11-12 |
| AP-7: Integration | #23-#24 | Mittel | KW 11 |
| AP-8: Testing | #25-#30 | Hoch | KW 12 |

**Deadline: 01.04.2026**

---
*Automatisch generiert am: 22.02.2026*
