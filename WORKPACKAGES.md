# Arbeitspakete - SU-Vereinswebsite

**Projekt:** SU-Vereinswebsite für Sportunion Rudmanns  
**Deadline:** 01.04.2026 (fix)  
**Budget:** 1 Kiste Bier 🍺  
**Umsetzung:** Florian (Entwicklung), Florian Blauensteiner (Content)

---

## 📦 AP-1: Setup & Design-System

**Ziel:** Grundlegende technische Basis und visuelle Identität

**Zeitraum:** KW 9 (24.02. - 02.03.2026)  
**Status:** 🔴 Nicht begonnen  
**Priorität:** 🔴 Hoch (Blockiert weitere Arbeit)

### User Stories
- US-017: Dark Theme Design
- US-021: Header mit Navigation
- US-022: Hero Slider

### Deliverables
| Task | Status | Issue |
|------|--------|-------|
| CSS-Designsystem (Farben, Typography, Breakpoints) | 🔴 Offen | #1 |
| Header-Component mit Navigation | 🔴 Offen | #2 |
| Hero-Slider Komponente | 🔴 Offen | #3 |

### Akzeptanzkriterien
- [ ] Styleguide existiert in `/src/css/style.css`
- [ ] Alle MVP-Komponenten sind gestylt
- [ ] Mobile-First Responsive Design implementiert
- [ ] Header auf allen Seiten eingebunden
- [ ] Navigation funktioniert auf Desktop und Mobile

### Aufwandsschätzung
**~3-4 Tage**

---

## 📦 AP-2: Core Pages - Home & Navigation

**Ziel:** Hauptseiten und wiederkehrende Komponenten

**Zeitraum:** KW 9-10 (03.03. - 09.03.2026)  
**Status:** 🔴 Nicht begonnen  
**Priorität:** 🔴 Hoch (MVP)

### User Stories
- US-001: Vereinsinformationen anzeigen
- US-002: News-/Blog-Bereich (statisch zuerst)
- US-023: Sponsoren-Section
- US-024: Footer mit Karte

### Deliverables
| Task | Status | Issue |
|------|--------|-------|
| Startseite mit Hero + News | 🔴 Offen | #4 |
| Sponsoren-Grid/Slider (global) | 🔴 Offen | #5 |
| Footer mit Map + Social Links | 🔴 Offen | #6 |

### Akzeptanzkriterien
- [ ] Startseite zeigt Vereinsinfo, Gründungsjahr, Spielstätte
- [ ] Letzte 3 News-Artikel auf Startseite
- [ ] Sponsoren-Logos auf jeder Seite sichtbar
- [ ] Footer mit eingebetteter Karte funktioniert
- [ ] Responsive auf Mobile/Desktop getestet

### Abhängigkeiten
- AP-1 (Design-System muss fertig sein)

### Aufwandsschätzung
**~4-5 Tage**

---

## 📦 AP-3: Team-Präsentation

**Ziel:** Mannschafts- und Trainerübersicht

**Zeitraum:** KW 10 (06.03. - 12.03.2026)  
**Status:** 🔴 Nicht begonnen  
**Priorität:** 🔴 Hoch (MVP)

### User Stories
- US-003: Mannschaftsübersicht (74 Spieler)
- US-004: Trainer & Betreuer
- US-025: Team-Seite mit Spieler-Grid

### Deliverables
| Task | Status | Issue |
|------|--------|-------|
| Team-Seite mit Spieler-Grid (74 Spieler) | 🔴 Offen | #7 |
| Trainer/Betreuer Section | 🔴 Offen | #8 |
| CSV-Daten → JSON → HTML Rendering | 🔴 Offen | - |

### Akzeptanzkriterien
- [ ] Alle 74 Spieler aus CSV-Daten angezeigt
- [ ] Spieler-Bilder aus `/data/player_images/` verlinkt
- [ ] Name + Geburtsdatum für jeden Spieler
- [ ] Responsive Grid (1-2 Spalten Mobile, 3-4 Desktop)
- [ ] Trainer/Betreuer separat oder integriert

### Abhängigkeiten
- AP-1 (Design-System)
- AP-2 (Footer/Header)
- CSV-Daten bereits vorhanden ✅

### Aufwandsschätzung
**~2-3 Tage**

---

## 📦 AP-4: Spielbetrieb

**Ziel:** Spielplan, Ergebnisse, Tabelle, Kontakte

**Zeitraum:** KW 10-11 (10.03. - 16.03.2026)  
**Status:** 🔴 Nicht begonnen  
**Priorität:** 🔴 Hoch (MVP)

