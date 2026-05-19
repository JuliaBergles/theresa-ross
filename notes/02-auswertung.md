# Phase 2 — Auswertungs-Logik und Cluster-Texte

> Zur Freigabe durch Theresa. Alle vier Ergebnis-Texte sind bereits im Code implementiert.

---

## Scoring-System

### Punktevergabe

Jede Antwort ergibt 0-3 Belastungspunkte:

| Punkte | Bedeutung |
|--------|-----------|
| 0 | Unauffällig / stabil |
| 1 | Leichter Hinweis |
| 2 | Klarer Hinweis |
| 3 | Starker Hinweis |

### Fragen mit Punktwert (11 von 18)

| Frage | 0 Punkte | 1 Punkt | 2 Punkte | 3 Punkte |
|-------|----------|---------|----------|----------|
| B1 Diagnosen | keine | 1-2 Diagnosen | 3-4 | 5+ |
| B2 Bauchbeschwerden | selten | monatlich | wöchentlich | täglich |
| B3 Schlaf | gut | Einschlafen schwer | nachts wach | morgens erschöpft |
| B4 Energie | gut | wechselnd | oft müde | meistens erschöpft |
| B5 Anspannung | selten | manchmal | oft | fast immer |
| C1 Stressreaktion | 0-1 Symptome | 2 | 3-4 | 5+ |
| C2 Bisheriges | 0-2 Versuche | 3-4 | 5-6 | 7+ |
| C3 Zur-Ruhe-Kommen | leicht | mal so mal so | schwer | unmöglich |
| C5 Körpergefühl | entspannt | wechselnd | angespannt | blockiert |
| D1 Soziales Netz | unterstützend/eng | neutral | schwierig | distanziert |
| D2 Offene Gespräche | ja jederzeit | jemand | niemand | keiner |
| D3 Natur | täglich | wöchentlich | selten | nie |
| D4 Körperverbindung | sehr | okay | wenig | getrennt |

**Maximale Punktzahl:** 11 x 3 = 33

### Fragen OHNE Punktwert (7 von 18)

- A1 (Alter) — nur Kontext
- A2 (Lebenssituation) — nur Kontext
- A3 (Motivation) — Freitext, Krisen-Check
- C4 (Selbstfürsorge) — Freitext, Krisen-Check
- E1 (Abschlussfrage) — Freitext, Krisen-Check

---

## Cluster-Grenzen

| Cluster | Punkte | Bezeichnung | Erwartete Verteilung |
|---------|--------|-------------|---------------------|
| A | 0-8 | Entspanntes Nervensystem | ~15-20% |
| B | 9-17 | Erste Anzeichen | ~35-40% |
| C | 18-27 | Spürbar belastet | ~30-35% |
| D | 28-33 | Ärztliche Begleitung | ~5-10% |

### Cluster-D-Override

Unabhängig von der Gesamtpunktzahl wird Cluster D ausgelöst wenn ALLE drei zutreffen:
- B3 Schlaf = "morgens erschöpft" (3 Punkte)
- B4 Energie = "meistens erschöpft" (3 Punkte)
- B5 Anspannung = "fast immer" (3 Punkte)

**Warum:** Diese Kombination deutet auf eine Belastung hin, die über Coaching hinausgeht. Selbst wenn andere Bereiche unauffällig sind, verdient diese Konstellation einen ärztlichen Verweis.

### Krisen-Override

Freitext-Felder (A3, C4, E1) werden auf Krisen-Wörter geprüft:
- "nicht mehr leben", "aufgeben", "verschwinden", "kein sinn", "alles vorbei", "will nicht mehr", "will weg", "suizid", "umbringen", "sterben", "tod", "hoffnungslos"

Bei Treffer: sofortige Unterbrechung mit Telefonseelsorge-Verweis (Overlay). Nutzer kann trotzdem fortfahren.

---

## Cluster-Texte (finale Fassung)

### Cluster A — Entspanntes Nervensystem

**Ton:** Bestätigend, warm, kein Verkaufsdruck.

> **Was dein Test zeigt**
>
> Du scheinst gerade in einer relativ stabilen Phase zu sein.
>
> Dein Körper findet seinen Rhythmus. Du hörst auf dich. Vieles davon machst du intuitiv schon gut.
>
> Falls du dich trotzdem weiter mit dem Thema Vagusnerv und Nervensystem beschäftigen möchtest, kannst du dir kostenlos Theresas E-Book holen. Es ist eine schöne Vertiefung — aber nichts, wovon du dich gedrängt fühlen solltest.
>
> **[E-Book kostenlos holen]**
> [Test wiederholen]

