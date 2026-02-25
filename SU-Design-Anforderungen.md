# Zusätzliche Design-Anforderungen - SU-Vereinswebsite

**Datum:** 22.02.2026  
**Quelle:** Florian (direkte Anforderung)

---

## 1. Globale Struktur (alle Seiten)

### Header (fixiert oben)
- **Farbe:** Orange (Vereinsfarbe)
- **Elemente:**
  - Logo
  - Navigation-Menü: **Home | Team | Blog | Pfingsturnier | Events | Fanshop**

### Content-Bereich
- Individuell pro Seite (siehe unten)

### Sponsoren-Section
- **Position:** Unter dem Content auf jeder Seite
- **Inhalt:** Alle Sponsoren-Logos
- **Darstellung:** Grid oder Slider

### Footer (alle Seiten)
- **Elemente:**
  - Link zu Impressum
  - Social Media Links: **Instagram, Facebook**
  - **Karten-Integration:** Google Maps/OpenStreetMap zum Birkenstadion Stift Zwettl

---

## 2. Seiten-spezifische Anforderungen

### Home (Startseite)

**Aufbau von oben nach unten:**
1. **Slider** - Großes Bild/Karussell (hero section)
2. **Content/Text** - Willkommenstext, aktuelle News
3. **Sponsoren-Section**
4. **Footer**

---

### Team

**Aufbau von oben nach unten:**
1. **Slider** - Großes Bild (Mannschaftsfoto oder Stadion)
2. **Content:**
   - **Spieler-Liste:**
     - Bild (aus data/player_images/)
     - Voller Name
     - Geburtsdatum
   - Grid-Layout oder Listen-Layout
3. **Sponsoren-Section**
4. **Footer**

**Technisch:**
- Datenquelle: `data/su_players.csv` (74 Spieler)
- Bilder: `data/player_images/`

---

### Blog

**Aufbau von oben nach unten:**
1. **Blog-Übersicht:**
   - Liste aller Blogposts
   - Titel, Vorschautext, Datum, Bild
   - Link zur **Detailseite**
2. **Sponsoren-Section**
3. **Footer**

**Blogpost-Detailseite:**
- Vollständiger Artikel
- **Social Share Button** (Teilen-Funktion)
- Zurück-Link zur Blog-Übersicht

**Technisch:**
- Content-Management: Einfach via Markdown/HTML
- Social Share: Facebook, Twitter/X, WhatsApp

---

### Pfingsturnier

**Aufbau von oben nach unten:**
1. **Countdown** - Großer Timer bis Pfingstsonntag (jährlich aktualisieren)
2. **Turnier-Info** - Kurzer Text mit Informationen zum Turnier
3. **Kontaktformular:**
   - Pflichtfelder:
     - Teamname
     - Nachricht/Text
     - E-Mail
   - Optional:
     - Telefonnummer
   - Absenden-Button → Anmeldung
4. **Sponsoren-Section**
5. **Footer**

**Technisch:**
- Countdown: JavaScript (targetDate = Pfingstsonntag aktuelles Jahr)
- Formular: HTML-Formular (E-Mail-Versand via backend oder Formspree)

---

### Events

**Aufbau von oben nach unten:**
1. **Event-Liste:**
   - Datum, Titel, Beschreibung
   - Veranstaltungskalender
2. **Sponsoren-Section**
3. **Footer**

---

### Fanshop

**Aufbau von oben nach unten:**
1. **Shop-Übersicht:**
   - Artikel-Bilder
   - Preise
   - In den Warenkorb / Bestellen
2. **Sponsoren-Section**
3. **Footer**

**Technisch:**
- Einfacher Shop (kein komplexer Checkout)
- Oder: Weiterleitung zu externem Shop

---

## 3. Technische Implementierungsdetails

### Farbschema (Vereinsfarben)
```css
--primary: #FF6600;    /* Orange - Header */
--secondary: #000000;  /* Schwarz */
--accent: #FFFFFF;     /* Weiß */
--background: #FFFFFF; /* Weiß für Content */
```

### Navigation
- **Desktop:** Horizontales Menü
- **Mobile:** Hamburger-Menü
- **Aktive Seite:** Visuell hervorgehoben

### Slider (Home & Team)
- Auto-Play (optional)
- Manuelle Navigation (Pfeile/Punkte)
- Responsive (verschiedene Bildgrößen für Mobile/Desktop)

