---
name: implement
description: Implementiert eine vorbereitete ESC-Story strikt nach ihrer Story-Datei — testgetrieben, im Rahmen von Constitution und Akzeptanzkriterien — und aktualisiert den Status. Use when a story file is ready and the user says "implement", "Story umsetzen", "dev story", "esc implement [id]", or wants to build the code for a prepared story.
argument-hint: "[story-id, z. B. 1.2]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
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

### 1. Story laden & verstehen
Nimm `$ARGUMENTS` als ID. Lies die Story-Datei vollständig. Spiegele kurz Akzeptanzkriterien und
betroffene Dateien zurück. Status (state.yaml) auf `in_progress`.

### 2. Umsetzungsplan
Kurzer Plan: welche Dateien, welche Tests zuerst. Halte dich an die in der Story genannten Pfade und
Muster sowie an die Constitution (Standards, Test-Regeln, Security).

### 3. Test-getrieben implementieren
Pro Akzeptanzkriterium:
1. Test(s) schreiben, die das Kriterium prüfen (red).
2. Minimal implementieren, bis grün.
3. Refaktorisieren, ohne das Verhalten zu ändern.
Bestehende Muster nutzen, keine Rad-Neuerfindungen, keine neuen Abhängigkeiten ohne Deckung durch
eine ADR/Constitution (sonst nachfragen).

### 4. Verifizieren — kein „fertig" ohne Beleg
Tests **tatsächlich ausführen** (via Bash), Build/Linter laufen lassen. Zeige die Ausgabe. Jedes
Akzeptanzkriterium gegen das Ergebnis prüfen. Schlägt etwas fehl: ehrlich berichten und beheben.

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
