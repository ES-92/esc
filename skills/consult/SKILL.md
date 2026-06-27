---
name: consult
description: Ruft gezielt eine ESC-Persona (Marie Curie/Analyse, Steve Jobs/Produkt, Walt Disney/UX, Einstein/Architektur, Eisenhower/Planung, Linus Torvalds/Engineering, Sokrates/Skepsis, Gandhi/Prinzipien) zu einer konkreten Frage. Use when the user says "frag <Persona>", "was würde Einstein/Jobs dazu sagen", "hol dir eine zweite Meinung", "esc consult", or wants a specific expert lens on a decision.
argument-hint: "[persona] [frage]"
allowed-tools: Read, Glob, Grep
---

# esc:consult — Persona gezielt befragen

Ziel: eine einzelne ESC-Persona zu einer konkreten Frage zu Wort kommen lassen — mit ihrer Stimme und
vor allem ihrer **kritischen Linse**. Kurz, scharf, verwertbar.

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/personas.md` — Cast, Linsen, Signaturen
- Relevanter `esc/`-Kontext (state.yaml, betroffenes Artefakt), falls die Frage sich darauf bezieht

## Ablauf
1. **Persona bestimmen.** Aus `$ARGUMENTS` (Name oder Rolle). Ist keine genannt, schlage 2–4 passende
   Personas zur Frage als Auswahl vor (AskUserQuestion) und lass wählen.
2. **Kontext laden.** Bezieht sich die Frage auf ein Artefakt (`esc/prd.md`, eine ADR …), lies es kurz.
3. **In Stimme antworten.** 1–2 Sätze in der Stimme der Persona, dann ihre **konkrete** Einschätzung
   aus ihrer Linse: Was sie gut findet, was sie angreift, welche Annahme sie prüft, was sie empfiehlt.
   Keine generischen Floskeln — immer auf *diese* Frage/dieses Artefakt bezogen.
4. **Verwertbar abschließen.** Eine klare Empfehlung oder die entscheidende Rückfrage. Bei
   entscheidungsrelevantem Ergebnis anbieten, es ins `decisions`-Log zu schreiben.

## Definition of Done
- [ ] Antwort kommt erkennbar aus der Linse der gewählten Persona, nicht generisch.
- [ ] Konkreter Bezug zur Frage/zum Artefakt; klare Empfehlung oder Rückfrage am Ende.
