---
name: epics
description: Zerlegt die Anforderungen von ESC in Epics und vertikal geschnittene User Stories mit testbaren Akzeptanzkriterien und führt ein Readiness-Gate (PRD/UX/Architektur vollständig?) durch. Use when PRD/architecture exist and the user says "Epics und Stories erstellen", "Backlog", "Stories schneiden", "esc epics", or wants to plan implementation work.
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# esc:epics — Epics & Stories + Readiness-Gate

Ziel: die Spec in umsetzbare, unabhängig testbare **Stories** schneiden, jede mit **testbaren Akzeptanz-
kriterien** und Rückverweis auf die Requirements. Vorher prüfen, ob die Specs überhaupt
implementierungsreif sind.

## Sichtweise & Schärfe
Diese Phase wird aus der **Planungs-Sicht** geführt — Slicing & Abhängigkeiten: „Ist das wirklich
vertikal und unabhängig?" (`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`). Am Akzeptanz-Gate greift die
**skeptische Sicht** an; Tiefe nach `level` (`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`). Erarbeite
Abschnitt für Abschnitt (`${CLAUDE_PLUGIN_ROOT}/shared/coauthoring.md`).

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/requirements-syntax.md`, `${CLAUDE_PLUGIN_ROOT}/shared/elicitation.md`
- `esc/state.yaml`, `esc/specs/prd.md`/`quick-spec.md`, `esc/specs/architecture/architecture.md`, `esc/specs/ux-spec.md`, `esc/specs/constitution.md`

## Ablauf

### 1. Readiness-Gate
Prüfe die vorgelagerten Artefakte gegen das Level (siehe `levels.md`). Checkliste:
- PRD/Quick-Spec vorhanden; Requirements testbar; Non-Goals gesetzt.
- (Level 3/4) Architektur + ADRs vorhanden; Datenmodell/Schnittstellen geklärt.
- (UI) UX-Spec mit Zuständen vorhanden.
- Keine offenen Blocker-Annahmen.
Bei Lücken: konkret benennen und vorschlagen, zum betreffenden Skill zurückzukehren. **Nicht** mit
unreifen Specs Stories erzwingen.

### 2. Epics bilden
Gruppiere die Requirements zu kohärenten **Epics** (Wert-Einheiten). Jedes Epic: Ziel, enthaltene
Requirement-IDs, grobe Reihenfolge/Abhängigkeit.

### 3. Stories schneiden
Pro Epic vertikale, **unabhängig auslieferbare** Stories. Je Story:
- Titel + ID (`<epic>.<nr>`), kurze Nutzer-orientierte Beschreibung („Als … will ich … damit …").
- **testbare Akzeptanzkriterien** (jedes 1:1 testbar, mit Requirement-Rückverweis).
- Abhängigkeiten, betroffene Komponenten/Dateien (grob).
- Schätzung der Größe (S/M/L) — zu große Stories aufteilen.
Achte auf INVEST (independent, negotiable, valuable, estimable, small, testable).

### 4. Akzeptanzkriterien-Gate
Stelle sicher, dass **jede** Story testbare testbare Kriterien hat. Für risikoreiche Stories eine
**Edge-Case-Jagd** durchführen. Danach `gates.story_acceptance: true`.

### 5. Schreiben
`esc/specs/epics.md` (Epics + Story-Übersicht in Reihenfolge). Lege je Story einen Eintrag in
`esc/state.yaml` unter `stories` an (`id`, `title`, `status: todo`). Optional pro Story bereits eine
Datei-Stub in `esc/specs/stories/` — die volle Kontextanreicherung macht `esc:story`.
state.yaml: `artifacts.epics: done`, `phase: deliver`.

### 6. Routen
Schlage `esc:story <id>` (für die erste Story) bzw. `esc:status` für die Reihenfolge vor.

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (Story-Board) und `esc:docs` (Verweise).
- [ ] Readiness-Gate bestanden oder Lücken klar an den Nutzer zurückgespielt.
- [ ] Jede Story ist vertikal, INVEST-tauglich und hat testbaren Akzeptanzkriterien mit Requirement-Bezug.
- [ ] Stories in state.yaml registriert; `gates.story_acceptance: true`.
