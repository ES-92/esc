---
name: docs
description: Pflegt die mitlaufende, lebende Projekt-Dokumentation esc/docs/DOCUMENTATION.md von ESC mit Mermaid-Diagrammen — Systemkontext, Architektur/Komponenten, Datenmodell (erDiagram), Kern-Flows (sequenceDiagram) und Glossar. Use when the user says "doku aktualisieren", "dokumentation", "diagramme", "esc docs", or wird am Ende relevanter Phasen automatisch aufgerufen.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# esc:docs — Lebende Dokumentation pflegen

Ziel: `esc/docs/DOCUMENTATION.md` als immer aktuelle, diagrammgestützte Sicht auf das Produkt führen.
Die Doku wird aus den vorhandenen Artefakten abgeleitet, nicht neu erfunden.

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/tracking.md` — Format & Mermaid-Vorlagen für DOCUMENTATION.md
- Vorhandene Artefakte: `esc/specs/product-brief.md`, `esc/specs/prd.md`, `esc/specs/ux-spec.md`,
 `esc/specs/architecture/architecture.md`, `esc/specs/architecture/decisions/`, `esc/state.yaml`

## Ablauf

### 1. Bestand sichten
Lies `DOCUMENTATION.md` (falls vorhanden) und die Artefakte. Bestimme, welche Abschnitte sich seit
dem letzten Stand geändert haben oder neu befüllbar sind.

### 2. Abschnitte aus Artefakten ableiten/aktualisieren
Pflege je nach vorhandenem Wissen (siehe Zuordnungstabelle in `shared/tracking.md`):
- **Überblick & Vision** — aus Brief/PRD (Problem, Zielgruppe, Kernnutzen).
- **Systemkontext** (`flowchart TB`) — Akteure ↔ System ↔ externe Dienste.
- **Architektur & Komponenten** (`flowchart`) — aus `architecture.md`, mit Verweis auf ADRs.
- **Datenmodell** (`erDiagram`) — Kern-Entitäten & Beziehungen aus der Architektur.
- **Kern-Flows** (`sequenceDiagram`) — die 3–5 wichtigsten Abläufe aus PRD/UX.
- **Glossar** — Fachbegriffe konsistent halten.
- **Verweise** — auf PRD, ADRs, Stories.
Nur Abschnitte schreiben, für die belastbares Wissen existiert; den Rest als „_folgt_" markieren.

### 3. Mermaid-Korrektheit
Bezeichner ohne Umlaute/Sonderzeichen, Labels in `["…"]` dürfen Umlaute enthalten. Diagramme klein
und fokussiert halten. Bei Aktualisierung das ganze betroffene Diagramm neu schreiben.

### 4. Konsistenz-Check
Doku darf den Specs nicht widersprechen. Findest du Widersprüche (z. B. Datenmodell ≠ PRD), den
Nutzer darauf hinweisen statt still zu glätten.

## Definition of Done
- [ ] Alle aus den aktuellen Artefakten ableitbaren Abschnitte sind aktuell.
- [ ] Mindestens Systemkontext + (sofern Architektur existiert) Datenmodell als gültige Mermaid-Diagramme.
- [ ] Keine Widersprüche zu den Specs; offene Stellen als „_folgt_" markiert.
