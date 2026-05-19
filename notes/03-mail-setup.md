# Phase 3 — E-Book-Versand: Mail-Setup-Anleitung für Theresa

> Schritt für Schritt. Kein Technik-Wissen nötig.

---

## Welchen Mail-Dienst?

Drei gute Optionen (alle DSGVO-konform, alle mit EU-Servern):

| Dienst | Kostenlos bis | Empfehlung |
|--------|--------------|------------|
| **Brevo** (ehem. Sendinblue) | 300 Mails/Tag | Beste Wahl wenn du noch keinen Dienst hast |
| **MailerLite** | 1.000 Subscriber | Gut wenn du schon MailerLite nutzt |
| **CleverReach** | 250 Empfänger | Deutsche Firma, komplett DACH |

**Frag Theresa:** Nutzt sie schon einen Mail-Dienst? Falls ja, nehmen wir den. Falls nein: Brevo.

---

## Setup mit Brevo (Empfehlung)

### 1. Account erstellen

1. Geh auf [brevo.com](https://www.brevo.com)
2. Kostenlos registrieren
3. E-Mail bestätigen
4. Im Setup-Wizard: "Ich bin Einzelunternehmer" / "Coaching"

### 2. Liste anlegen

1. Im Menü: **Contacts** → **Lists**
2. **Create a list** → Name: "E-Book Empfänger"
3. Eine zweite Liste: "Newsletter" (für die, die den Newsletter-Opt-In angehakt haben)

### 3. Double-Opt-In einrichten (Pflicht in DE!)

1. **Contacts** → **Forms** → **Create a subscription form**
2. Formular-Typ: **Double opt-in**
3. Bestätigungsmail anpassen:
   - Betreff: "Bitte bestätige deine E-Mail"
   - Text: "Du hast gerade das E-Book angefordert. Bestätige kurz deine E-Mail, damit ich es dir schicken kann."
   - Button: "Ja, bestätigen"
4. Nach Bestätigung → Weiterleitung auf: Danke-Seite (oder zurück zur Website)

### 4. Automation: E-Book automatisch versenden

1. **Automations** → **Create an automation**
2. Trigger: **Contact joins list** → "E-Book Empfänger"
3. Aktion: **Send an email**
4. E-Mail gestalten:
   - Betreff: "Dein E-Book: Darm, Nervensystem und du"
   - Inhalt: Kurzer persönlicher Text von Theresa + Download-Link
   - E-Book als PDF-Link (nicht als Anhang — Brevo hat Größenlimit)
5. **Aktivieren**

### 5. PDF hosten

Das E-Book-PDF muss irgendwo online liegen. Optionen:
- **Google Drive**: PDF hochladen → "Freigeben" → "Jeder mit dem Link" → Link kopieren
- **Dropbox**: PDF hochladen → "Link teilen" → Link kopieren

Diesen Link in die Automation-E-Mail als Button einbauen: "E-Book herunterladen"

### 6. API-Key für die Website (optional, für später)

Wenn die Website den Mail-Dienst direkt ansprechen soll:
1. **Settings** → **SMTP & API** → **API Keys**
2. **Generate a new API key** → Name: "Website"
3. Key sicher speichern

**Aktuell nicht nötig** — die Website loggt die Anfrage nur in der Konsole. Für den Anfang kann Theresa die E-Book-Anfragen manuell bearbeiten oder ein Tally-Formular nutzen.

---

## Alternative: Tally.so (einfacher, kein Mail-Dienst nötig)

Falls Theresa es maximal einfach will:

1. Auf [tally.so](https://tally.so) registrieren (kostenlos, EU-Server)
2. Formular erstellen mit: Vorname, E-Mail, Newsletter-Checkbox
3. **Settings** → **After submission** → Redirect auf Danke-Seite mit Download-Link
4. **Notifications** → Theresa bekommt eine Mail bei jeder Anfrage
5. Im Code der Website: Tally-Formular per iframe einbetten

**Vorteil:** Kein Mail-Dienst nötig, DSGVO-konform, sofort einsatzbereit.
**Nachteil:** Kein automatischer E-Book-Versand, kein Double-Opt-In für Newsletter.

---

## Integration in die Website

### Option A: Tally iframe (sofort umsetzbar)

Im E-Book-Formular-Bereich der selbsttest.html:

```html
<iframe
  data-tally-src="https://tally.so/embed/FORM-ID?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1"
  loading="lazy" width="100%" height="400" frameborder="0"
  title="E-Book anfordern">
</iframe>
<script src="https://tally.so/widgets/embed.js"></script>
```

### Option B: Brevo API (später, wenn Volumen steigt)

```javascript
// In der submit-Funktion:
fetch('https://api.brevo.com/v3/contacts', {
  method: 'POST',
  headers: {
    'api-key': 'DEIN-API-KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: email,
    attributes: { VORNAME: name },
    listIds: [LISTE_ID],
    updateEnabled: true
  })
});
```

**Achtung:** API-Key niemals im Frontend-Code! Entweder:
- Über einen serverlosen Endpunkt (z.B. Netlify Functions)
- Oder Tally als Zwischenlösung nutzen

---

## Empfehlung für den Start

1. **Sofort:** Tally-Formular für E-Book-Anfragen (einfach, DSGVO-konform)
2. **Wenn es läuft:** Brevo oder MailerLite für automatischen Versand + Newsletter
3. **Theresas E-Book** muss als PDF vorliegen und online gehostet sein

---

**Status: Theresa muss entscheiden:**
- [ ] Welchen Mail-Dienst? (Brevo / MailerLite / Tally für den Anfang)
- [ ] E-Book-PDF fertig?
- [ ] Newsletter gewünscht? (wenn ja: Double-Opt-In Pflicht)
