# Theresa Ross — Website

Statische Website für Theresa Ross (Gesundheitsberaterin für Darmgesundheit & Stressmanagement).

## Domain & Deploy

- **Live:** https://theresa-ross.de
- **Hosting:** GitHub Pages
- **Repo:** https://github.com/JuliaBergles/theresa-ross
- **Deploy:** Push auf `main` → Pages baut automatisch neu (ca. 1–3 Minuten bis live).
- **Custom Domain:** in `CNAME` gepflegt (`theresa-ross.de`).

## Lokal ansehen

```
cd /Users/juliabergles/theresa-ross
python3 -m http.server 8765
```

Dann im Browser: http://localhost:8765

## Struktur

- `index.html` — Startseite (Hero, Drei Wege, Über-mich-Teaser, Angebote, VAGUS FLOW, FAQ, Newsletter)
- `ueber-mich.html` — Über mich (Portrait, Geschichte, Qualifikationen)
- `coaching.html` — VAGUS FLOW Programm-Seite
- `selbsttest.html` — 18-Fragen-Selbsttest
- `privatpersonen.html`, `unternehmen.html` — aktuell in der Nav ausgeblendet
- `impressum.html`, `datenschutz.html` — Rechtliches
- `assets/css/` — `tokens.css`, `base.css`, `components.css` (Design-Tokens getrennt)
- `assets/js/main.js` — Nav-Toggle, FAQ-Accordion, Fade-Ups
- `images/` — alle Fotos (nummeriert 1–22 + `theresa-ueber-mich.jpg`)

## Design-System

- **Fonts:** `var(--font-display)` (Überschriften, Serif-Charakter) + `var(--font-body)` (Fließtext)
- **Farben:** Beige (`#EAE0D5`), Dunkelbraun-Akzent (`#7A4440`)
- **Sektionen:** `.section`, `.section--elevated` (hell erhöht), `.section--dark` (dunkler Block)
- **Buttons:** `.btn--primary`, `.btn--ghost-light`
- **Animation:** Elemente mit `.fade-up` faden beim Scrollen ein

## Konventionen

- Neue Fotos nach `images/` mit sprechendem Namen (nicht als Nummer)
- Bei Text-Änderungen: HTML-Entities beachten (`&`, `–`, geschütztes Leerzeichen `&nbsp;`)
- Starttermin für VAGUS FLOW steht an **drei Stellen** und muss konsistent bleiben:
  - `index.html`: Angebots-Karte + VAGUS-FLOW-Sektion
  - `coaching.html`: Herbstspecial-Block (H2 + Info-Boxen)

## Offene Punkte / To-dos

- Zusätzliche Inhalte aus `iCloud/Theresa Ross Website/` sind noch nicht im Repo (contentplan.html, Workbooks, nervensystem-test, RESET-PDF). Bei Bedarf mergen.
- `privatpersonen.html` und `unternehmen.html` sind in der Nav auskommentiert — Entscheidung offen, ob sie zurückkommen.
- FAQ auf `index.html` verweist auf "Herbstspecial" — bei Terminwechsel mit-anpassen.
