---
name: discover
description: Discovery-Phase von ESC. Führt interaktiv durch Brainstorming und Analyse und erzeugt einen Product Brief (Problem, Nutzer, Ziele, Scope, Risiken) — noch ohne Technologie. Use when the user has run esc:init and wants to explore/analyze the idea, says "lass uns brainstormen", "discovery", "product brief", "esc discover", or needs to clarify problem and audience before writing a PRD.
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, WebSearch, WebFetch
---

# esc:discover — Brainstorming & Analyse → Product Brief

Ziel: das Problemfeld gemeinsam durchdringen und einen **Product Brief** erzeugen, der die spätere
PRD-Arbeit fokussiert. Beschreibe **WAS und WARUM, nicht WIE** (keine Technologie).

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/elicitation.md` (Frage-Protokoll + Vertiefungs-Methoden)
- `${CLAUDE_PLUGIN_ROOT}/shared/principles.md`
- `esc/state.yaml` und `esc/constitution.md` (Kontext)

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

Bei größeren Vorhaben (Level 3/4) optional **Research** anbieten: Markt/Wettbewerb/Domäne via
WebSearch/WebFetch recherchieren und Erkenntnisse einarbeiten — nur auf Wunsch des Nutzers.

### 3. Kritisch vertiefen (Pflicht bei Level 3/4)
Nach Vision und Scope mindestens **eine** Vertiefungs-Methode anbieten/durchführen
(empfohlen: Pre-Mortem oder Stakeholder-Runde), um blinde Flecken aufzudecken.

### 4. Brief schreiben
Schreibe `esc/product-brief.md` mit Abschnitten: Problem · Zielgruppe & JTBD · Alternativen ·
Vision · Ziele · Scope (MoSCoW inkl. Non-Goals) · Risiken & Annahmen · offene Fragen.
Aktualisiere `esc/state.yaml`: `artifacts.product_brief: done`, wichtige Entscheidungen ins
`decisions`-Log, `phase` auf nächste Phase.

### 5. Routen
Schlage `esc:prd` als nächsten Schritt vor (bzw. `esc:ux`, falls UI-lastig und gewünscht).

## Definition of Done
- [ ] Mitlaufende Artefakte aktualisiert: `esc:track` (TRACKER.md) und `esc:docs` (Überblick/Kontext).
- [ ] `esc/product-brief.md` deckt alle Gerüst-Abschnitte ab; Non-Goals sind explizit.
- [ ] Mindestens eine kritische Vertiefung erfolgte (Level 3/4: Pflicht).
- [ ] Offene Annahmen/Fragen sind festgehalten, nicht verschwiegen.
- [ ] state.yaml und Decision-Log aktualisiert.
