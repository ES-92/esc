---
name: discover
description: Discovery-Phase von ESC. Führt interaktiv durch Brainstorming und Analyse, betrachtet kritisch bestehende (kommerzielle) Produkte als Inspiration (was der Nutzer mag und warum, plus eigene Vorschläge der KI mit Begründung) und erzeugt einen Product Brief (Problem, Nutzer, Inspiration, Ziele, Scope, Risiken) — noch ohne Technologie. Use when the user has run esc:init and wants to explore/analyze the idea, says "lass uns brainstormen", "discovery", "product brief", "esc discover", or needs to clarify problem and audience before writing a PRD.
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, WebSearch, WebFetch
---

# esc:discover — Brainstorming & Analyse → Product Brief

Ziel: das Problemfeld gemeinsam durchdringen und einen **Product Brief** erzeugen, der die spätere
PRD-Arbeit fokussiert. Beschreibe **WAS und WARUM, nicht WIE** (keine Technologie).

## Sichtweise & Schärfe
Diese Phase wird aus der **analytischen Sicht** geführt — Evidenz statt Annahme: „Woher wissen wir das?"
(`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`). An jedem Gate greift die **skeptische Sicht** an; Tiefe
nach `level` (`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`). Erarbeite Abschnitt für Abschnitt
(`${CLAUDE_PLUGIN_ROOT}/shared/coauthoring.md`).

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/elicitation.md` (Frage-Protokoll + Vertiefungs-Methoden)
- `${CLAUDE_PLUGIN_ROOT}/shared/principles.md`
- `esc/state.yaml` und `esc/docs/constitution.md` (Kontext)

## Vorbedingung
`esc/state.yaml` muss existieren (sonst auf `esc:init` verweisen). Prüfe `level`: Bei Level 0/1 ist
discover optional — weise darauf hin und biete an, direkt zu `esc:prd` zu springen.

## Ablauf (interaktiv, eine Runde je Thema, Antworten sofort persistieren)

### 1. Modus wählen
Biete an: `1) Geführt` (Schritt für Schritt) · `2) Brainstorm` (erst divergent Ideen sammeln, dann
konvergieren) · `3) Schnell` (nur die Kernfragen). Default je nach Level.

### 2. Themen durcharbeiten (Brief-Gerüst)
Erarbeite per Elicitation nacheinander:
1. **Problem** — welcher konkrete Schmerz, mit welchen Folgen heute?
2. **Zielgruppe & Jobs-to-be-Done** — wer, in welcher Situation, will was erreichen?
3. **Heutige Alternativen** — wie lösen sie es jetzt (inkl. „nichts tun")? Was ist daran schlecht?
4. **Produkt-Vision** — ein Satz: für [Zielgruppe] die [Kategorie], die [Kernnutzen].
5. **Ziele & Erfolgsbild** — woran erkennt man Erfolg? (noch grob; messbar wird es im PRD)
6. **Scope** — MoSCoW: Must / Should / Could / **Won't** (Non-Goals explizit!).
7. **Risiken & offene Annahmen** — was muss wahr sein, damit das funktioniert?

### 3. Inspiration & Wettbewerb (kritisch, beidseitig)
Führe die Inspirations-Analyse nach `${CLAUDE_PLUGIN_ROOT}/shared/inspiration.md` durch:
1. **Frag den Nutzer**, welche Produkte/Apps er mag — *was genau* (Feature, Flow, Haptik, Geschäftsmodell)
   und *warum* — und destilliere den dahinterliegenden Bedarf sowie die Übertragbarkeit auf dieses Projekt.
2. **Immer** eine **kurze Web-Wettbewerbsanalyse** (WebSearch/WebFetch, 2–3 gezielte Suchen nach
   vergleichbaren/konkurrierenden Produkten) als Grundlage. **Schlage dann selbst** 2–5 relevante
   (kommerzielle) Produkte vor und sage je konkret: *was* du übernehmen würdest, *warum* (Bezug zu unserem
   Problem/Nutzer), *wie* angepasst — und *was bewusst nicht*. Quellen nennen.
3. Die **skeptische Sicht** prüft jede Übernahme: Bedarf statt Oberfläche, Passung zu Zielgruppe/Zielen/
   Constitution; Verzichte und Anti-Patterns explizit festhalten.
Ergebnis: ein Abschnitt „Inspiration & Wettbewerb" (Tabelle Quelle/Übernehmen/Warum/Anpassung + bewusste Verzichte).

### 4. Kritisch vertiefen (Pflicht bei Level 3/4)
Nach Vision und Scope mindestens **eine** Vertiefungs-Methode anbieten/durchführen
(empfohlen: Pre-Mortem oder Stakeholder-Runde), um blinde Flecken aufzudecken.

### 5. Brief schreiben
Schreibe `esc/docs/product-brief.md` mit Abschnitten: Problem · Zielgruppe & JTBD · Alternativen ·
**Inspiration & Wettbewerb** · Vision · Ziele · Scope (MoSCoW inkl. Non-Goals) · Risiken & Annahmen · offene Fragen.
Aktualisiere `esc/state.yaml`: `artifacts.product_brief: done`, wichtige Entscheidungen ins
`decisions`-Log, `phase` auf nächste Phase.

### 6. Routen
Schlage `esc:prd` als nächsten Schritt vor (bzw. `esc:ux`, falls UI-lastig und gewünscht).

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (TRACKER.md) und `esc:docs` (Überblick/Kontext).
- [ ] Inspiration & Wettbewerb durchgeführt: kurze Web-Wettbewerbsanalyse (immer), Nutzer-Vorlieben *und* eigene Produktvorschläge mit Quellen, je mit Begründung und bewussten Verzichten.
- [ ] `esc/docs/product-brief.md` deckt alle Gerüst-Abschnitte ab; Non-Goals sind explizit.
- [ ] Mindestens eine kritische Vertiefung erfolgte (Level 3/4: Pflicht).
- [ ] Offene Annahmen/Fragen sind festgehalten, nicht verschwiegen.
- [ ] state.yaml und Decision-Log aktualisiert.
