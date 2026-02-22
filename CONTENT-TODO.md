# 📋 CONTENT-TODO - Fehlende Inhalte für SU-Vereinswebsite

**Projekt:** SU-Vereinswebsite  
**Status:** AP-1 & AP-2 implementiert (Design-System + Core Pages)  
**Letzte Aktualisierung:** 22.02.2026

---

## 🖼️ BILDER & GRAFIKEN

### Hero-Slider (Startseite)
| Datei | Pfad | Beschreibung | Status |
|-------|------|--------------|--------|
| `team-2024.jpg` | `/src/assets/hero/` | Mannschaftsfoto 2024 | ❌ FEHLEND |
| `pokal-2024.jpg` | `/src/assets/hero/` | Pokalsieg-Feier 2024 | ❌ FEHLEND |
| `pfingstturnier.jpg` | `/src/assets/hero/` | Pfingstturnier-Actionshot | ❌ FEHLEND |

**Empfohlene Größe:** 1920x1080px (16:9)  
**Format:** JPG oder WebP  
**Anforderung:** Hochwertig, dynamisch, Vereinsfarbe Orange sollte erkennbar sein

### Vereinslogo
| Datei | Pfad | Beschreibung | Status |
|-------|------|--------------|--------|
| `logo-su-rudmanns.svg` | `/src/assets/` | Hauptlogo als SVG | ❌ FEHLEND |
| `logo-su-rudmanns.png` | `/src/assets/` | Fallback PNG (500x500px) | ❌ FEHLEND |
| `favicon.svg` | `/src/assets/` | Favicon für Browser-Tab | ❌ FEHLEND |

