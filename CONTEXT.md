# Theresa Ross — Website

Statische Website für Theresa Ross (Gesundheitsberaterin für Darmgesundheit & Stressmanagement).

## Domain & Deploy

- **Live:** https://theresa-ross.de
- **Hosting:** GitHub Pages
- **Repo:** https://github.com/JuliaBergles/theresa-ross
- **Deploy:** Push auf `main` → Pages baut automatisch neu (ca. 1–3 Minuten bis live).
- **Custom Domain:** in `CNAME` gepflegt (`theresa-ross.de`).
- **Nach Deploy:** Cmd+Shift+R (Hard-Refresh), damit Browser-Cache umgangen wird.

## Lokal ansehen

```
cd "/Users/juliabergles/Library/Mobile Documents/com~apple~CloudDocs/Theresa Ross Website"
python3 -m http.server 8765
```

Dann im Browser: http://localhost:8765

## Hauptangebot: VAGUS FLOW

8-wöchiges Coaching-Programm mit persönlicher Begleitung.

- **Start:** 19. September 2026
- **Launch-Preis:** 549 € – **nur im August!** Danach wird der Preis teurer.
- **Plätze limitiert verfügbar** (persönliche Begleitung).
- **Buchungslink:** https://theresa-ross.thrivecart.com/vagus-flow/
- **Button-Wording überall:** "Sei dabei" (nicht mehr "Warteliste")

Alle CTA-Buttons zu VAGUS FLOW verweisen auf den Thrivecart-Buchungslink. Der alte MailerLite-Warteliste-Link (`preview.mailerlite.io/forms/1206562/…`) wird nicht mehr verwendet.

## MailerLite Setup

- **Landing Page (Workbook-Anmeldung):** `https://theresa-ross-gesundheitsberatung-5bceai.mailerpage.io`
- **Aktive Gruppen:**
  - `Newsletter Abonnenten NEU` — Hauptliste
  - `Newsletter Automation` — Welcome-Sequence-Trigger
  - `PDF - 5 neurobiologische Muster` — Freebie-Interessenten
- **Aktive Automation:** `Freebook 5 neurobiologische Muster - VAGUS FLOW` (Trigger: neue Anmeldung, verschickt Workbook-Link per Mail)
- **Absender:** `theresaross-coach@outlook.de` (Free-Domain — Deliverability könnte mit eigener Domain besser sein)

## Weitere Angebote

- **Selbsttest** (`selbsttest.html`) — 18 Fragen, kostenlos, anonym
- **Workbook** (`workbook.html`) — 6 Stationen zur Selbstreflexion
- **E-Book / Workbook "5 Muster"** (`ebook.html`) — 5 neurologische Muster; wird als Lead Magnet über MailerLite ausgeliefert (siehe Workbook-Trichter unten)
- **Newsletter** — 20 vorbereitete Ausgaben (`newsletter/newsletter.html`); Anmeldung läuft ausschließlich über den Workbook-Trichter (keine separate Newsletter-Sektion mehr)

## Workbook-Trichter (Lead Magnet Flow)

Der Newsletter-Einstieg passiert über das kostenlose "5 Muster"-Workbook:

1. **Button "Workbook kostenlos sichern"** auf `index.html` (E-Book-Sektion, `#ebook`) → verlinkt auf MailerLite-Landing-Page
2. **MailerLite-Landing-Page:** `https://theresa-ross-gesundheitsberatung-5bceai.mailerpage.io` (Anmelde-Formular)
3. **Nach Double-Opt-In:** Person landet in MailerLite-Gruppen "Newsletter Abonnenten NEU", "Newsletter Automation" und "PDF - 5 neurobiologische Muster"
4. **Automation "Freebook 5 neurobiologische Muster - VAGUS FLOW"** feuert → Mail mit Workbook-Link (`https://theresa-ross.de/ebook.html`) wird verschickt