---

### Cluster B — Erste Anzeichen

**Ton:** Beobachtend, sanft, E-Book als naheliegende Hilfe.

> **Was dein Test zeigt**
>
> Es gibt ein paar Bereiche, in denen sich dein Körper gerade weniger gehalten anfühlen könnte.
>
> Vielleicht der Bauch. Vielleicht der Schlaf. Vielleicht die innere Ruhe tagsüber.
>
> Das ist kein Alarmsignal. Das sind kleine Hinweise.
>
> Oft helfen schon einfache Veränderungen — Atmung, Pausen, Bewegung in der Natur, gemeinsame Mahlzeiten.
>
> Theresa Ross hat dazu ein E-Book geschrieben, das du dir gerne kostenlos holen kannst. Es geht um die Verbindung zwischen Darm, Nervensystem und Geist.
>
> **[E-Book kostenlos holen]**
> [Test wiederholen]

---

### Cluster C — Spürbar belastet

**Ton:** Klar, anerkennend, E-Book + Coaching als Möglichkeit, ärztlicher Hinweis.

> **Was dein Test zeigt**
>
> Mehrere deiner Antworten passen zu einem Muster, das viele Menschen mit chronischen Beschwerden kennen — der Körper steht unter dauerhafter Anspannung.
>
> Schlaf, Verdauung, Energie, vielleicht auch Stimmung — wirken mitgenommen.
>
> Das ist nicht deine Schuld. Das ist eine nachvollziehbare Reaktion auf das, was du gerade trägst.
>
> Es gibt verschiedene Wege, das zu adressieren. Theresa Ross arbeitet seit Jahren mit der Verbindung von Darm-Hirn-Achse, Vagusnerv und Körper-Geist.
>
> Ihr kostenloses E-Book wäre ein ruhiger erster Schritt. Wenn du tiefer gehen möchtest, ist das Coaching VagusFlow gerade im Herbstspecial.
>
> Wichtig: Bei anhaltenden körperlichen Beschwerden sprich bitte zusätzlich mit deiner Hausärztin.
>
> **[E-Book kostenlos holen]**
> **[Mehr über das Coaching]**
> [Test wiederholen]

---

### Cluster D — Hinweis auf ärztliche Begleitung

**Ton:** Ernst, einfühlsam, KEIN Coaching-Verweis als erste Option.

> **Was dein Test zeigt**
>
> Deine Antworten beschreiben eine sehr starke Belastung.
>
> Erschöpfung in diesem Ausmaß, anhaltende Schmerzen oder das Gefühl, abgeschnitten zu sein, verdienen mehr als einen Online-Test als Antwort.
>
> Mein erster Vorschlag wäre nicht ein E-Book oder ein Coaching.
>
> Mein erster Vorschlag wäre: Sprich mit jemandem, dem du vertraust. Vereinbare einen Termin bei deiner Hausärztin.
>
> Wenn die Gedanken dunkel werden, ist die Telefonseelsorge 24 Stunden erreichbar: 0800 111 0 111 (kostenfrei, anonym).
>
> Wenn du danach trotzdem das E-Book lesen möchtest, ist es weiter da. Aber bitte hol dir zuerst echte Hilfe.
>
> **[Telefonseelsorge anrufen]**
> [Wenn ich trotzdem das E-Book möchte]
> [Test wiederholen]

---

## E-Book-Formular (nach Klick)

Felder:
- Vorname (optional)
- E-Mail (Pflicht)
- Checkbox 1 (Pflicht): "Ich möchte das E-Book per E-Mail erhalten und akzeptiere die Datenschutzerklärung."
- Checkbox 2 (optional): "Ich möchte gelegentlich weitere Tipps von Theresa per E-Mail erhalten."

Unter dem Formular — Werbe-Kennzeichnung:
> Hinweis: Dieses E-Book ist von Theresa Ross. Es führt zu ihrem kostenpflichtigen Coaching-Programm VagusFlow. Du bekommst das E-Book kostenlos und kannst es ohne weitere Verpflichtung lesen.

---

## Visuelle Gestaltung der Ergebnisse

- Kein Score, keine Punktzahl, kein Balkendiagramm
- Nur der Ergebnis-Text in Theresas Schrift und Farben
- Sanfte Hintergrundfarbe (bg-light)
- CTAs als Buttons, nicht aufdringlich
- Cluster D: Telefonseelsorge-Nummer visuell hervorgehoben

---

**Status: Wartet auf Theresas Freigabe der Cluster-Texte.**
Sobald freigegeben → Phase 3 (E-Book-Versand und Datenschutz).
