---
name: init
description: Startet ein ESC-Vorhaben. Klassifiziert das Projekt scale-adaptiv (Level 0–4), legt den esc/-Workspace mit state.yaml und einer Constitution (Guardrails) an und routet zur passenden nächsten Phase. Use when the user wants to start a new product/feature, says "neues Projekt", "lass uns starten", "esc init", "ich will etwas bauen/spezifizieren", or has an idea but no specs yet.
argument-hint: "[kurze Idee/Projektname]"
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, Bash
---

# esc:init — Vorhaben starten & klassifizieren

Du bist der ESC-Startpunkt. Ziel dieses Schritts: das Vorhaben verstehen, scale-adaptiv
einstufen, den Workspace anlegen und eine Constitution (Guardrails für die KI) erarbeiten. **Noch
kein Brief, kein PRD, kein Code.**

## Sichtweise & Schärfe
Diese Phase wird aus der **Prinzipien-Sicht** geführt — Hüterin der Guardrails/Constitution
(`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`). Die Gate-Schärfe richtet sich nach `level`
(`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`).

## Lies zuerst
Lade und befolge diese Referenzen (im Plugin):
- `${CLAUDE_PLUGIN_ROOT}/shared/principles.md` — Haltung
- `${CLAUDE_PLUGIN_ROOT}/shared/elicitation.md` — Frage-Protokoll (nummerierte Optionen, warten!)
- `${CLAUDE_PLUGIN_ROOT}/shared/levels.md` — Level-Modell 0–4
- `${CLAUDE_PLUGIN_ROOT}/shared/state.md` — state.yaml-Schema

## Ablauf

### 0. Bestehenden Workspace prüfen
Prüfe, ob `esc/state.yaml` im aktuellen Projekt existiert. Falls ja: melde den Stand und schlage
vor, mit `esc:status` fortzufahren statt neu zu initialisieren. Sonst weiter.

### 1. Idee erfassen (kurze Konversation, eine Frage je Schritt)
Nimm `$ARGUMENTS` als Startpunkt. Erarbeite per Elicitation-Protokoll knapp:
1. **Was** soll entstehen? (ein Satz in eigenen Worten zurückspiegeln zur Bestätigung)
2. **Welches Problem / welcher Schmerz** wird gelöst, für **wen**?
3. **Greenfield oder Brownfield?** (neues Projekt vs. Änderung an bestehendem Code — bei Brownfield
  kurz die Codebase scannen: Sprache, Framework, Struktur via Glob/Grep)
4. **Grobe Größe?** Biete die Level-Beschreibungen aus `levels.md` als nummerierte Optionen an.

### 2. Level vorschlagen & bestätigen
Leite aus den Antworten + Heuristiken (Story-Zahl, betroffene Subsysteme, Neuheit, Architektur-Risiko,
Reversibilität) ein **Level 0–4** ab. Zeige deine Begründung und lass den Nutzer bestätigen oder
korrigieren. **Im Zweifel eine Stufe niedriger.**

### 3. Constitution erarbeiten (Guardrails)
Das ist der wichtigste Output dieses Schritts: nicht-verhandelbare Regeln, an die sich jede spätere
KI-Implementierung halten MUSS. Frage gezielt (nummerierte Optionen + Defaults aus Codebase) nach:
- **Sprachen/Stack-Zwänge** (falls schon gesetzt) oder „noch offen".
- **Coding-Standards** (z. B. Formatter, Linter, Namens-/Ordnerkonventionen).
- **Test-Anspruch** (z. B. „jede Story braucht Tests", Coverage-Schwelle, TDD ja/nein).
- **Security/Compliance-Grenzen** (z. B. keine Secrets im Code, DSGVO, Auth-Regeln).
- **Architektur-Leitplanken** (z. B. „boring, stabile Technologie bevorzugen", keine neue DB ohne ADR).
- **Out-of-Scope-Grundsätze** (was generell NICHT gebaut wird).
Halte die Constitution knapp und prüfbar (eine Regel = eine Zeile, im Zweifel als „MUSS"-Satz).
Bei sehr kleinen Vorhaben (Level 0/1) reicht eine Minimal-Constitution (Stack + Test-Regel).

### 4. Workspace schreiben
Lege an (per Bash `mkdir -p esc/specs/requirements esc/specs/architecture/decisions esc/specs/stories`):
- `esc/state.yaml` nach Schema (`level`, `phase: init`→ als Nächstes setzen, `artifacts` je nach Level
 auf `pending`/`n/a`, leeres `decisions`-Array mit ggf. erster Stack-Entscheidung).
- `esc/specs/constitution.md` aus Schritt 3.
Verwende das aktuelle Datum (frage nach oder nutze `date +%F` via Bash) für `created`.

### 5. Tracker & Doku anlegen
Lege die mitlaufenden Dateien initial an (Vorlagen in `${CLAUDE_PLUGIN_ROOT}/shared/tracking.md`):
- `esc/TRACKER.md` — via `esc:track` (Skript oder manuell) auf Basis des frischen `state.yaml`.
- `esc/specs/DOCUMENTATION.md` — Skelett mit Überblick (aus der Idee) und Platzhaltern „_folgt_".

### 6. Routen
Zeige eine kompakte Zusammenfassung (Projekt, Level, welche Phasen vorgesehen sind — Tabelle aus
`levels.md`) und schlage den nächsten Skill vor:
- Level 0/1 → in der Regel direkt `esc:prd` (Quick-Spec) oder `esc:epics`.
- Level 2 → `esc:discover` (optional) → `esc:prd`.
- Level 3/4 → `esc:discover`.
Frage, ob direkt weiter (`[1] ja, weiter mit <Skill>` / `[2] später`).

## Definition of Done
- [ ] `esc/state.yaml` existiert mit korrektem `level` und Phasen-Plan.
- [ ] `esc/specs/constitution.md` existiert und ist prüfbar formuliert.
- [ ] Mindestens die Stack-/Test-Grundregeln sind festgehalten.
- [ ] `esc/TRACKER.md` und `esc/specs/DOCUMENTATION.md` initial angelegt.
- [ ] Nächster Schritt wurde dem Nutzer klar vorgeschlagen.
