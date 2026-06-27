---
name: prd
description: Erstellt das Product Requirements Document (PRD) von ESC mit funktionalen Requirements in EARS-Notation, Zielen, messbaren Erfolgsmetriken und Non-Goals. Bei Level 0/1 erzeugt es stattdessen eine schlanke Quick-Spec. Use when the user has a product brief or idea and wants to define requirements, says "PRD erstellen", "Anforderungen festlegen", "esc prd", "quick spec", or needs testable requirements before architecture.
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# esc:prd — Requirements definieren (EARS)

Ziel: aus dem Brief/der Idee **testbare Anforderungen** machen, die als Guardrails für die KI-Umsetzung
dienen. Weiterhin **WAS, nicht WIE** — Technologie kommt erst in `esc:architecture`.

## Persona & Schärfe
Du führst diese Phase als **Jobs (Steve Jobs)** — radikaler Fokus: „Entscheiden, was man *nicht* baut,
ist genauso wichtig." Sprich in seiner Stimme und fordere Klarheit, Metriken und Non-Goals ein
(`${CLAUDE_PLUGIN_ROOT}/shared/personas.md`). An jedem Gate tritt **Sokrates** auf; Tiefe nach `level`
(`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`).

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/ears-guide.md` — EARS-Notation (verbindlich für Requirements)
- `${CLAUDE_PLUGIN_ROOT}/shared/elicitation.md`
- `esc/state.yaml`, `esc/constitution.md`, `esc/product-brief.md` (falls vorhanden)

## Routing nach Level (aus state.yaml)
- **Level 0/1 → Quick-Spec.** Erzeuge `esc/quick-spec.md`: Problem · Lösung in 1–3 Sätzen ·
  Akzeptanzkriterien (EARS) · betroffene Dateien/Bereiche · Out-of-Scope. Kurz halten, dann zu
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

### 3. Funktionale Requirements in EARS — GATE
Arbeite die Anforderungen kapitelweise (nach Feature-Bereich) heraus. Jede Anforderung MUSS einem
EARS-Muster folgen (`shared/ears-guide.md`) und eine eindeutige ID bekommen (`FR-001` …).
Für jeden Bereich:
1. Happy Path als Ereignis-/Zustands-Requirements.
2. **Edge-Case-Jagd** (Pflicht): Fehlerpfade, leere/maximale Eingaben, Nebenläufigkeit, Rechte →
   als `FALLS … DANN`-Requirements ergänzen.
Nach Abschluss `gates.prd_requirements: true`.

### 4. Nicht-funktionale Anforderungen
Knapp: Performance, Sicherheit, Datenschutz, Zugänglichkeit, Skalierung — nur was relevant ist,
jeweils mit Schwelle. Verweise auf Constitution, statt Regeln zu duplizieren.

### 5. Scope-Grenzen & Annahmen
Non-Goals explizit auflisten (aus Brief übernehmen/schärfen). Offene Annahmen markieren.

### 6. PRD schreiben
`esc/prd.md` mit: Überblick/Problem · Ziele & Metriken · Funktionale Requirements (EARS, nummeriert,
nach Bereich gruppiert) · Nicht-funktionale Anforderungen · Non-Goals · Annahmen & offene Fragen.
state.yaml: `artifacts.prd: done`, Entscheidungen ins Log, `phase` weiter.

### 7. Routen
Vorschlag: `esc:ux` (wenn UI), sonst `esc:architecture` (Level 2 leicht, 3/4 voll), bei Level 2
ohne Architektur direkt `esc:epics`.

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (TRACKER.md) und `esc:docs` (Überblick/Flows).
- [ ] Jede funktionale Anforderung ist EARS-konform, nummeriert und testbar.
- [ ] Jedes Ziel hat eine messbare Metrik mit Schwelle.
- [ ] Edge-Cases/Fehlerpfade sind als Requirements erfasst (nicht nur Happy Path).
- [ ] Non-Goals sind explizit.
- [ ] Beide Pflicht-Gates (`prd_metrics`, `prd_requirements`) durchlaufen und in state.yaml gesetzt.
