---
name: map
description: Analysiert einen bestehenden Codebase (Brownfield) und erzeugt einen AI-lesbaren Ist-Stand — Stack, Build/Test, Modul-/Ordnerstruktur, Architekturmuster, Datenmodell, Konventionen, Einstiegspunkte, Tech-Debt/Risiken — als esc/specs/codebase-map.md, an den sich die folgenden Phasen binden. Use when working on an existing project and the user says "bestehenden Code analysieren", "brownfield", "codebase mappen", "esc map", or before specs/changes on existing code.
allowed-tools: Read, Glob, Grep, Bash, AskUserQuestion, Write, Edit
---

# esc:map — Bestehenden Code erfassen (Brownfield)

Ziel: den **Ist-Stand** eines bestehenden Projekts so erfassen, dass alle folgenden ESC-Phasen darauf
aufsetzen — statt Greenfield zu raten. Ergebnis ist eine kompakte, faktenbasierte Karte.

## Sichtweise & Schärfe
Aus der **analytischen Sicht** geführt — nur belegen, was im Code wirklich steht
(`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`). Keine Vermutungen als Fakten ausgeben.

## Lies zuerst
- `esc/state.yaml`, `esc/specs/constitution.md` (falls vorhanden)
- Den **Code selbst** via Glob/Grep/Bash — Manifeste, Configs, Einstiegspunkte, Tests.

## Ablauf

### 1. Scope & Tiefe klären
Frag (Auswahl): ganzes Repo oder ein Teilbereich? Tiefe (Überblick vs. gründlich)? Bei Monorepo: welches Paket.

### 2. Fakten sammeln (aus dem Code, nicht raten)
- **Stack & Tooling:** Sprachen, Frameworks, Paketmanager (aus `package.json`/`pyproject.toml`/`go.mod`/… ).
- **Build/Run/Test:** wie startet/testet/lintet man das Projekt (Scripts, Makefile, CI-Konfig).
- **Struktur:** Top-Level-Module/Ordner und ihre Verantwortung; Einstiegspunkte (`main`, Server, Routen).
- **Architekturmuster:** Layering, Patterns, externe Integrationen, Persistenz.
- **Datenmodell:** Kern-Entitäten/Tabellen/Schemas (aus Migrations/Models) — als `erDiagram` skizzieren.
- **Konventionen:** Namens-/Ordner-/Test-Konventionen, Formatter/Linter-Regeln.
- **Risiken/Tech-Debt:** offensichtliche Schwachstellen, fehlende Tests, veraltete Deps, „hier-nicht-anfassen"-Zonen.
Mit `git log`/`git ls-files` ein grobes Aktivitäts-/Größenbild gewinnen.

### 3. Karte schreiben
`esc/specs/codebase-map.md`: Überblick · Stack & Tooling · Build/Run/Test · Struktur (Modul-Tabelle) ·
Architektur (+ Mermaid) · Datenmodell (`erDiagram`) · Konventionen · Risiken/Tech-Debt · offene Fragen.
Unsicheres klar als „unbestätigt" markieren, nicht als Fakt.

### 4. Constitution & Bindung
Biete an, entdeckte **Konventionen** in die Constitution zu übernehmen (z. B. „nutze den vorhandenen
Test-Runner X", „Datenzugriff nur über Layer Y"). Danach `esc:bind` vorschlagen, damit die Karte in der
CLAUDE.md verlinkt ist.

### 5. Routen
state.yaml aktualisieren (Brownfield vermerkt). Schlage den nächsten Schritt vor: bei kleiner Änderung
direkt `esc:prd` (Quick-Spec)/`esc:epics`; bei größerem Vorhaben `esc:discover`/`esc:prd`.

## Definition of Done
- [ ] `esc/specs/codebase-map.md` ist faktenbasiert (aus dem Code belegt), Unsicheres markiert.
- [ ] Build/Run/Test-Wege und Kern-Konventionen sind erfasst.
- [ ] Entdeckte Konventionen in die Constitution übernommen (auf Wunsch); `esc:bind` angeboten.