### User Stories
- US-005: Spielplan anzeigen
- US-006: Spielergebnisse anzeigen
- US-007: Ligatabelle anzeigen
- US-010: Ansprechpartner

### Deliverables
| Task | Status | Issue |
|------|--------|-------|
| Spielplan-Seite (Serie H) | 🔴 Offen | #9 |
| Ergebnisse-Seite | 🔴 Offen | #10 |
| Ligatabelle (manuelle Integration) | 🔴 Offen | #11 |
| Ansprechpartner/Kontakt-Seite | 🔴 Offen | #12 |

### Akzeptanzkriterien
- [ ] Spielplan mit Datum, Uhrzeit, Gegner
- [ ] Ergebnisse der gespielten Spiele
- [ ] Ligatabelle anzeigen (manuelle Pflege)
- [ ] Vorstand + Trainer als Ansprechpartner gelistet
- [ ] Kontaktdaten (E-Mail/Telefon) verlinkt

### Abhängigkeiten
- AP-1 (Design-System)
- AP-2 (Navigation)

### Aufwandsschätzung
**~3-4 Tage**

---

## 📦 AP-5: Content-Seiten

**Ziel:** Statische Inhalte und Vereinsgeschichte

**Zeitraum:** KW 11 (13.03. - 19.03.2026)  
**Status:** 🔴 Nicht begonnen  
**Priorität:** 🟡 Mittel (Optional für MVP)

### User Stories
- US-008: Vereinsgeschichte
- US-009: Vorstand
- US-011: Spielstätte
- US-018: Erfolge hervorheben
- US-019: Prominente Mitglieder

