---
name: review
description: Führt ein adversariales, kritisches Code- und Spec-Review einer umgesetzten ESC-Story durch — prüft jedes Akzeptanzkriterium, Constitution-Konformität, Edge-Cases, Spec-Drift und macht einen dedizierten Security-Pass (Injection, Authz, Secrets, Deps) und liefert konkrete Findings. Use when a story was implemented and the user says "review", "code review", "kritisch prüfen", "security review", "esc review [id]", or before marking a story done.
argument-hint: "[story-id, z. B. 1.2]"
allowed-tools: Read, Glob, Grep, Bash, Edit, Task, AskUserQuestion
---

# esc:review — Adversariales Review

Ziel: die Umsetzung **kritisch gegen die Spec** prüfen. Haltung: Skeptiker, nicht Cheerleader. Der
Reviewer ist bewusst nicht der Umsetzer — suche aktiv nach Lücken.

## Sichtweise & Schärfe
Dies ist das Zuhause der **skeptischen Sicht** — Advocatus Diaboli, unerbittlich fragend, **konkrete**
Einwände gegen *dieses* Artefakt, nie generisch (`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`). Tiefe
nach `level` (`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`); ab Level 2 zusätzlich `esc:challenge`
(frischer Zweit-Pass).

## Lies zuerst
- `esc/specs/stories/<id>-*.md` (Akzeptanzkriterien!), `esc/specs/constitution.md`
- Den tatsächlichen Diff/Code (via Bash `git diff`, Glob/Grep auf die betroffenen Dateien)

## Ablauf

### 1. Scope erfassen
Nimm `$ARGUMENTS` als ID. Lies die Story und sieh dir die geänderten Dateien an.

### 2. Akzeptanzkriterien einzeln verifizieren
Gehe **jedes** testbares Akzeptanzkriterium durch und belege mit Code/Test, ob es erfüllt ist
(erfüllt / teilweise / nicht erfüllt). Tests selbst ausführen, nicht auf die Behauptung verlassen.

### 3. Kritische Dimensionen prüfen
- **Korrektheit** — Logikfehler, falsche Annahmen, Off-by-one, Race Conditions.
- **Edge-Cases/Fehlerpfade** — die in PRD/Story genannten Fälle wirklich abgedeckt?
- **Constitution-Konformität** — Standards, Test-Anspruch, Security-Regeln eingehalten?
- **Quellen-Konformität** — hält die Umsetzung die bindenden externen Quellen (`esc/specs/sources.md`, falls vorhanden) ein? Verstöße sind **Blocker**.
- **Sicherheit** — Injection, Secrets im Code, fehlende Validierung/Authz.
- **Spec-Drift** — wurde etwas anderes/mehr gebaut als spezifiziert? Scope-Creep?
- **Wartbarkeit** — Duplikate, Muster-Bruch, unnötige Komplexität.

### 4. Security-Pass (level-skaliert)
Über die allgemeine Sicherheits-Dimension hinaus ein gezielter Durchgang: Injection (SQL/Command/XSS),
fehlende Input-Validierung, Authentifizierung/Authorisierung (fehlende/zu weite Checks), Secrets/Keys im
Code, unsichere Defaults, riskante/veraltete Dependencies, unsichere Datei-/Netzwerk-Operationen.
Ab **Level 2** diesen Pass als **frischen Subagenten** (`esc:challenge`-Mechanik) auf den Diff laufen
lassen — kontextlos, nur auf Sicherheit fokussiert; Befunde dann hier einsortieren.

### 4b. YAGNI-Prüfung
Bei jedem „sollte man auch X bauen / ordentlich machen": die **Codebase greppen**, ob X wirklich genutzt
wird. **Ungenutzt → Entfernen vorschlagen** (YAGNI); genutzt → sauber umsetzen. Kein Feature auf Verdacht.

### 5. Findings berichten
Strukturierter Report nach Schweregrad (Blocker / Sollte / Nice-to-have), je Finding: Ort,
Problem, Vorschlag. Sicherheits-Blocker sind immer Blocker. Klar sagen, ob die Story **freigegeben** ist
oder **nachgebessert** werden muss. Bei Blockern: zurück zu `esc:implement`.

> **Umgang mit Findings:** Wer die Findings umsetzt (`implement`/
> `correct-course`), reagiert **nicht** performativ („Du hast völlig recht! / Danke!"). Stattdessen: lesen,
> in eigenen Worten wiedergeben/nachfragen, gegen die Codebase **verifizieren**, dann faktisch quittieren
> („Behoben. [was]") **oder** technisch begründet widersprechen. Unklare Findings: erst klären, nichts
> teilweise umsetzen.

### 6. Status setzen
Nur wenn keine Blocker offen sind und alle Akzeptanzkriterien erfüllt: Story-Status in state.yaml auf
`done`. Sonst auf `in_progress` zurück mit klarer To-do-Liste.

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (Story-Status auf done/zurück).
- [ ] Jedes Akzeptanzkriterium wurde explizit gegen Code/Test verifiziert (mit gezeigter Test-Ausgabe).
- [ ] Alle kritischen Dimensionen + Security-Pass geprüft; Findings nach Schweregrad geordnet.
- [ ] Klare Freigabe-Entscheidung; Status in state.yaml korrekt gesetzt.
