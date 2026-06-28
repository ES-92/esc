---
name: prd
description: Erstellt das Product Requirements Document (PRD) von ESC mit funktionalen Requirements in testbarer Form, Zielen, messbaren Erfolgsmetriken und Non-Goals. Bei Level 0/1 erzeugt es stattdessen eine schlanke Quick-Spec. Use when the user has a product brief or idea and wants to define requirements, says "PRD erstellen", "Anforderungen festlegen", "esc prd", "quick spec", or needs testable requirements before architecture.
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# esc:prd — Requirements definieren

Ziel: aus dem Brief/der Idee **testbare Anforderungen** machen, die als Guardrails für die KI-Umsetzung
dienen. Weiterhin **WAS, nicht WIE** — Technologie kommt erst in `esc:architecture`.

## Sichtweise & Schärfe
Diese Phase wird aus der **Fokus-Sicht** geführt — Prioritäten, Metriken, Non-Goals: „Was bauen wir
bewusst nicht?" (`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`). An jedem Gate greift die **skeptische
Sicht** an; Tiefe nach `level` (`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`). Erarbeite Abschnitt für
Abschnitt (`${CLAUDE_PLUGIN_ROOT}/shared/coauthoring.md`).

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/requirements-syntax.md` — testbare Anforderungssyntax (verbindlich für Requirements)
- `${CLAUDE_PLUGIN_ROOT}/shared/elicitation.md`
- `esc/state.yaml`, `esc/docs/constitution.md`, `esc/docs/product-brief.md` (falls vorhanden)

## Routing nach Level (aus state.yaml)
- **Level 0/1 → Quick-Spec.** Erzeuge `esc/docs/quick-spec.md`: Problem · Lösung in 1–3 Sätzen ·
 Akzeptanzkriterien (testbar) · betroffene Dateien/Bereiche · Out-of-Scope. Kurz halten, dann zu
 `esc:epics`/`esc:story` routen. Überspringe die übrigen Schritte.
- **Level 2–4 → volles PRD** (unten).

## Ablauf (volles PRD)

### 1. Kontext sichten
Lies Brief und Constitution. Fasse das Problem in einem Satz zusammen und lass bestätigen.

### 2. Ziele & messbare Erfolgsmetriken — GATE
Erarbeite per Elicitation 3–5 Produktziele und je Ziel **mindestens eine messbare Metrik**
(Zahl + Schwelle + Zeitraum). Vage Metriken zurückweisen und konkretisieren.
**Pflicht-Vertiefung:** mindestens eine Methode (empfohlen Pre-Mortem oder 5-mal-Warum) durchführen,
bevor weitergegangen wird. Danach `gates.prd_metrics: true` in state.yaml.

### 3. Funktionale Requirements (FR) — eigenes Dokument, GATE
Erarbeite die funktionalen Anforderungen **Abschnitt für Abschnitt** (`coauthoring.md`), gruppiert nach
Feature-Bereich. Jede Anforderung MUSS einem festen Satzmuster folgen (`shared/requirements-syntax.md`)
und eine eindeutige ID bekommen (`FR-001` …). Pro Bereich:
1. Happy Path als Ereignis-/Zustands-Anforderungen.
2. **Edge-Case-Jagd** (Pflicht): Fehlerpfade, leere/maximale Eingaben, Nebenläufigkeit, Rechte →
   als `FALLS … DANN`-Anforderungen ergänzen.
Schreibe sie nach `esc/docs/requirements/functional.md`. Nach Abschluss `gates.prd_requirements: true`.

### 4. Nicht-funktionale Anforderungen (NFR) — eigenes Dokument
Erarbeite die NFR nach `esc/docs/requirements/non-functional.md`, gegliedert in: Performance ·
Sicherheit · Datenschutz · Zugänglichkeit · Skalierung · Betrieb. Nur was relevant ist, jeweils mit
**messbarer Schwelle**. Verweise auf die Constitution, statt Regeln zu duplizieren.

### 5. Scope-Grenzen & Annahmen
Non-Goals explizit auflisten (aus Brief übernehmen/schärfen). Offene Annahmen markieren.

### 6. PRD-Überblick schreiben
`esc/docs/prd.md` ist der **Überblick**, der auf die Detail-Dokumente verlinkt: Problem · Ziele &
Metriken · Verweis auf `requirements/functional.md` (FR) und `requirements/non-functional.md` (NFR) ·
Non-Goals · Annahmen & offene Fragen.
state.yaml: `artifacts.prd: done`, Entscheidungen ins Log, `phase` weiter.

### 7. Routen
Vorschlag: `esc:ux` (wenn UI), sonst `esc:architecture` (Level 2 leicht, 3/4 voll), bei Level 2
ohne Architektur direkt `esc:epics`.

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (TRACKER.md) und `esc:docs` (Überblick/Flows).
- [ ] Jede FR ist testbar, eindeutig nummeriert und steht in `requirements/functional.md`.
- [ ] NFR stehen in `requirements/non-functional.md`, jeweils mit messbarer Schwelle.
- [ ] Jedes Ziel hat eine messbare Metrik mit Schwelle.
- [ ] Edge-Cases/Fehlerpfade sind als Requirements erfasst (nicht nur Happy Path).
- [ ] Non-Goals sind explizit.
- [ ] Beide Pflicht-Gates (`prd_metrics`, `prd_requirements`) durchlaufen und in state.yaml gesetzt.