### Deliverables
| Task | Status | Issue |
|------|--------|-------|
| Vereinsgeschichte Timeline | 🔴 Offen | #13 |
| Vorstand-Seite (kombinierbar mit #12) | 🔴 Offen | #14 |
| Spielstätte mit Anfahrt | 🔴 Offen | #15 |
| Erfolge (Pokalsieg 2024) | 🔴 Offen | #16 |
| Prominente Mitglieder | 🔴 Offen | #16 |

### Akzeptanzkriterien
- [ ] Geschichte chronologisch dargestellt
- [ ] Pokalsieg 2024 prominent hervorgehoben
- [ ] Vorstandsmitglieder mit Fotos
- [ ] Spielstätte mit Anfahrtsbeschreibung
- [ ] "Steger Wuff" und "Expräsi Bruchsi" vorgestellt

### Abhängigkeiten
- Texte/Fotos vom Verein erforderlich ⚠️

### Aufwandsschätzung
**~2-3 Tage** (wenn Material vorhanden)

---

## 📦 AP-6: Erweiterte Features (Phase 2)

**Ziel:** Interaktive Features und Integrationen

**Zeitraum:** KW 11-12 (17.03. - 26.03.2026)  
**Status:** 🔴 Nicht begonnen  
**Priorität:** 🟢 Niedrig/Mittel (Nach MVP)

### User Stories
- US-026: Blog mit Detailseiten
- US-027: Pfingstturnier-Countdown
- US-028: Turnier-Anmeldeformular
- US-029: Events-Seite
- US-012: Fotogalerie
- US-016: Instagram Integration

### Deliverables
| Task | Status | Issue |
|------|--------|-------|
| Blog mit .md → JSON System | 🔴 Offen | #17 |
| Pfingsturnier-Countdown | 🔴 Offen | #18 |
| Turnier-Anmeldeformular | 🔴 Offen | #19 |
| Events-Seite | 🔴 Offen | #20 |
| Fotogalerie mit Lightbox | 🔴 Offen | #21 |
| Instagram Feed Integration | 🔴 Offen | #22 |

### Akzeptanzkriterien
- [ ] Blog-Artikel können als .md hinzugefügt werden
- [ ] Countdown zeigt korrekt bis Pfingstsonntag
- [ ] Formular sendet E-Mail an florian.blauen@gmail.com
- [ ] Galerie mit Lightbox-Navigation
- [ ] Instagram-Posts werden auf Website angezeigt

### Abhängigkeiten
- CMS/Backend-Lösung wählen (Netlify, Formspree, o.ä.)

### Aufwandsschätzung
**~5-7 Tage** (hohe Varianz je nach gewählten Features)

---

## 📦 AP-7: Integration & Commerce

**Ziel:** Sponsoren-Vollständigkeit und Fan-Shop

**Zeitraum:** KW 11 (17.03. - 19.03.2026)  
**Status:** 🔴 Nicht begonnen  
**Priorität:** 🟡 Mittel

### User Stories
- US-015: Fan-Shop
- US-030: Fanshop (redundant)
- US-013: Sponsoren-Präsentation

### Deliverables
| Task | Status | Issue |
|------|--------|-------|
| Sponsoren-Logos hochladen | 🔴 Offen | #24 |
| Sponsoren-Verlinkungen | 🔴 Offen | #24 |
| Fan-Shop (statisch mit Mail-Bestellung) | 🔴 Offen | #23 |

### Akzeptanzkriterien
- [ ] Alle Sponsorenlogos vorhanden und verlinkt
- [ ] Shop-Seite mit Artikeln
- [ ] "Per E-Mail bestellen"-Button funktioniert

### Abhängigkeiten
- Materialien: Sponsorenlogos ⚠️

### Aufwandsschätzung
**~2 Tage**

---

## 📦 AP-8: Testing & Go-Live

**Ziel:** Qualitätssicherung und Live-Schaltung

**Zeitraum:** KW 12 (24.03. - 01.04.2026)  
**Status:** 🔴 Nicht begonnen  
**Priorität:** 🔴 Hoch (Blockiert Go-Live)

### User Stories
- US-020: Impressum & Datenschutz (gesetzlich erforderlich!)

### Deliverables
| Task | Status | Issue |
|------|--------|-------|
| Impressum erstellen | 🔴 Offen | #25 |
| Datenschutzerklärung (DSGVO) | 🔴 Offen | #25 |
| Responsive Testing | 🔴 Offen | #26 |
| Performance Optimierung | 🔴 Offen | #27 |
| Cross-Browser Testing | 🔴 Offen | #28 |
| Deployment Script testen | 🔴 Offen | #29 |
| Domain-Setup & Go-Live | 🔴 Offen | #30 |

### Akzeptanzkriterien
- [ ] Impressum + Datenschutz vorhanden (rechtskonform)
- [ ] Mobile/Desktop Responsive getestet
- [ ] Lighthouse-Score > 90
- [ ] Chrome, Firefox, Safari getestet
- [ ] Deployment funktioniert zuverlässig
- [ ] Domain aufgesetzt (surudmanns.at)
- [ ] HTTPS aktiviert
- [ ] Go-Live am 01.04.2026

### Abhängigkeiten
- Alle anderen APs müssen fertig sein

### Aufwandsschätzung
**~3-4 Tage**

---

## 📊 Übersicht & Timeline

```
KW 9        KW 10       KW 11       KW 12
|           |           |           |
[AP-1]      [AP-3]      [AP-5]      [AP-8]
[AP-2]      [AP-4]      [AP-6]      
                        [AP-7]
```

### Priorisierung für Florian

**Phase 1 (MVP - Muss bis 01.04.):**
1. ✅ AP-1: Setup & Design (KW 9)
2. ✅ AP-2: Core Pages (KW 9-10)
3. ✅ AP-3: Team-Präsentation (KW 10)
4. ✅ AP-4: Spielbetrieb (KW 10-11)
5. ✅ AP-8: Testing & Go-Live (KW 12)

**Phase 2 (Optional - Wenn Zeit bleibt):**
6. ⭕ AP-5: Content-Seiten (KW 11)
7. ⭕ AP-7: Sponsoren vollständig (KW 11)
8. ⭕ AP-6: Erweiterte Features (KW 11-12)

### Gesamtaufwand
**Geschätzt: 24-32 Tage (reine Arbeitszeit)**
- Bei 50% Auslastung: ~6-8 Wochen
- Deadline ist machbar bei Fokus auf MVP (AP-1 bis AP-4 + AP-8)

### Kritische Pfad
```
AP-1 → AP-2 → AP-3 → AP-4 → AP-8
```

---

## ⚠️ Blocker & Risiken

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Materialien fehlen (Fotos, Texte) | Hoch | Mittel | Frühzeitig anfragen, Platzhalter nutzen |
| Design-Änderungen | Mittel | Mittel | Styleguide früh festlegen |
| Hosting-Probleme | Niedrig | Hoch | Früh testen, Backup-Plan |
| Zeitdruck | Hoch | Hoch | Fokus auf MVP, Nice-to-have verschieben |

---

## 📝 Nächste Schritte

1. **AP-1 starten:** Design-System aufsetzen
2. **Materialien sammeln:** Sponsorenlogos, Team-Fotos, Texte anfordern
3. **Domain prüfen:** surudmanns.at verfügbar?
4. **GitHub Issues anlegen:** Aus GITHUB-ISSUES.md übernehmen

---

*Erstellt am: 22.02.2026*  
*Autor: Jarvis (AI Assistant)*  
*Version: 1.0*
