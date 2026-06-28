---
name: bind
description: Erzeugt/aktualisiert eine CLAUDE.md im Produkt-Root, die Claude Code dauerhaft auf die ESC-Specs (constitution, Requirements, Architektur, Stories) verweist — so gelten die Specs als Guardrails auch außerhalb der ESC-Skills. Use when the user says "guardrails verankern", "CLAUDE.md generieren", "Specs verbindlich machen", "esc bind", or after the constitution/specs changed.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# esc:bind — Specs als ambiente Guardrails (CLAUDE.md)

Ziel: die ESC-Specs für **jede** Claude-Code-Sitzung verbindlich machen — nicht nur innerhalb der
ESC-Skills. Dazu einen **verwalteten Block** in der `CLAUDE.md` des Produkt-Roots pflegen, der auf die
Specs zeigt und die wichtigsten nicht-verhandelbaren Regeln verdichtet.

## Lies zuerst
- `esc/specs/constitution.md` (Pflicht), plus Index der vorhandenen Specs in `esc/specs/`
- vorhandene `CLAUDE.md` im Produkt-Root (falls vorhanden) — **nicht überschreiben**

## Ablauf
1. **Constitution destillieren:** die 3–7 wichtigsten, prüfbaren Regeln als Kurz-Bullets.
2. **Spec-Index sammeln:** welche Spec-Dateien existieren (constitution, requirements/, architecture/, ux-spec, epics, stories/, codebase-map).
3. **Verwalteten Block schreiben/aktualisieren** in `./CLAUDE.md` — exakt zwischen den Markern, den Rest
   der Datei unangetastet lassen. Existiert keine CLAUDE.md, neu anlegen. Existiert der Block schon, nur ihn ersetzen.

```markdown
<!-- ESC:BEGIN (auto-generiert von esc:bind — nicht von Hand editieren) -->
## Spec-Guardrails (ESC)

Dieses Projekt wird spec-getrieben mit ESC entwickelt. **Vor Code-Änderungen die relevanten Specs lesen
und einhalten.** Bei Konflikt gewinnt die Spec; Spec-Änderungen laufen über die ESC-Skills, nicht ad hoc.

- Nicht-verhandelbare Regeln: `esc/specs/constitution.md`
- Anforderungen: `esc/specs/requirements/functional.md` · `non-functional.md`
- Architektur & Entscheidungen: `esc/specs/architecture/`
- Stories (Akzeptanzkriterien): `esc/specs/stories/`
- Ist-Stand (Brownfield): `esc/specs/codebase-map.md`

**Kernregeln (Digest):**
- <Regel 1>
- <Regel 2>
- …
<!-- ESC:END -->
```
Nur Verweise auf tatsächlich existierende Dateien aufnehmen.

4. **Bestätigen:** kurz melden, was geschrieben wurde, und dass der restliche CLAUDE.md-Inhalt erhalten blieb.

## Definition of Done
- [ ] `./CLAUDE.md` enthält einen aktuellen, klar markierten ESC-Block; übriger Inhalt unverändert.
- [ ] Digest spiegelt die aktuelle Constitution; nur existierende Spec-Pfade verlinkt.
