---
name: story
description: Bereitet eine einzelne Story von ESC zur Implementierung vor, indem sie zu einer self-contained Story-Datei angereichert wird — mit allem Kontext (relevante Requirements, ADRs, betroffene Dateien, Constitution-Regeln, testbaren Akzeptanzkriterien, Testplan), den ein KI-Agent zur fehlerfreien Umsetzung braucht. Use when the user says "create story", "nächste Story vorbereiten", "Story-Kontext", "esc story [id]" before implementing.
argument-hint: "[story-id, z. B. 1.2]"
allowed-tools: Read, Write, Edit, Glob, Grep
---

# esc:story — Self-contained Story-Kontext aufbauen

Ziel: aus einer Backlog-Story eine **selbst-enthaltene** Story-Datei machen, sodass ein frischer
Agent sie ohne weitere Recherche korrekt umsetzen kann. Das bekämpft Kontextverlust und „falsche
Library / falscher Ort / kaputte Regression".

## Sichtweise & Schärfe
Diese Phase wird aus der **Planungs-Sicht** geführt — vollständiger, abhängigkeits-bewusster
Story-Kontext (`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`). Bei Unklarheiten fragt die **skeptische
Sicht** nach, statt zu raten; Tiefe nach `level` (`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`).

## Lies zuerst
- `esc/state.yaml` (Story-Liste + Reihenfolge), `esc/specs/epics.md`
- `esc/specs/prd.md`/`quick-spec.md`, `esc/specs/architecture/architecture.md`, `esc/specs/architecture/decisions/`, `esc/specs/ux-spec.md`, `esc/specs/constitution.md`
- `esc/specs/sources.md` (bindende externe Quellen, falls vorhanden) — relevante Vorgaben in die Story-Constraints zitieren
- Relevante Codebase-Stellen via Glob/Grep (tatsächliche Dateipfade, bestehende Muster).

## Ablauf

### 1. Story wählen
Nimm `$ARGUMENTS` als Story-ID. Fehlt sie, schlage anhand `state.yaml` die nächste `todo`-Story in
Reihenfolge vor. Status auf `in_progress` setzen.

### 2. Kontext zusammentragen (nur das Relevante — Just-in-Time)
Extrahiere gezielt:
- Die zugehörigen **Requirement-IDs** + die testbare Anforderung aus dem PRD.
- Relevante **ADR-Entscheidungen** und **Constitution-Regeln**, die hier gelten.
- **Konkrete betroffene Dateien/Module** (echte Pfade) und bestehende Muster, an die sich die
 Umsetzung halten soll.
- UX-Verhaltensregeln (falls UI).

### 3. Story-Datei schreiben
`esc/specs/stories/<id>-<slug>.md` mit diesen Abschnitten:
- **Story** — „Als … will ich … damit …".
- **Akzeptanzkriterien** — nummeriert, jedes testbar (festes Satzmuster).
- **Kontext & Constraints** — relevante Requirements, ADRs, Constitution-Regeln (zitiert, nicht nur verlinkt).
- **Betroffene Dateien** — konkrete Pfade + ob neu/ändern, bestehende Muster zum Nachahmen.
- **Testplan** — welche Tests (Unit/Integration/E2E) decken welche Akzeptanzkriterien ab.
- **Out-of-Scope** — was diese Story bewusst NICHT tut.
- **Offene Fragen** — falls etwas unklar ist: hier festhalten und den Nutzer fragen, nicht raten.

### 4. Selbst-Check
Prüfe: Könnte ein Agent **ohne** weitere Dateien diese Story korrekt umsetzen? Wenn nein, fehlenden
Kontext ergänzen. Keine Widersprüche zwischen Akzeptanzkriterien und Constraints.

### 5. Routen
Wenn der Nutzer offene Fragen geklärt hat → `esc:implement <id>`.

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (Story-Status auf in_progress).
- [ ] Story-Datei ist self-contained (Agent braucht nichts weiter zu lesen).
- [ ] Akzeptanzkriterien sind testbar und mit Tests verknüpft.
- [ ] Betroffene Dateien sind mit echten Pfaden benannt.
- [ ] Offene Fragen sind markiert, nicht überspielt.
