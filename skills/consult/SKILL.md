---
name: consult
description: Betrachtet eine konkrete Frage oder Entscheidung gezielt aus einer einzelnen kritischen Sichtweise (analytisch, Fokus, Nutzer, Architektur, Planung, pragmatisch, skeptisch oder Prinzipien). Use when the user says "betrachte das aus Sicht X", "zweite Meinung", "kritische Einschätzung", "esc consult", or wants one specific lens on a decision.
argument-hint: "[sichtweise] [frage]"
allowed-tools: Read, Glob, Grep
---

# esc:consult — Eine Sichtweise anlegen

Ziel: eine Frage aus **einer** kritischen Sichtweise beleuchten — kurz, scharf, verwertbar.

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md` — die Sichtweisen, ihre Linsen und Leitfragen
- Relevanter `esc/`-Kontext (state.yaml, betroffenes Artefakt), falls die Frage sich darauf bezieht

## Ablauf
1. **Sichtweise bestimmen.** Aus `$ARGUMENTS`. Ist keine genannt, schlage die 2–4 relevantesten
   Sichtweisen zur Frage als Auswahl vor (AskUserQuestion) und lass wählen.
2. **Kontext laden.** Bezieht sich die Frage auf ein Artefakt (`esc/specs/prd.md`, eine ADR …), lies es kurz.
3. **Aus der Linse antworten.** Wende die Leitfrage und den Fokus der Sichtweise **konkret** auf die
   Frage an: Was ist tragfähig, was greift sie an, welche Annahme prüft sie, was empfiehlt sie?
   Keine generischen Floskeln — immer auf *diese* Frage/dieses Artefakt bezogen.
4. **Verwertbar abschließen.** Eine klare Empfehlung oder die entscheidende Rückfrage. Bei
   entscheidungsrelevantem Ergebnis anbieten, es ins `decisions`-Log zu schreiben.

## Definition of Done
- [ ] Antwort kommt erkennbar aus der gewählten Sichtweise, nicht generisch.
- [ ] Konkreter Bezug zur Frage/zum Artefakt; klare Empfehlung oder Rückfrage am Ende.
