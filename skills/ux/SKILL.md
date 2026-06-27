---
name: ux
description: Erstellt die UX-Spezifikation von ESC — Informationsarchitektur, Kern-User-Flows, Screen-/Zustandsinventar, Interaktions- und Verhaltensregeln, Edge-/Leerzustände und Barrierefreiheit. Use when the product has a user interface and the user says "UX design", "user flows", "screens spezifizieren", "esc ux", or after a PRD when UI behavior needs defining before architecture.
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# esc:ux — UX-Spezifikation

Ziel: das **Verhalten der Oberfläche** so festlegen, dass die KI sie eindeutig umsetzen kann — Flows,
Zustände, Regeln. Kein Pixel-Design, sondern überprüfbare Verhaltensspezifikation.

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/elicitation.md`, `${CLAUDE_PLUGIN_ROOT}/shared/ears-guide.md`
- `esc/state.yaml`, `esc/prd.md`, `esc/constitution.md`

## Vorbedingung
Nur sinnvoll, wenn das Produkt eine UI hat. Bei reinen Backends/CLIs/Libraries kurz nachfragen und
ggf. überspringen (`artifacts.ux_spec: n/a`).

## Ablauf

### 1. Informationsarchitektur & Screens
Erarbeite per Elicitation das **Screen-/View-Inventar** und ihre Hierarchie (Navigation). Jede
Ansicht mit Zweck und den darauf möglichen Aktionen.

### 2. Kern-User-Flows
Für die 3–5 wichtigsten Aufgaben den Flow Schritt für Schritt: Einstieg → Schritte → Erfolg.
Jeden Flow gegen die PRD-Requirements prüfen (Lücken aufdecken).

### 3. Zustände & Verhaltensregeln (EARS)
Für jede wichtige Ansicht/Komponente die Zustände definieren: **Leer · Lädt · Erfolg · Fehler ·
Keine-Rechte**. Interaktions-/Verhaltensregeln als EARS-Sätze formulieren
(z. B. „WENN das Formular ungültig ist, MUSS der Absende-Button deaktiviert sein.").

### 4. Edge-Cases & Barrierefreiheit
**Edge-Case-Jagd** (Pflicht bei Level 3/4): lange Texte, Fehlerketten, Offline, langsames Netz.
Barrierefreiheit knapp: Tastatur-Navigation, Fokus, Kontrast, Screenreader-Labels — soweit relevant.

### 5. UX-Spec schreiben
`esc/ux-spec.md`: Screen-Inventar & IA · Kern-Flows · Zustände je Ansicht · Verhaltensregeln (EARS) ·
Edge-/Leerzustände · Barrierefreiheit · offene Design-Fragen.
state.yaml: `artifacts.ux_spec: done`, `phase` weiter. Routen zu `esc:architecture`.

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (TRACKER.md) und `esc:docs` (Kern-Flows).
- [ ] Alle Kern-Flows abgedeckt und mit PRD-Requirements rückverknüpft.
- [ ] Für jede wichtige Ansicht sind Leer-/Lade-/Fehler-/Erfolgszustände definiert.
- [ ] Verhaltensregeln sind als testbare EARS-Sätze formuliert.
