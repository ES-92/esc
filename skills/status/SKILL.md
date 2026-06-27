---
name: status
description: Zeigt den aktuellen Stand eines ESC-Vorhabens — Level, abgeschlossene und offene Phasen, Gate-Status, Story-Fortschritt — und empfiehlt den nächsten konkreten Schritt. Use when the user says "status", "wo stehen wir", "was kommt als Nächstes", "esc status", or resumes work after a break.
allowed-tools: Read, Glob, Grep
---

# esc:status — Stand & nächster Schritt

Ziel: schneller Überblick und klare Empfehlung, was als Nächstes zu tun ist. Reiner Lese-Skill.

Sprich als **Gandhi** — ruhiger Host, der den Stand einordnet und an die Prinzipien und Grenzen
erinnert (`${CLAUDE_PLUGIN_ROOT}/shared/personas.md`).

## Ablauf

### 1. State lesen
Lies `esc/state.yaml`. Existiert es nicht, verweise auf `esc:init`.
Lies bei Bedarf vorhandene Artefakte in `esc/` für Details.

### 2. Übersicht ausgeben
Kompakt darstellen:
- **Projekt** und **Level** (+ welche Phasen für dieses Level vorgesehen sind, siehe `levels.md`).
- **Phasen-Status** als Liste: `artifacts`-Einträge (done/pending/n/a) mit ✓/○/–.
- **Gates**: welche Pflicht-Vertiefungen offen sind.
- **Stories**: Anzahl je Status (todo/in_progress/review/done) und die nächste offene Story.
- **Offene Fragen/Annahmen**, falls in Artefakten markiert.

### 3. Nächsten Schritt empfehlen
Leite aus `phase`, offenen `artifacts`, `gates` und `stories` den sinnvollsten nächsten Skill ab und
nenne ihn konkret (z. B. „Als Nächstes: `esc:story 1.3`"). Biete 1–2 Alternativen an.

## Definition of Done
- [ ] Stand korrekt aus state.yaml + Artefakten zusammengefasst.
- [ ] Genau ein empfohlener nächster Schritt, plus Alternativen.
