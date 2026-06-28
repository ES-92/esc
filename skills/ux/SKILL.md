---
name: ux
description: Erstellt die UX-Spezifikation von ESC — Informationsarchitektur, Kern-User-Flows, Screen-/Zustandsinventar, Interaktions- und Verhaltensregeln, Edge-/Leerzustände und Barrierefreiheit. Bietet optional einen intensiveren, visuellen Modus mit HTML/CSS/JS-Mockup-Varianten (3–4 zur Auswahl) und Live-Browser-Preview. Use when the product has a user interface and the user says "UX design", "user flows", "screens spezifizieren", "mockups", "esc ux", or after a PRD when UI behavior needs defining before architecture.
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, Bash
---

# esc:ux — UX-Spezifikation

Ziel: das **Verhalten der Oberfläche** so festlegen, dass die KI sie eindeutig umsetzen kann — Flows,
Zustände, Regeln. Kein Pixel-Design, sondern überprüfbare Verhaltensspezifikation.

## Sichtweise & Schärfe
Diese Phase wird aus der **Nutzer-Sicht** geführt — Erlebnis & Fehlerpfade: „Wie fühlt sich der
schlechteste Moment an?" (`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`). An jedem Gate greift die
**skeptische Sicht** an; Tiefe nach `level` (`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`). Erarbeite
Abschnitt für Abschnitt (`${CLAUDE_PLUGIN_ROOT}/shared/coauthoring.md`).

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/elicitation.md`, `${CLAUDE_PLUGIN_ROOT}/shared/requirements-syntax.md`
- `esc/state.yaml`, `esc/specs/prd.md`, `esc/specs/constitution.md`

## Vorbedingung
Nur sinnvoll, wenn das Produkt eine UI hat. Bei reinen Backends/CLIs/Libraries kurz nachfragen und
ggf. überspringen (`artifacts.ux_spec: n/a`).

## Ablauf

### 1. Informationsarchitektur & Screens
Erarbeite per Elicitation das **Screen-/View-Inventar** und ihre Hierarchie (Navigation). Jede
Ansicht mit Zweck und den darauf möglichen Aktionen.

### 2. Modus wählen: textbasiert oder visuell (Mockups)?
Frage den Nutzer (Auswahl):
- **Standard (textbasiert)** — Flows/Zustände/Regeln direkt als Spec. Schnell, token-sparsam.
- **Visuell intensiv (Mockups + Live-Preview)** — pro Schlüssel-Screen 3–4 HTML/CSS/JS-Varianten zum
  Auswählen, im Browser. Mächtiger, aber **token-intensiver**.
Bei „visuell intensiv": nach `${CLAUDE_PLUGIN_ROOT}/shared/mockups.md` vorgehen (Schlüssel-Screens zuerst,
Fidelity-Modus erfragen, Varianten in `esc/docs/mockups/`, Server mit Port-Frage, auswählen, gewählte →
Spec destillieren, Rest archivieren). Die gewählten Mockups speisen die folgenden Schritte.

### 3. Kern-User-Flows
Für die 3–5 wichtigsten Aufgaben den Flow Schritt für Schritt: Einstieg → Schritte → Erfolg.
Jeden Flow gegen die PRD-Requirements prüfen (Lücken aufdecken).

### 4. Zustände & Verhaltensregeln
Für jede wichtige Ansicht/Komponente die Zustände definieren: **Leer · Lädt · Erfolg · Fehler ·
Keine-Rechte**. Interaktions-/Verhaltensregeln als testbare Sätze formulieren
(z. B. „WENN das Formular ungültig ist, MUSS der Absende-Button deaktiviert sein.").

### 5. Edge-Cases & Barrierefreiheit
**Edge-Case-Jagd** (Pflicht bei Level 3/4): lange Texte, Fehlerketten, Offline, langsames Netz.
Barrierefreiheit knapp: Tastatur-Navigation, Fokus, Kontrast, Screenreader-Labels — soweit relevant.

### 6. UX-Spec schreiben
`esc/specs/ux-spec.md`: Screen-Inventar & IA · Kern-Flows · Zustände je Ansicht · Verhaltensregeln (testbar) ·
Edge-/Leerzustände · Barrierefreiheit · offene Design-Fragen. Bei visuellem Modus: Verweis auf die
gewählten Mockups (als visuelle Referenz, kein bindender Code).
state.yaml: `artifacts.ux_spec: done`, `phase` weiter. Routen zu `esc:architecture`.

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (TRACKER.md) und `esc:docs` (Kern-Flows).
- [ ] Alle Kern-Flows abgedeckt und mit PRD-Requirements rückverknüpft.
- [ ] Für jede wichtige Ansicht sind Leer-/Lade-/Fehler-/Erfolgszustände definiert.
- [ ] Verhaltensregeln sind als testbare Sätze formuliert.
- [ ] Visueller Modus (falls gewählt): gewählte Variante in die Spec destilliert, Rest archiviert; `ux-spec.md` ist auch ohne Mockups vollständig.
