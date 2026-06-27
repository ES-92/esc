---
name: review
description: Führt ein adversariales, kritisches Code- und Spec-Review einer umgesetzten ESC-Story durch — prüft jedes Akzeptanzkriterium, Constitution-Konformität, Edge-Cases, Sicherheit und Spec-Drift und liefert konkrete Findings. Use when a story was implemented and the user says "review", "code review", "kritisch prüfen", "esc review [id]", or before marking a story done.
argument-hint: "[story-id, z. B. 1.2]"
allowed-tools: Read, Glob, Grep, Bash, Edit
---

# esc:review — Adversariales Review

Ziel: die Umsetzung **kritisch gegen die Spec** prüfen. Haltung: Skeptiker, nicht Cheerleader. Der
Reviewer ist bewusst nicht der Umsetzer — suche aktiv nach Lücken.

## Lies zuerst
- `esc/stories/<id>-*.md` (Akzeptanzkriterien!), `esc/constitution.md`
- Den tatsächlichen Diff/Code (via Bash `git diff`, Glob/Grep auf die betroffenen Dateien)

## Ablauf

### 1. Scope erfassen
Nimm `$ARGUMENTS` als ID. Lies die Story und sieh dir die geänderten Dateien an.

### 2. Akzeptanzkriterien einzeln verifizieren
Gehe **jedes** EARS-Akzeptanzkriterium durch und belege mit Code/Test, ob es erfüllt ist
(erfüllt / teilweise / nicht erfüllt). Tests selbst ausführen, nicht auf die Behauptung verlassen.

### 3. Kritische Dimensionen prüfen
- **Korrektheit** — Logikfehler, falsche Annahmen, Off-by-one, Race Conditions.
- **Edge-Cases/Fehlerpfade** — die in PRD/Story genannten Fälle wirklich abgedeckt?
- **Constitution-Konformität** — Standards, Test-Anspruch, Security-Regeln eingehalten?
- **Sicherheit** — Injection, Secrets im Code, fehlende Validierung/Authz.
- **Spec-Drift** — wurde etwas anderes/mehr gebaut als spezifiziert? Scope-Creep?
- **Wartbarkeit** — Duplikate, Muster-Bruch, unnötige Komplexität.

### 4. Findings berichten
Strukturierter Report nach Schweregrad (Blocker / Sollte / Nice-to-have), je Finding: Ort,
Problem, Vorschlag. Klar sagen, ob die Story **freigegeben** ist oder **nachgebessert** werden muss.
Bei Blockern: zurück zu `esc:implement`.

### 5. Status setzen
Nur wenn keine Blocker offen sind und alle Akzeptanzkriterien erfüllt: Story-Status in state.yaml auf
`done`. Sonst auf `in_progress` zurück mit klarer To-do-Liste.

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (Story-Status auf done/zurück).
- [ ] Jedes Akzeptanzkriterium wurde explizit gegen Code/Test verifiziert (mit gezeigter Test-Ausgabe).
- [ ] Alle kritischen Dimensionen geprüft; Findings nach Schweregrad geordnet.
- [ ] Klare Freigabe-Entscheidung; Status in state.yaml korrekt gesetzt.