**Anforderung:**
- Transparente Hintergründe (SVG/PNG)
- Vereinsfarben: Orange (#FF6600), Schwarz, Weiß
- Auch als weiße Version für dunkle Hintergründe

### Spieler-Bilder
| Pfad | Anzahl | Status |
|------|--------|--------|
| `/data/player_images/` | 19 Bilder | ⚠️ VORHANDEN aber prüfen |

**Bisherige Bilder:**
- `1_DANGL.png`, `7_GRETZ.png`, `5_KIRCHNER.png`, etc.

**TODO:**
- [ ] Alle 19 Spieler-Bilder auf aktuelles Format prüfen
- [ ] Falls neue Spieler dazugekommen: Bilder nachreichen
- [ ] Einheitliches Format (idealerweise 400x500px, Portrait)

### Sponsoren-Logos
| Pfad | Beschreibung | Status |
|------|--------------|--------|
| `/src/assets/sponsors/sponsor1.svg` | Hauptsponsor | ❌ FEHLEND |
| `/src/assets/sponsors/sponsor2.svg` | Premiumpartner | ❌ FEHLEND |
| `/src/assets/sponsors/sponsor3.svg` | Partner | ❌ FEHLEND |
| `/src/assets/sponsors/sponsor4.svg` | Partner | ❌ FEHLEND |

**Anforderung:**
- SVG-Format (Vektor = skalierbar)
- Falls kein SVG verfügbar: PNG mit transparentem Hintergrund
- Max-Höhe: 80px
- Graustufen-Filter wird automatisch angewendet (Hover = Farbe)

### News/Beitrags-Bilder
| Pfad | Beschreibung | Status |
|------|--------------|--------|
| `/src/assets/news/pokalsieg-2024.jpg` | Pokalsieg-Feier | ❌ FEHLEND |
| `/src/assets/news/saisonstart-2024.jpg` | Saisonstart | ❌ FEHLEND |
| `/src/assets/news/...` | Weitere News-Bilder | ❌ FEHLEND |

**Empfohlene Größe:** 800x600px (4:3) oder 1200x675px (16:9)

---

## 📝 TEXTE & INHALTE

### Startseite
| Bereich | Text/Inhalt | Status |
|---------|-------------|--------|
| Hero-Subtitle | "Hobby-Liga-Fußball aus Stift Zwettl seit 1988" | ✅ VORHANDEN (kann angepasst werden) |
| Vereinsbeschreibung | Kurzbeschreibung des Vereins | ✅ VORHANDEN (kann erweitert werden) |

### News/Beiträge (Blog)
**Aktuell:** Nur Beispiel-Content  
**Benötigt:** Echte News-Beiträge als Markdown-Dateien

**Format pro Beitrag:**
```markdown
---
title: "Titel der News"
date: 2024-06-15
image: /assets/news/bild.jpg
excerpt: "Kurze Zusammenfassung..."
---

Hier der vollständige Text...
```

**Vorschläge für erste Beiträge:**
- [ ] Pokalsieg 2024 (Bericht + Fotos)
- [ ] Saisonvorschau 2024/25
- [ ] Neuzugänge im Team
- [ ] Rückblick Pfingstturnier 2024

### Spielplan & Ergebnisse
**Benötigte Daten:**
- [ ] Kompletter Spielplan Serie H (Datum, Uhrzeit, Gegner, Ort)
- [ ] Bereits gespielte Spiele mit Ergebnissen
- [ ] Aktuelle Ligatabelle (JSON oder manuelle Eingabe)

**Format:**
```json
{
  "spiele": [
    {
      "datum": "2024-09-15",
      "uhrzeit": "15:00",
      "gegner": "FC Musterdorf",
      "ort": "Heim/Auswärts",
      "ergebnis": "3:1" // oder null für zukünftige Spiele
    }
  ]
}
```

### Trainer & Betreuer
**Benötigt:**
- [ ] Name des Trainers
- [ ] Name des Co-Trainers (falls vorhanden)
- [ ] Betreuer
- [ ] Fotos (idealerweise 400x500px, Portrait)
- [ ] Kurze Vorstellung/Biografie (optional)

### Vorstand
**Benötigt:**
- [ ] Vorstandsvorsitzender (Name, Funktion, Kontakt)
- [ ] Stellvertreter
- [ ] Kassier
- [ ] Schriftführer
- [ ] Weitere Vorstandsmitglieder
- [ ] Fotos (optional)

### Vereinsgeschichte
**Benötigt:**
- [ ] Wichtige Meilensteine (chronologisch)
- [ ] Gründungsgeschichte 1988
- [ ] Pokalsieg 2024 (detailliert)
- [ ] Historische Fotos (optional)

**Format:** Timeline mit Jahreszahlen

### Ansprechpartner
**Benötigt:**
- [ ] Komplette Liste mit:
  - Name
  - Funktion (Vorstand, Trainer, etc.)
  - E-Mail
  - Telefon (optional)

### Spielstätte (Birkenstadion)
**Benötigt:**
- [ ] Detaillierte Beschreibung der Anlage
- [ ] Anfahrtsbeschreibung (Auto)
- [ ] Anfahrt mit Öffentlichen (falls vorhanden)
- [ ] Parkplatz-Informationen
- [ ] Fotos vom Stadion (optional)

### Impressum (RECHTLICH ERFORDERLICH!)
**Benötigt:**
- [ ] Vereinsname (vollständig)
- [ ] Postanschrift
- [ ] ZVR-Nummer (Vereinsregister)
- [ ] Verantwortlicher für den Inhalt (lt. MedienG)
- [ ] Kontaktdaten (E-Mail reicht)

### Datenschutzerklärung (RECHTLICH ERFORDERLICH!)
**Optionen:**
1. Generator verwenden (z.B. https://www.datenschutzerklärung-generator.de/)
2. Muster von Vereinswebseiten adaptieren

**Muss enthalten:**
- Verantwortlicher
- Hosting-Informationen
- Kontaktformular-Datenverarbeitung
- Cookies (falls verwendet)
- Google Maps (wenn eingebunden)
- Betroffenenrechte

---

## 🔧 TECHNISCHE INHALTE

### Domain & Hosting
| Item | Status | Info |
|------|--------|------|
| Domain registriert | ❌ FEHLEND | Empfohlen: surudmanns.at |
| SSL-Zertifikat | ❌ FEHLEND | Bei IONOS meist inkludiert |
| SFTP-Zugangsdaten | ⚠️ PRÜFEN | Für Deploy-Script |

### E-Mail-Einstellungen (für Formulare)
**Aktuell:** florian.blauen@gmail.com als Empfänger  
**Optional:** Vereins-E-Mail einrichten (z.B. kontakt@surudmanns.at)

### Social Media Links
| Plattform | Link | Status |
|-----------|------|--------|
| Instagram | https://instagram.com/su_rudmanns | ⚠️ PRÜFEN |
| Facebook | https://facebook.com/surudmanns | ⚠️ PRÜFEN |

**TODO:**
- [ ] Korrekte Links eintragen
- [ ] Falls keine Social Media existiert: Links entfernen oder Profile anlegen

---

## 📱 ERWEITERTE FEATURES (Phase 2)

### Pfingstturnier
- [ ] Turnier-Logo oder Banner
- [ ] Turnier-Beschreibung
- [ ] Anmeldeformular-Felder definieren
- [ ] Turnier-Reglement (PDF oder Text)

### Fan-Shop
- [ ] Produktfotos
- [ ] Preisliste
- [ ] Größen/Varianten
- [ ] Bestellprozess klären (Mail vs. Zahlung)

### Fotogalerie
- [ ] Kategorien definieren (Spiele, Events, Mannschaft)
- [ ] Fotos sammeln und sortieren

---

## ✅ PRIO-LISTE (Wichtigste zuerst)

### BLOCKING (Muss vor Go-Live)
1. **Impressum** - Rechtlich erforderlich!
2. **Datenschutzerklärung** - Rechtlich erforderlich!
3. **Vereinslogo** - Für Branding wichtig
4. **Domain + SSL** - Technisch erforderlich

### HOCH (MVP-Qualität)
5. Hero-Bilder (mindestens 1 gutes Bild)
6. Trainer/Ansprechpartner-Daten
7. Sponsoren-Logos
8. Echte News-Beiträge (mind. 2-3)

### MITTEL (Optische Verbesserung)
9. Spieler-Bilder (falls nicht alle vorhanden)
10. Weitere Hero-Bilder
11. Vereinsgeschichte

### NIEDRIG (Kann später nachgereicht werden)
12. Fan-Shop-Inhalte
13. Fotogalerie
14. Historische Daten

---

## 📤 ÜBERGABE

Diese Liste kann an folgende Personen übergeben werden:

**Für Bilder & Design:**
- Werbeprofi (A-er) für Logo/Design
- Florian für Spieler-/Mannschaftsfotos

**Für Texte & Inhalte:**
- Vorstand für Impressum/Datenschutz
- Trainer für Team-Informationen
- Florian für News/Beiträge

**Für Technik:**
- Florian für Domain/Hosting

---

*Letzte Aktualisierung: 22.02.2026 durch Jarvis*  
*Diese Datei sollte regelmäßig aktualisiert werden!*
