# SU-Vereinswebsite - Projektdokumentation

## Projektübersicht

**Projektname:** SU-Vereinswebsite  
**Kunde:** Sportunion Rudmanns  
**Projektstart:** 22.02.2026  
**Status:** 🟡 Anforderungsphase  
**Priorität:** 🔴 Hoch

---

## 1. Zielsetzung / Aufgabenstellung

### Primäres Ziel
Entwicklung einer modernen, professionellen Website für den Hobby-Liga-Fußballverein **Sportunion Rudmanns**.

### Ziele
- **Informationsplattform:** Aktuelle News, Spielpläne und Ergebnisse für Mitglieder und Fans
- **Repräsentation:** Professioneller Webauftritt des Vereins
- **Kommunikation:** Zentrale Anlaufstelle für Anfragen und Informationen
- **Mitgliedergewinnung:** Präsentation des Vereins für potenzielle neue Mitglieder

### Erfolgskriterien
- [ ] Responsive Design (Mobile & Desktop)
- [ ] Einfache Pflege durch Vereinsverantwortliche
- [ ] Klare Struktur und Navigation
- [ ] Professionelles Erscheinungsbild

---

## 2. Ausgangssituation

### Ist-Zustand
- Aktuell keine Website vorhanden (oder veraltete Präsenz)
- Kommunikation läuft über Social Media oder WhatsApp
- Informationen sind verteilt und nicht zentralisiert

### Stakeholder
| Name / Gruppe | Rolle | Kontakt | Verantwortlichkeit |
|---------------|-------|---------|-------------------|
| Sportunion Rudmanns | Auftraggeber | sportunionrudmanns@gmail.com | Inhalte, Freigaben |
| Alexander | Werbeprofi | alexander@werbeprofi.at | Design-Beratung |
| Jonathan | Unterstützung | jonathan.bobleter@gmail.com | Koordination |
| Florian Blauensteiner | Projektleiter / Developer | florian@blauensteiner.io | Umsetzung |

### Technische Rahmenbedingungen
- **Hosting:** SFTP-Webspace (IONOS/1&1)
- **Domain:** Noch zu definieren (empfohlen: surudmanns.at)
- **Technologie:** HTML, CSS, JavaScript (statische Website)
- **Deployment:** Automatisch via Python-Script

---

## 3. Scope (Projektumfang)

### In Scope (Geplant)
- Startseite mit News/Updates
- Mannschaftsübersicht
- Spielplan & Ergebnisse (optional: automatische Integration)
- Vorstand/Ansprechpartner
- Trainingszeiten
- Kontakt/Impressum
- Responsive Design
- Social Media Integration

### Optional (Wenn gewünscht)
- Mitgliederbereich (geschützter Bereich)
- Fotogalerie
- Sponsoren-Präsentation
- Fan-Shop/Merchandise
- Historie/Vereinsgeschichte

### Out of Scope (Nicht enthalten)
- Komplexe Backend-Entwicklung (PHP, Datenbank)
- Benutzer-Login-System (außer explizit gewünscht)
- E-Commerce mit Zahlungsintegration

---

## 4. Anforderungen

### Funktionale Anforderungen
Basierend auf dem Fragebogen (ausstehend):
- [ ] Design-Vorgaben (Farben, Logo)
- [ ] Module definieren (News, Mannschaften, etc.)
- [ ] Inhalte/Pflege klären

### Nicht-funktionale Anforderungen
- **Performance:** Ladezeit < 2 Sekunden
- **SEO:** Grundlegende Suchmaschinenoptimierung
- **Barrierefreiheit:** WCAG 2.1 Level AA (wo möglich)
- **Datenschutz:** DSGVO-konform (Impressum, Datenschutz)

---

## 5. Zeitplan & Meilensteine

| Phase | Zeitraum | Status | Deliverable |
|-------|----------|--------|-------------|
| **Initiierung** | 22.02.2026 | 🟢 Abgeschlossen | Projektsetup, Repository |
| **Anforderung** | 22.02. - offen | 🟡 Aktiv | Fragebogen ausgefüllt |
| **Konzeption** | TBD | 🔴 Geplant | User Stories, Design-Vorschlag |
| **Entwicklung** | TBD | 🔴 Geplant | Implementation |
| **Testing** | TBD | 🔴 Geplant | QA, Content-Einpflege |
| **Go-Live** | TBD | 🔴 Geplant | Deployment |

**Deadline:** Noch zu definieren (abhängig von Vereins-Terminplan)

---

## 6. Risiken & Abhängigkeiten

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Verzögerte Rückmeldung vom Verein | Mittel | Hoch | Frühes Versenden, Follow-up |
| Unklare Design-Vorgaben | Mittel | Mittel | Referenz-Websites zeigen |
| Fehlende Inhalte (Texte, Fotos) | Hoch | Mittel | Redaktionelles Briefing |
| Technische Einschränkungen Hosting | Niedrig | Mittel | Frühzeitige Klärung |

---

## 7. Kommunikation & Reporting

### Status-Updates
- **Wöchentlich:** Kurzes Update an Florian (Text)
- **Bei Meilensteinen:** Detaillierter Report
- **Bei Blockern:** Sofortige Eskalation

### Dokumentation
- **GitHub:** Code, Issues, Project Board
- **Portfolio:** PORTFOLIO.md (Master-Übersicht)
- **Projekt:** Diese PROJECT.md

---

## 8. Links & Ressourcen

### Repository & Tools
- **GitHub Repo:** https://github.com/BlauensteinerFlorian/SU-Vereinswebsite
- **GitHub Project:** [SU Website Project](https://github.com/BlauensteinerFlorian/SU-Vereinswebsite/projects)
- **Fragebogen:** `Fragebogen Anforderungen SU Website.csv`

### Deployment
- **Ziel-Server:** SFTP (Zugangsdaten in `.env`)
- **Deploy-Script:** `scripts/deploy.py`

### Referenzen
- **Ähnliche Projekte:** Sportunion-Websites (zur Inspiration)

---

## Änderungshistorie

| Datum | Version | Änderung | Autor |
|-------|---------|----------|-------|
| 22.02.2026 | 1.0 | Initiale Dokumentation | Jarvis |

---

*Diese Dokumentation wird laufend aktualisiert.*
