---
name: track
description: Aktualisiert den mitlaufenden Projekt-Tracker esc/TRACKER.md von ESC aus dem aktuellen Zustand — Pipeline-Fortschritt (Mermaid), Artefakt-/Gate-Status, Story-Board und Decision-Log. Use when the user says "tracker aktualisieren", "fortschritt", "esc track", or wird am Ende jeder Phase automatisch von den anderen Skills aufgerufen.
allowed-tools: Read, Write, Bash
---

# esc:track — Projekt-Tracker aktualisieren

Ziel: `esc/TRACKER.md` mit dem aktuellen Stand aus `esc/state.yaml` neu erzeugen. Schnell, idempotent.

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/tracking.md` — Format & Mermaid-Vorlage für TRACKER.md
- `esc/state.yaml`

## Ablauf

### 1. State prüfen
Existiert `esc/state.yaml` nicht, auf `esc:init` verweisen und stoppen.

### 2. Rendern — zwei Wege
1. **Bevorzugt (deterministisch):** Versuche das Skript:
   ```
   python3 ${CLAUDE_PLUGIN_ROOT}/scripts/render_tracker.py esc
   ```
   Meldet es Erfolg („TRACKER.md geschrieben"), bist du fertig mit dem Rendern.
2. **Fallback (manuell):** Meldet das Skript, dass es übersprungen hat (kein Python/nicht parsebar),
   oder ist es nicht vorhanden, dann erzeuge `esc/TRACKER.md` selbst exakt nach der Vorlage in
   `shared/tracking.md`:
   - Pipeline-Flowchart: jeden Knoten nach `artifacts`-Status stylen (done/active/pending), für das
     Level nicht vorgesehene Phasen als `:::skipped`.
   - Artefakt-, Gate-, Story-Tabellen + Story-Pie aus `state.yaml`.
   - Decision-Log aus dem `decisions`-Array; Risiken/offene Fragen aus den Artefakten.

### 3. Kurz bestätigen
Eine Zeile: was sich seit dem letzten Stand geändert hat (z. B. „PRD abgeschlossen, Phase → ux").

## Definition of Done
- [ ] `esc/TRACKER.md` spiegelt `state.yaml` korrekt (Phase, Artefakte, Gates, Stories, Decisions).
- [ ] Mermaid-Pipeline rendert (gültige Syntax, Knoten korrekt gestylt).
