---
name: council
description: Lässt mehrere kritische Sichtweisen aufeinanderprallen, um eine Entscheidung mit Trade-offs aus verschiedenen Linsen zu beleuchten, und liefert eine synthetisierte Empfehlung. Use when the user says "mehrere Perspektiven", "lass die Sichtweisen diskutieren", "Pro und Contra abwägen", "esc council", or faces a cross-cutting decision with trade-offs.
argument-hint: "[frage/entscheidung]"
allowed-tools: Read, Glob, Grep, AskUserQuestion
---

# esc:council — Mehr-Perspektiven-Runde

Ziel: eine Entscheidung mit Trade-offs aus **mehreren Sichtweisen** beleuchten — eine moderierte
Mini-Debatte der Linsen, die in einer klaren Synthese mündet. Bei Level 4 an Schlüssel-Gates automatisch.

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md` — die Sichtweisen & ihre Linsen
- Relevanter `esc/`-Kontext (state.yaml, betroffenes Artefakt/ADR)

## Ablauf

### 1. Frage & Teilnehmer
Aus `$ARGUMENTS` die Frage/Entscheidung nehmen (sonst kurz erfragen). Wähle die 3–5 Sichtweisen, deren
Linsen am relevantesten sind (z. B. bei einer Tech-Entscheidung: Architektur, pragmatisch, Fokus, skeptisch).
Biete die Auswahl an, falls sinnvoll.

### 2. Runde 1 — Positionen
Jede gewählte Sichtweise äußert sich **kurz** (1–3 Sätze) aus ihrer Linse: Position + wichtigstes
Argument. Konkret auf die Frage bezogen, kein Geplänkel.

### 3. Runde 2 — Reibung
Lass die Positionen aufeinanderprallen: wo widersprechen sie sich? Die skeptische Sicht bohrt bei jeder
Position nach („und warum…?"). Spannungen und echte Trade-offs herausarbeiten, nicht glätten.

### 4. Synthese
Moderiere zu einer **Empfehlung**: was die beste Argumentlage nahelegt, welche Bedenken bestehen bleiben,
welche Bedingung die Entscheidung kippen würde. Dem Nutzer als Auswahl zur Entscheidung vorlegen.

### 5. Festhalten
Bei einer getroffenen Entscheidung: ins `decisions`-Log (mit den wichtigsten Gegenargumenten als
verworfene Alternativen). Betrifft es eine Architektur-Frage, ADR über `esc:architecture` anstoßen.

## Definition of Done
- [ ] Mind. 3 Sichtweisen mit unterscheidbaren, konkreten Positionen zur Frage.
- [ ] Echte Reibung/Trade-offs sichtbar gemacht (kein künstlicher Konsens).
- [ ] Klare Synthese + Entscheidung; Ergebnis im Decision-Log.
