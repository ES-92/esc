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

## Design vor Code (hartes Gate)
Keine Implementierung, bevor die zugehörige Spec vom Nutzer freigegeben ist — unabhängig von der
wahrgenommenen Einfachheit. Das gilt für jedes Vorhaben.

## „2–3 Ansätze + Empfehlung" an echten Entscheidungen
An bedeutsamen Weichenstellungen (Produkt-Richtung, UX-Ansatz, Scope, Technologie) nicht die erstbeste
Lösung nehmen: **2–3 wirklich verschiedene Optionen** mit Trade-offs vorlegen, eine **empfehlen** (mit
Begründung), dann den Nutzer wählen lassen. (`esc:architecture` tut das für Technologie schon; gilt auch
für `discover`/`prd`/`ux`.)

## Spec-Self-Review (Abschluss-Gate jeder Spec-Phase)
Bevor ein Spec-Artefakt (`product-brief`, `prd`, FR/NFR, `ux-spec`, `architecture`, `epics`) als `done`
gilt, mit frischen Augen prüfen — nur **echte** Umsetzungs-Probleme flaggen, keine Stil-Nörgelei:

| Kategorie | Worauf achten |
|---|---|
| **Vollständigkeit** | Platzhalter, „TBD/TODO", unfertige Abschnitte |
| **Konsistenz** | interne Widersprüche, gegensätzliche Anforderungen |
| **Klarheit** | Anforderung mehrdeutig genug, um das **Falsche** zu bauen? |
| **Scope** | fokussiert genug für einen Plan (nicht mehrere unabhängige Subsysteme)? |
| **YAGNI** | ungefragte Features, Over-Engineering |

Gefundene Probleme **inline fixen**, dann erst `done`. Kalibrierung: „Nur flaggen, was in der Planung echte
Probleme verursacht."

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