### Karten-Integration (Footer)
- **Ziel:** Birkenstadion, Stift Zwettl
- **Provider:** Google Maps oder OpenStreetMap (datenschutzfreundlicher)
- **Funktion:** Klick öffnet externe Karte (Google Maps App/Website)

### Social Share (Blog)
- **Plattformen:** Facebook, X/Twitter, WhatsApp, E-Mail
- **Funktion:** Aktuelle URL teilen

---

## 4. Neue/aktualisierte User Stories

### US-021: Header mit Navigation
**Als** Besucher  
**möchte ich** eine klare Navigation haben  
**damit** ich alle Seiten finden kann.

**AK:**
- [ ] Orangener Header
- [ ] Menüpunkte: Home, Team, Blog, Pfingsturnier, Events, Fanshop
- [ ] Mobile-responsive (Hamburger-Menü)

### US-022: Hero Slider (Home & Team)
**Als** Besucher  
**möchte ich** ansprechende Bilder sehen  
**damit** die Website professionell wirkt.

**AK:**
- [ ] Großes Slider-Bild oben
- [ ] Automatisches Rotieren (optional)
- [ ] Manuelle Steuerung

### US-023: Sponsoren-Section
**Als** Sponsor  
**möchte ich** prominent platziert werden  
**damit** meine Unterstützung sichtbar ist.

**AK:**
- [ ] Auf jeder Seite unter dem Content
- [ ] Logo-Grid
- [ ] Verlinkung zu Sponsoren-Websites

### US-024: Footer mit Karte
**Als** Besucher  
**möchte ich** den Standort finden  
**damit** ich zum Stadion komme.

**AK:**
- [ ] Karten-Einbettung (Birkenstadion)
- [ ] Social Media Links
- [ ] Impressum-Link

### US-025: Team-Seite mit Spieler-Grid
**Als** Fan  
**möchte ich** alle Spieler sehen  
**damit** ich die Mannschaft kenne.

**AK:**
- [ ] Grid-Layout mit Bild, Name, Geburtsdatum
- [ ] Alle 74 Spieler aus CSV
- [ ] Responsive (Mobile: 1-2 Spalten, Desktop: 3-4 Spalten)

### US-026: Blog mit Detailseiten
**Als** Besucher  
**möchte ich** Artikel lesen und teilen  
**damit** ich informiert bin.

**AK:**
- [ ] Übersichtsseite mit Vorschau
- [ ] Detailseite pro Artikel
- [ ] Social Share Buttons

### US-027: Pfingsturnier-Countdown
**Als** Interessent  
**möchte ich** sehen wie lange es noch dauert  
**damit** ich mich vorbereiten kann.

**AK:**
- [ ] Großer Countdown (Tage, Stunden, Minuten)
- [ ] Automatisch bis Pfingstsonntag
- [ ] Jährlich neu (reset nach Turnier)

### US-028: Turnier-Anmeldeformular
**Als** Team  
**möchte ich** mich online anmelden  
**damit** wir am Turnier teilnehmen können.

**AK:**
- [ ] Felder: Teamname, Nachricht, E-Mail (Pflicht)
- [ ] Optional: Telefon
- [ ] Absenden-Button
- [ ] E-Mail-Benachrichtigung an Verein

---

## 5. Priorisierung

**MVP (Minimum Viable Product) für 01.04.2026:**
1. ✅ Header mit Navigation
2. ✅ Home-Seite mit Slider
3. ✅ Team-Seite mit Spieler-Liste
4. ✅ Sponsoren-Section
5. ✅ Footer mit Karte und Social Links
6. ✅ Impressum

**Phase 2 (nach Go-Live):**
- Blog mit CMS
- Pfingsturnier-Countdown + Anmeldung
- Events-Seite
- Fanshop
- Social Share

---

## 6. Dateien & Resourcen

**Bereitgestellte Daten:**
- `data/su_players.csv` - 74 Spieler mit Namen, Geburtsdaten
- `data/player_images/` - 74 Spieler-Fotos

**Noch benötigt:**
- Slider-Bilder (Home & Team)
- Sponsoren-Logos (hochauflösend)
- Texte für Home, Pfingsturnier, etc.
- Instagram/Facebook Links

---

*Dokument erstellt: 22.02.2026*  
*Autor: Jarvis (AI Assistant)*
