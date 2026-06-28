---
name: challenge
description: Führt einen skeptischen Zweit-Pass auf ein fertiges Artefakt (PRD, FR/NFR, Architektur, ADR, Story, UX-Spec) durch — ein frischer Subagent liest es ohne Konversationshistorie gegen und liefert konkrete Befunde, die dann zur Entscheidung präsentiert werden. Use when the user says "challenge", "zerpflück das", "kritisch gegenlesen", "zweite Meinung ohne Bias", "esc challenge [artefakt]", or before finalizing a critical artifact.
argument-hint: "[artefakt-pfad oder name, z. B. prd]"
allowed-tools: Read, Glob, Grep, Task, AskUserQuestion
---

# esc:challenge — Skeptischer Zweit-Pass

Ziel: ein fertiges Artefakt von einem **frischen, kontextlosen Skeptiker** gegenlesen lassen, um
Betriebsblindheit zu durchbrechen. Wer etwas baut, ist nicht der, der es benotet.

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md` (skeptische Sicht), `${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`
- Das zu prüfende Artefakt + `esc/docs/constitution.md`

## Ablauf

### 1. Artefakt bestimmen
Aus `$ARGUMENTS` das Zielartefakt ableiten (`esc/docs/prd.md`, `esc/docs/requirements/functional.md`,
`esc/docs/architecture/architecture.md`, eine ADR, eine Story, `esc/docs/ux-spec.md`). Unklar? Per
Auswahl die vorhandenen Artefakte anbieten.

### 2. Frischen Subagenten beauftragen
Starte über das **Task-Tool** einen Subagenten mit klarer Anweisung:
- Rolle: **kompromissloser Skeptiker (Advocatus Diaboli)**, der dieses Artefakt zu *widerlegen* versucht.
- Input: vollständiger Artefakt-Text + relevante Akzeptanz-/Qualitätskriterien + Constitution-Auszug.
- Auftrag: konkrete Schwächen finden — Lücken, Widersprüche, unbelegte Annahmen, ungeprüfte Edge-Cases,
  Spec-Drift, Verstöße gegen die Constitution. **Pro Befund:** Schweregrad (Blocker/Sollte/Nice),
  Ort, Problem, Vorschlag. Default zu „kritisch": im Zweifel als Schwäche melden, nicht durchwinken.
- Output: strukturierte Befundliste (der Subagent stellt **keine** Rückfragen — das Auswahl-Tool steht
  ihm nicht zur Verfügung).

### 3. Befunde präsentieren (skeptische Sicht)
Spiegele die Befunde im Hauptlauf aus der skeptischen Sicht. Präsentiere sie als Auswahl
(AskUserQuestion, in 4er-Häppchen). Pro Befund entscheidet der Nutzer: **adressieren** (zurück zum
Phasen-Skill) oder **bewusst akzeptieren** (Begründung → `decisions`-Log).

### 4. Ergebnis festhalten
Offene Blocker verhindern den `done`-Status des Artefakts. Akzeptierte Befunde + Begründungen ins
`decisions`-Log. Kurzfazit, ob das Artefakt den Zweit-Pass besteht.

## Definition of Done
- [ ] Frischer Subagent hat das Artefakt ohne Konversationshistorie geprüft.
- [ ] Befunde nach Schweregrad, je mit Ort/Problem/Vorschlag, dem Nutzer zur Entscheidung vorgelegt.
- [ ] Akzeptierte Befunde im Decision-Log; Blocker blockieren den `done`-Status.
