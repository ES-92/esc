# ESC — Co-Authoring-Protokoll (Abschnitt für Abschnitt)

Specs werden in ESC **nicht in einem Rutsch generiert**, sondern **Abschnitt für Abschnitt gemeinsam
mit dem Nutzer** erarbeitet — kritisch, mit voller Kontrolle des Nutzers über jeden Abschnitt. Das gilt
für alle erarbeiteten Artefakte (Product Brief, PRD/FR/NFR, UX-Spec, Architektur, Epics, Stories).

## Die Schleife (pro Abschnitt)
Für **jeden** Abschnitt eines Dokuments:

1. **Kontext nennen.** Sage kurz, welcher Abschnitt jetzt dran ist und warum er zählt (1 Zeile).
2. **Entwurf vorschlagen.** Lege einen konkreten Entwurf des Abschnitts vor — knapp, konkret, nicht
   ausufernd. Wo es Optionen gibt, biete sie als Auswahl an (Pfeil + Leertaste, siehe `elicitation.md`).
3. **Kritisch angreifen.** Aus der für die Phase führenden Sichtweise (`viewpoints.md`) + an Gates aus
   der **skeptischen Sichtweise**: Was ist schwach, unbelegt, mehrdeutig, unvollständig? Konkret, nicht generisch.
4. **Nutzer entscheidet.** Der Nutzer bestätigt, ändert oder verwirft. **Warte auf die Antwort.**
   Übernimm Änderungen wörtlich. Nichts ohne Zustimmung festschreiben.
5. **Persistieren.** Den finalen Abschnitt sofort ins Zieldokument schreiben; relevante Entscheidungen
   ins Decision-Log (`esc/state.yaml`).
6. **Weiter.** Erst dann zum nächsten Abschnitt. Optional anbieten, eine Pause zu machen oder zu springen.

## Tiefe skaliert mit Level (`intensity.md`)
- **Level 0/1:** kompakte Schleife — Entwurf + 1 kritische Rückfrage je Abschnitt, kein Zerreden.
- **Level 2:** je Abschnitt skeptischer Einwand + Bestätigung.
- **Level 3/4:** je Abschnitt mehrere Einwände, Annahmen-Audit, bei Schlüsselabschnitten Mehr-Perspektiven-Runde.

## Regeln
- **Ein Abschnitt zur Zeit.** Niemals das ganze Dokument auf einmal hinwerfen und „passt das?" fragen.
- **Der Nutzer hat das letzte Wort** über jeden Abschnitt — ESC schlägt vor und hinterfragt, entscheidet aber nicht allein.
- **Keine stillen Annahmen.** Unklarheiten werden zu Rückfragen, nicht zu geratenem Text.
- **Konsistenz prüfen.** Neue Abschnitte dürfen früheren nicht widersprechen; Widersprüche aktiv ansprechen.

## Standard-Abschnittsfolgen (Anhalt)
- **Product Brief:** Problem · Zielgruppe & JTBD · Alternativen · Inspiration & Wettbewerb · Vision · Ziele · Scope/Non-Goals · Risiken & Annahmen.
- **PRD:** Überblick/Problem · Ziele & Metriken · (→ FR-Dokument) · (→ NFR-Dokument) · Non-Goals · Annahmen.
- **Funktionale Requirements (FR):** je Feature-Bereich ein Abschnitt mit nummerierten, testbaren Anforderungen.
- **Nicht-funktionale Requirements (NFR):** Performance · Sicherheit · Datenschutz · Zugänglichkeit · Skalierung · Betrieb.
- **UX-Spec:** Screen-Inventar · Kern-Flows · Zustände je Ansicht · Verhaltensregeln · Edge-/Leerzustände · Barrierefreiheit.
- **Architektur:** Treiber · Kontext/Komponenten · Datenmodell · Schnittstellen · Querschnitt · je Entscheidung eine ADR.
- **Epics & Stories:** je Epic ein Abschnitt; je Story Beschreibung + testbare Akzeptanzkriterien + Abhängigkeiten.
