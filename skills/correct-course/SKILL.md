---
name: correct-course
description: Managt eine wesentliche Änderung mitten in der Umsetzung — geänderte Anforderung, neue/aktualisierte externe Quelle, technischer Blocker oder Scope-Shift. Analysiert die Auswirkung auf Specs, Architektur und Stories, erstellt einen Änderungsvorschlag und zieht die betroffenen Artefakte konsistent nach. Use when the user says "correct course", "kurs korrigieren", "Anforderung hat sich geändert", "Spec stimmt nicht mehr", "esc correct-course".
argument-hint: "[was hat sich geändert]"
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, Bash
---

# esc:correct-course — Spec-Drift kontrolliert auffangen

Ziel: wenn sich mitten in der Umsetzung etwas Wesentliches ändert, **nicht** still weiterdriften,
sondern Auswirkung analysieren, bewusst entscheiden und die Specs konsistent nachziehen.

## Sichtweise & Schärfe
Geführt aus **skeptischer** + **Planungs-Sicht** (`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`): Ist die
Änderung wirklich nötig? Was ist der kleinste konsistente Eingriff? Tiefe nach `level`
(`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`).

## Lies zuerst
- `esc/state.yaml`, `esc/specs/` (relevante Specs/ADRs/Stories), `esc/specs/sources.md` (falls vorhanden)

## Ablauf

### 1. Auslöser erfassen
Aus `$ARGUMENTS` bzw. per Frage: **was** hat sich geändert und **warum**? Typen: geänderte Anforderung ·
**aktualisierte externe Quelle** (SOP/Vorschrift, vgl. `esc:sources`) · technischer Blocker/Erkenntnis ·
Scope-Shift · falsche Annahme. Die **skeptische Sicht** prüft: ist die Änderung real und nötig, oder nur Bequemlichkeit?

### 2. Impact-Analyse
Bestimme **konkret** die betroffenen Artefakte: welche Requirements (FR/NFR), ADRs, UX-Teile, Epics,
Stories und welcher bereits gebaute Code. Markiere, was nur angepasst vs. neu gemacht vs. verworfen wird.

### 3. Änderungsvorschlag (Auswahl)
Lege 2–3 Optionen vor mit Trade-offs (z. B. bestehende Story umbauen · neue Story anhängen · zurückstellen ·
Architektur-Delta nötig). Empfehlung + Begründung. Der Nutzer entscheidet.

### 4. Artefakte konsistent nachziehen
Aktualisiere die betroffenen Specs **abschnittsweise** (`coauthoring.md`): Requirements, ggf. neue **ADR**
(bei Architektur-Folgen), UX, Epics/Stories. Story-Status in `state.yaml` anpassen (z. B. betroffene
Stories auf `todo`/`in_progress` zurück). Alles ins `decisions`-Log mit Begründung.

### 5. Abschluss
`esc:track` + `esc:docs` aktualisieren; bei geänderter Constitution/Quellen `esc:bind` nachziehen.
Klar zusammenfassen, was sich geändert hat und was als Nächstes zu tun ist.

## Definition of Done
- [ ] Auslöser und betroffene Artefakte sind klar benannt (Impact-Analyse).
- [ ] Eine bewusst gewählte Option ist umgesetzt; alle betroffenen Specs/Stories konsistent nachgezogen.
- [ ] Entscheidung samt Begründung im Decision-Log; Tracker/Doku (und ggf. CLAUDE.md) aktualisiert.
