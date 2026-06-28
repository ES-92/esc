# ESC — Elicitation-Protokoll

Dieses Protokoll definiert, **wie** ESC im Terminal mit dem Nutzer interagiert. Alle Phasen-Skills
verwenden es. Ziel: geführte, kritisch hinterfragende Konversation statt Monolog — der Nutzer trifft
Entscheidungen, die KI hält sie fest. Geführt wird jede Phase durch ihre **kritische Sichtweise**
(`viewpoints.md`); die Schärfe richtet sich nach dem **Level** (`intensity.md`). Specs werden dabei
**Abschnitt für Abschnitt** erarbeitet (`coauthoring.md`).

## Goldene Regeln
1. **Immer warten.** Stelle eine Frage (oder eine eng zusammengehörige Gruppe) und **warte auf die
   Antwort des Nutzers, bevor du weitermachst.** Beantworte dich niemals selbst.
2. **Auswahl-first (Pfeil + Leertaste).** Nutze für Entscheidungen das native **`AskUserQuestion`**-Tool,
   damit der Nutzer per Auswahl statt Tippen bestätigt. Eine freie Eingabe ist über die automatische
   „Other"-Option immer möglich.
3. **In 4er-Häppchen chunken.** `AskUserQuestion` erlaubt max. 4 Optionen je Frage und max. 4 Fragen je
   Aufruf. Brauchst du mehr Optionen, biete die 4 relevantesten an plus eine Option **„➕ weitere
   Optionen"** und stelle bei deren Wahl die nächsten 4 in einer Folgerunde. Nie Optionen still weglassen.
4. **Eine Entscheidung pro Schritt.** Lieber kurze, fokussierte Runden als ein Fragebogen.
5. **Defaults vorschlagen.** Leite aus Kontext (Codebase, bisherige Antworten) eine empfohlene Option ab
   und setze sie als erste Option mit Zusatz „(empfohlen)".
6. **Sofort persistieren.** Schreibe jede Antwort unmittelbar in das zugehörige Artefakt bzw. ins
   Decision-Log (`esc/state.yaml`), bevor du die nächste Frage stellst.
7. **Aus der Sichtweise & kritisch.** Stelle Fragen aus der aktiven Sichtweise und nimm Antworten nicht
   unkritisch hin — Widersprüche, fehlende Fälle und unausgesprochene Annahmen aufdecken.

## Frage-Format (Standard)

**Bevorzugt — `AskUserQuestion`** (Auswahl per Pfeil + Leertaste):
- `header`: kurzes Label (≤12 Zeichen), z. B. „Zielgruppe".
- `question`: die Frage aus der aktiven Sichtweise.
- `options`: 2–4 konkrete Optionen, jede mit `label` + kurzer `description` (Konsequenz/Trade-off).
  Erste Option = empfohlener Default.
- `multiSelect: true`, wenn mehrere Antworten zulässig sind.

**Fallback — nummeriertes Markdown-Menü** (nur bei offenem Brainstorming oder wenn Auswahl unpassend):

```
❓ Schritt 2/5 — Zielgruppe   (analytische Sicht)

Wer ist die primäre Zielgruppe?
  1) Endkunden (B2C)   2) Unternehmen (B2B)   3) Interne Teams   4) Entwickler/API
  5) Etwas anderes — beschreibe es

→ Antworte mit Zahl(en) oder eigenem Text. (Empfehlung: 2)
```

- Bei freier Eingabe nachhaken, bis die Antwort konkret genug für eine testbare Spec ist.

## Vertiefungs-Methoden (kritisches Hinterfragen)

Nach jedem fertig erarbeiteten Abschnitt schärft der Skill mit **einer** Methode — angeboten als
Auswahl (4 relevanteste + „➕ weitere"):

- **Pre-Mortem** — „Angenommen es scheitert in 6 Monaten — warum?"; Ursachen rückwärts ableiten.
- **Annahmen-Audit** — alle impliziten Annahmen auflisten und einzeln angreifen *(Pflicht laut `intensity.md`)*.
- **Edge-Case-Jagd** — Grenzfälle, Fehlerpfade, Nebenläufigkeit, leere/maximale Eingaben durchgehen.
- **Stakeholder-Runde** — gleiche Frage aus Sicht verschiedener Rollen (Nutzer, Dev, Business, Support, Security).
- **Red-Team vs. Blue-Team** — eine Seite greift die Spec an, die andere verteidigt.
- **5-mal-Warum** — wiederholt „Warum?" fragen, um zur Wurzel zu kommen.
- **Erste-Prinzipien** — Annahmen entfernen, von Grundwahrheiten neu aufbauen.
- **Tree-of-Thoughts** — mehrere Lösungswege parallel andenken, dann besten wählen.
- **Inversions-Test** — „Was würde das garantiert ruinieren?" und dann das Gegenteil sichern.
- **MoSCoW** — Must/Should/Could/Won't, um Scope zu schärfen.

## Gate-Regel (Pflicht, skaliert nach Level)

An kritischen Gates ist die Vertiefung **nicht optional**. Vorgehen (Details + Staffel: `intensity.md`):
1. Die führende Sichtweise schärft den Abschnitt mit der passenden Methode.
2. Die **skeptische Sichtweise** greift an und formuliert **konkrete** Einwände gegen *dieses* Artefakt
   (Anzahl je Level). Jeder Einwand wird adressiert oder bewusst akzeptiert (Begründung → Decision-Log).
3. Ab Level 1/2 zusätzlich **Annahmen-Audit**; ab Level 2 **skeptischer Zweit-Pass** (`esc:challenge`).
4. Erst wenn alle Einwände/Befunde ausgeräumt oder akzeptiert sind: `gates.<x>: true`.

Gates sind: PRD-Erfolgsmetriken · funktionale Requirements (inkl. Edge-Case-Jagd) · jede Architektur-ADR ·
Story-Akzeptanzkriterien — plus jede Stelle, an der ein Artefakt `done` werden soll.