Deshalb: eine separate Newsletter-Anmelde-Sektion auf `index.html` gibt es nicht mehr — alle neuen Newsletter-Abonnenten kommen über das Workbook rein.

## Struktur

- `index.html` — Startseite (Hero, Drei Wege, Über-mich-Teaser, Angebote, VAGUS FLOW, FAQ, E-Book/Workbook-Trichter, Über-mich). E-Book-Button verlinkt auf MailerLite-Landing-Page.
- `ueber-mich.html` — Über mich (Portrait, Geschichte, Qualifikationen)
- `coaching.html` — VAGUS FLOW Programm-Seite (Preisbereich + neue "Stimmen"-Sektion mit Teilnehmerinnen-Feedback zwischen Ablauf und Herbstspecial)
- `selbsttest.html` — 18-Fragen-Selbsttest
- `workbook.html`, `ebook.html` — Freebies mit CTA zu VAGUS FLOW (technisch weiter direkt erreichbar; primärer Weg zu `ebook.html` läuft über den MailerLite-Trichter)
- `privatpersonen.html`, `unternehmen.html` — aktuell in der Nav ausgeblendet
- `contentplan.html` — interne Übersicht der 26 Instagram-Karussell-Posts
- `newsletter/newsletter.html` — 20 Newsletter-Ausgaben (gestylt)
- `impressum.html`, `datenschutz.html` — Rechtliches
- `assets/css/` — `tokens.css`, `base.css`, `components.css` (Design-Tokens getrennt)
- `assets/js/main.js` — Nav-Toggle, FAQ-Accordion, Fade-Ups
- `images/` — alle Fotos (nummeriert 1–22 + `theresa-ueber-mich.jpg`, `feedback-vagusflow-01.jpg`)

## Navigation (aktuell sichtbar)

VAGUS FLOW · Über mich · Selbsttest
(Privatpersonen, Unternehmen, Rabattcodes sind ausgeblendet.)

## Design-System

- **Fonts:** `var(--font-display)` (Überschriften, Serif-Charakter) + `var(--font-body)` (Fließtext)
- **Farben:** Beige (`#EAE0D5`), Dunkelbraun-Akzent (`#7A4440`)
- **Sektionen:** `.section`, `.section--elevated` (hell erhöht), `.section--dark` (dunkler Block)
- **Buttons:** `.btn--primary`, `.btn--ghost-light`
- **Animation:** Elemente mit `.fade-up` faden beim Scrollen ein

Details in:
- `content/branding/visual_dna.md` — Design-Grundlagen
- `content/branding/design_standards.md` — Design-Regeln
- `content/branding/tonality_examples.md` — Sprache (warm, ruhig, klar; per "du")

## Content-Plan

`content/contentplan/contentplan.md` — 13 Wochen / 26 Karussell-Posts für Instagram, inkl. CTA-Verteilung und Saisonalität. Interne HTML-Übersicht: `contentplan.html`.

## Konventionen

- Neue Fotos nach `images/` mit sprechendem Namen (nicht als Nummer)
- Bei Text-Änderungen: HTML-Entities beachten (`&amp;`, `&ndash;`, geschütztes Leerzeichen `&nbsp;`)
- Preis- und Termin-Angaben zu VAGUS FLOW an **mehreren Stellen** konsistent halten:
  - `coaching.html` (Preisbereich + Schema.org-Snippet)
  - `index.html` (VAGUS FLOW-Sektion)
  - `privatpersonen.html` (Herbst-Special-Sektion)
  - `newsletter/newsletter.html` (mehrere Ausgaben)

## Kontakt

theresaross-coach@outlook.de

## Arbeitsregeln

Siehe `/Users/juliabergles/CLAUDE.md`:
- Sauber und strukturiert arbeiten, keine Quick-and-Dirty-Lösungen
- Bestehenden Code erst verstehen, bevor geändert wird
- Gute UX mitdenken
- Bei Unklarheiten nachfragen statt raten
