---
name: implement
description: Implementiert eine vorbereitete ESC-Story strikt nach ihrer Story-Datei — testgetrieben, im Rahmen von Constitution und Akzeptanzkriterien — und aktualisiert den Status. Use when a story file is ready and the user says "implement", "Story umsetzen", "dev story", "esc implement [id]", or wants to build the code for a prepared story.
argument-hint: "[story-id, z. B. 1.2]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
disable-model-invocation: true
---

# esc:implement — Story umsetzen

Ziel: die Story **genau nach Spec** bauen. Die Story-Datei ist die Single Source of Truth. Nicht
improvisieren, nicht den Scope erweitern, nicht über Tests lügen.

## Sichtweise & Schärfe
Diese Phase wird aus der **pragmatischen Sicht** geführt — funktionierender, getesteter Code: „Läuft
es? Beweise es mit grünen Tests." Keine Abkürzung, kein Scope-Creep
(`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`, `${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`).

## Lies zuerst
- `esc/specs/stories/<id>-*.md` (maßgeblich), `esc/specs/constitution.md`
- Bei Lücken/Widersprüchen in der Story: **stoppen** und `esc:story` bzw. den Nutzer einschalten,
 nicht raten.

## Ablauf

### 0. Isolierter Workspace (optional, Git-Worktree)
Biete an, die Story in einem **isolierten Git-Worktree** umzusetzen (main bleibt sauber). Vorgehen:
**Isolation erst erkennen** (schon in einem Worktree? Submodul?), dann **native Worktree-Tools bevorzugen**;
sonst `git worktree add` in ein **ignoriertes** Verzeichnis (`.worktrees/`, vorher `git check-ignore`).
Baseline-Tests vor Start laufen lassen. Nur mit Nutzer-Zustimmung; niemals auf `main` ohne Einverständnis.

### 1. Story laden & verstehen
Nimm `$ARGUMENTS` als ID. Lies die Story-Datei vollständig. Spiegele kurz Akzeptanzkriterien und
betroffene Dateien zurück. Status (state.yaml) auf `in_progress`.

### 2. Umsetzungsplan
Kurzer Plan: welche Dateien, welche Tests zuerst. Halte dich an die in der Story genannten Pfade und
Muster sowie an die Constitution (Standards, Test-Regeln, Security).

### 3. Test-getrieben implementieren (ROT-GRÜN-REFACTOR)
Pro Akzeptanzkriterium / Plan-Schritt:
1. **ROT:** Test schreiben, der das Kriterium prüft.
2. **Scheitern sehen (Pflicht):** Test laufen lassen und **bestätigen, dass er scheitert** — aus dem
   richtigen Grund (Feature fehlt, kein Tippfehler). „Wer den Test nicht scheitern sah, weiß nicht, ob er
   das Richtige prüft." Passt er sofort → er testet Bestehendes, Test korrigieren.
3. **GRÜN:** minimalste Implementierung bis grün — keine Extra-Features, kein „verbessern über den Test hinaus".
4. **Grün sehen:** Test + übrige Tests grün, Ausgabe sauber (keine Fehler/Warnungen).
5. **REFACTOR:** aufräumen, ohne Verhalten zu ändern.
Bestehende Muster nutzen, keine Rad-Neuerfindungen, keine neuen Abhängigkeiten ohne Deckung durch eine
ADR/Constitution. **STOPP wenn blockiert** (fehlende Abhängigkeit, unklare Anweisung, wiederholt scheiternde
Verifikation) — nachfragen statt raten.

### 4. Verifizieren — Eisernes Gesetz
```
KEINE FERTIG-BEHAUPTUNG OHNE FRISCH AUSGEFÜHRTE VERIFIKATIONS-EVIDENZ
```
Vor jeder Status-Behauptung die **Gate-Function**: 1) Welches Kommando beweist die Behauptung? →
2) vollständig ausführen → 3) Ausgabe + Exit-Code lesen, Fehler zählen → 4) bestätigt die Ausgabe die
Behauptung? → 5) erst dann behaupten, **mit gezeigter Ausgabe**. Schritt übersprungen = gelogen.
**Warnsignale — STOPP:** „sollte gehen" / „bin sicher" / „Linter lief" ohne Ausführung; „Super!/Fertig!"
vor der Verifikation; Commit ohne Verifikation. „Linter ≠ Compiler", „Zuversicht ≠ Evidenz."

### 5. Story & State aktualisieren
In der Story-Datei einen kurzen Umsetzungs-Vermerk ergänzen (was gebaut, welche Dateien, welche
Tests). state.yaml: Story-Status auf `review`. Abweichungen von der Spec dokumentieren — bei
größeren Abweichungen `esc:status`/Korrektur vorschlagen.

### 6. Routen
Schlage `esc:review <id>` vor.

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (Story-Status auf review) und ggf. `esc:docs`.
- [ ] Alle Akzeptanzkriterien sind durch tatsächlich laufende Tests belegt.
- [ ] Build/Linter grün; Ausgabe wurde gezeigt (keine Behauptung ohne Beleg).
- [ ] Constitution-Regeln eingehalten; keine ungedeckten neuen Abhängigkeiten.
- [ ] Kein Scope über die Story hinaus; Abweichungen dokumentiert.
- [ ] Story-Status auf `review` gesetzt.
