# Design-Spec: ESC × obra/superpowers – Fusion (v2.0.0)

- **Datum:** 2026-07-01
- **Status:** Zur Umsetzung freigegeben (nach Nutzer-Review)
- **Zielversion:** ESC v2.0.0 (21 → 22 Skills)

## 1. Ziel & Kontext

ESC (Erik's Spec Crafting) soll die **Disziplinen** der obra/superpowers-Skills *echt eingearbeitet*
bekommen — nicht als separate `shared/`-Referenzdateien, sondern als konkrete **Schritte, Gates und
Kern-Prinzipien innerhalb der bestehenden Skills**, gespeist aus den **Originalquellen** (Repo
`github.com/obra/superpowers`). Gewählte Richtung: **A+C** (direkt einweben + authentische Quellen).

Alle eingewobenen Inhalte werden **auf Deutsch lokalisiert**; nur die Eigennamen der Original-Skills
bleiben als Referenz erhalten.

## 2. Geltungsbereich & Nicht-Ziele

**Im Scope** (die vom Nutzer gewählten Muster 2–10):
Umsetzungsplan pro Story (writing-plans), Verification-before-completion, prägnantes/klares Schreiben,
systematisches Debugging (neuer Skill), Design-Taste in Mockups, Brainstorming-Disziplin (2–3 Ansätze +
Design-Gate), Spec-Self-Review, YAGNI, Git-Worktrees.

**Bewusst NICHT** (YAGNI):
- Kein eigenständiger Skill pro Disziplin (kein `esc:plan`, `esc:verify`, `esc:worktree`) — nur **ein**
  neuer Skill (`esc:debug`); alles andere wächst in bestehende Skills.
- Keine `shared/`-Disziplin-Sidecars (explizite Nutzer-Vorgabe).
- Keine Übernahme von `subagent-driven-development`, `dispatching-parallel-agents`,
  `finishing-a-development-branch` in dieser Version.

**Ehrliche Korrekturen (Quellen-Recherche):**
- `elements-of-style` / `writing-clearly-and-concisely` ist **kein** obra/superpowers-Skill. Prägnantes
  Schreiben wird daher über die authentische **Spec-Self-Review** („Clarity") verankert, nicht als
  erfundene Quelle.
- Ein eigenständiger `YAGNI`-Skill existiert **nicht**. YAGNI wird in der echten obra-Form eingebaut:
  Grep-auf-Nutzung → ungenutzt → entfernen (aus `receiving-code-review`) plus das Mantra „DRY. YAGNI. TDD."

## 3. Authentische obra-Devices (durchgängig, auf Deutsch)

Diese Stilmittel prägen alle eingewobenen Abschnitte:
1. **Eisernes Gesetz** — das eine Nicht-Verhandelbare je Disziplin, in einem Codeblock hervorgehoben.
2. **„Verletzung des Buchstabens ist Verletzung des Geistes."** — gegen Regel-Lawyering.
3. **„Warnsignale — STOPP"** — Listen typischer Ausreden/Fehlverhalten, die zum Prozess-Neustart zwingen.
4. **„Ausrede → Realität"** — kurze Tabellen, die Rationalisierungen entkräften.
5. **Announce + REQUIRED-SUB-SKILL** — jede Phase kündigt an, was sie tut, und verkettet den nächsten Schritt.

## 4. Neue/erweiterte Kern-Prinzipien (`shared/principles.md`)

Ergänzt bzw. verschärft (tragen die Fusion ins ESC-Selbstverständnis):
- **P: Evidenz vor Behauptung (Eisernes Gesetz).** Kein „fertig/behoben/grün" ohne frisch ausgeführte
  Verifikation in derselben Nachricht. Verletzung des Buchstabens = Verletzung des Geistes.
- **P: Design vor Code (hartes Gate).** Keine Implementierung, bevor das Design/die Spec vom Nutzer
  freigegeben ist — unabhängig von der wahrgenommenen Einfachheit.
- **P: YAGNI, rücksichtslos.** Im Zweifel weglassen; „professionelle" Zusatz-Features nur, wenn nachweislich
  genutzt (Grep-Prüfung).
- **P: Keine Platzhalter.** In Specs/Plänen kein „TBD", „TODO", „später ausfüllen", „ähnlich wie oben".
- **P: Keine performative Zustimmung.** Auf Feedback kein „Du hast völlig recht!/Danke!"; stattdessen
  verifizieren, dann faktisch quittieren („Behoben. [was geändert]") oder technisch begründet widersprechen.

## 5. Einweb-Landkarte (pro Skill)

### 5.1 `esc:implement` ← verification-before-completion, TDD-„watch it fail", executing-plans, worktrees
- **Eisernes Gesetz (Verifikation)** als Codeblock: „KEINE FERTIG-BEHAUPTUNG OHNE FRISCHE VERIFIKATIONS-EVIDENZ".
- **Gate-Function** (vor jeder Status-Behauptung), 5 Schritte: 1) Welches Kommando beweist die Behauptung?
  2) Vollständig ausführen 3) Ausgabe + Exit-Code lesen, Fehler zählen 4) Bestätigt die Ausgabe die Behauptung?
  5) Erst dann behaupten — **mit Evidenz**. „Schritt übersprungen = gelogen, nicht verifiziert."
- **„Scheitern sehen"**-Mandat im ROT-GRÜN-REFACTOR: den Test *zuerst scheitern sehen*, sonst weiß man nicht,
  ob er das Richtige prüft.
- **„STOPP wenn blockiert, nicht raten"** (executing-plans): bei fehlender Abhängigkeit, unklarer Anweisung
  oder wiederholt scheiternder Verifikation anhalten und nachfragen.
- **Worktree-Option** (using-git-worktrees): Isolation erst *erkennen* (`GIT_DIR`/`GIT_COMMON`, Submodul-Guard),
  dann native Tools bevorzugen, sonst `git worktree add` in ein **ignoriertes** Verzeichnis (`.worktrees/`,
  vorher `git check-ignore`), Baseline-Tests vor Start. Nur auf Nutzer-Zustimmung.
- **Warnsignale — STOPP:** „sollte jetzt gehen", „bin sicher", „Linter lief" ohne Ausführung; Zufriedenheit
  vor Verifikation („Super!/Fertig!"); Commit/PR ohne Verifikation.

### 5.2 `esc:story` ← writing-plans
Neuer **Pflicht-Abschnitt „## Umsetzungsplan"** in der Story-Datei, im authentischen writing-plans-Stil:
- **Datei-Landkarte zuerst** (welche Dateien, je eine klare Verantwortung; zusammen Geändertes zusammen).
- **Task-Right-Sizing:** kleinster Schnitt, den ein Reviewer eigenständig freigeben/ablehnen könnte; endet
  mit einem unabhängig testbaren Ergebnis.
- **Bite-sized Schritte** (je 2–5 Min, eine Aktion), TDD-strukturiert:
  1. Scheiternden Test schreiben
  2. Test laufen lassen — **Erwartet: FEHLSCHLAG**
  3. Minimale Implementierung
  4. Test laufen lassen — **Erwartet: BESTANDEN**
  5. Committen
- **Interfaces je Task** (Consumes/Produces mit exakten Signaturen); **exakte Dateipfade**.
- **„Keine Platzhalter"** (hart): kein „TBD/TODO/später", kein „Fehlerbehandlung ergänzen" ohne Konkretisierung,
  kein „ähnlich wie Task N" (Code wiederholen).
- **Plan-Self-Review** (selbst, kein Subagent): Spec-Abdeckung (jede Anforderung → ein Task), Platzhalter-Scan,
  Typ-/Namens-Konsistenz über Tasks.

### 5.3 `esc:debug` (NEU) ← systematic-debugging + root-cause-tracing
Vollständige Spezifikation in Abschnitt 6.

### 5.4 `esc:review` ← verification, YAGNI (grep), receiving-code-review
- **Verifikations-Gate** vor „done": jedes Akzeptanzkriterium mit frisch ausgeführter Evidenz.
- **Authentische YAGNI-Prüfung:** bei „sollten wir auch X bauen/ordentlich machen" → Codebase greppen;
  **ungenutzt → Entfernen vorschlagen**; genutzt → sauber umsetzen.
- **receiving-code-review-Disziplin** (für den Umgang mit Findings, z. B. in `implement`/`correct-course`):
  erst vollständig lesen, in eigenen Worten wiedergeben/nachfragen, gegen Codebase verifizieren, dann
  faktisch quittieren **oder** technisch begründet widersprechen. **Verboten:** „Du hast völlig recht!",
  „Guter Punkt!", „Danke fürs Finden!" — stattdessen einfach „Behoben. [was]".
- **Regressionstest-Muster:** Test schreiben → läuft (grün) → Fix zurücknehmen → Test **muss scheitern** →
  Fix wiederherstellen → grün.

### 5.5 `esc:ux` + `shared/mockups.md` ← design-taste-frontend
- **„Design-Lesart"-Einzeiler** vor jedem Mockup: „Lese das als: <Seitentyp> für <Zielgruppe>, mit
  <Vibe>-Sprache, Richtung <Design-System/Ästhetik>."
- **Drei Dials** (aus dem Brief abgeleitet, konservativ bei Produkt-UI/Trust-first): `DESIGN_VARIANZ`,
  `BEWEGUNG`, `DICHTE`.
- **Echte Design-Systeme:** liest der Brief als bekanntes System (Fluent/Material/Carbon/Polaris/Primer/
  GOV.UK/USWDS/Radix/shadcn/Tailwind …), das **offizielle Paket** nutzen statt CSS nachzubauen; **ein**
  System pro Projekt.
- **Anti-Default-Disziplin:** keine KI-Lila-Verläufe, kein zentrierter Hero über dunklem Mesh, keine drei
  gleichen Feature-Cards, kein generisches Glassmorphism überall, kein Inter+slate-900 als Reflex.
- **Ehrlich:** design-taste-frontend zielt originär auf Landing/Portfolio/Redesign; ESC übernimmt die
  **Prinzipien** (Lesart, Dials, echte Systeme, Anti-Default) und passt sie auf die jeweilige Produkt-UI an.

### 5.6 `esc:discover` / `esc:prd` / `esc:ux` ← brainstorming
- **Hartes Design-Gate:** keine Implementierung vor freigegebenem Design/Spec.
- **Eine Frage nach der anderen** (verstärkt das bestehende Co-Authoring).
- **„2–3 Ansätze + Empfehlung"** an echten Produkt-/UX-Entscheidungen (nicht nur in `architecture`).

### 5.7 Alle Spec-erzeugenden Skills ← spec-document-reviewer
**Abschluss-Gate „Spec-Self-Review"** in `discover`, `prd`, `ux`, `architecture`, `epics`: frische-Augen-Check
auf **Completeness** (Platzhalter/TBD/Lücken), **Consistency** (Widersprüche), **Clarity** (mehrdeutig genug,
um das Falsche zu bauen?), **Scope** (fokussiert genug für einen Plan?), **YAGNI** (ungefragte Features).
Kalibrierung: nur echte Umsetzungs-Probleme flaggen, keine Stil-Nörgelei. Inline fixen.

## 6. Neuer Skill: `esc:debug`

- **Zweck:** systematisches Debugging bei Bug/Testfehler/unerwartetem Verhalten — Ursache vor Fix.
- **Sichtweise:** skeptisch + pragmatisch.
- **Eisernes Gesetz:** „KEINE FIXES OHNE ROOT-CAUSE-ANALYSE ZUERST".
- **Vier Phasen (jede vor der nächsten abschließen):**
  1. **Ursache untersuchen:** Fehlermeldung/Stacktrace vollständig lesen; konsistent reproduzieren (nicht
     reproduzierbar → mehr Daten sammeln, nicht raten); letzte Änderungen prüfen (git diff/Deps/Config);
     in Mehr-Komponenten-Systemen an **jeder** Grenze instrumentieren (einmal laufen lassen: **WO** bricht es);
     den fehlerhaften Wert **rückwärts zur Quelle** tracen. „Fix an der Quelle, nicht am Symptom."
  2. **Muster-Analyse:** funktionierendes Beispiel finden, **vollständig** vergleichen, **jede** Differenz
     benennen (nichts als „kann nicht wichtig sein" abtun).
  3. **Hypothese & Test:** eine Hypothese („Ich vermute X, weil Y"), minimal testen, eine Variable; verifizieren,
     bevor es weitergeht; bei Unklarheit „Ich verstehe X nicht" sagen.
  4. **Umsetzung:** **zuerst** scheiternder Testfall (reproduziert den Bug), dann ein einzelner Fix (kein
     „wo ich schon dabei bin"), verifizieren. **Bei ≥3 gescheiterten Fixversuchen: STOPP — Architektur infrage
     stellen** (nicht bloß neue Hypothese).
- **Warnsignale — STOPP:** „Quick-Fix jetzt, später untersuchen"; „einfach X ändern und schauen"; „ist
  wahrscheinlich X"; Lösung vor Datenfluss-Trace; „ein Fixversuch noch" (bei bereits 2+).
- **Definition of Done:** Ursache belegt (Phase 1 abgeschlossen); ein Fix an der Quelle; Regressionstest
  rot→grün; keine Nebenbei-Änderungen.

## 7. Betroffene Dateien (Änderungsliste)

- **Neu:** `skills/debug/SKILL.md`
- **Geändert (Skills):** `implement`, `story`, `review`, `ux`, `discover`, `prd`, `architecture`, `epics`
- **Geändert (shared):** `principles.md`, `mockups.md`, `coauthoring.md` (Design-Gate/2-3-Ansätze),
  `elicitation.md` (Announce-Stil)
- **Geändert (Meta):** `.claude-plugin/plugin.json` (v2.0.0, Beschreibung), `README.md` (22 Skills, neue Devices)

## 8. Versionierung

- **v2.0.0** — Meilenstein „superpowers-Fusion". Commands/Workspace-Struktur bleiben **abwärtskompatibel**
  (keine Umbenennung, keine Pfadänderung); die Major-Nummer markiert den methodischen Tiefensprung.
- Skill-Zahl: **22** (neu: `esc:debug`).

## 9. Definition of Done (für die Umsetzung dieser Spec)

- [ ] Alle eingewobenen Inhalte auf Deutsch; obra-Eigennamen nur als Referenz.
- [ ] `esc:debug` existiert mit Eisernem Gesetz, 4 Phasen, Warnsignalen.
- [ ] `esc:story` erzeugt einen Pflicht-Umsetzungsplan (bite-sized, TDD-Schritte, keine Platzhalter).
- [ ] `esc:implement` enthält Verifikations-Eisernes-Gesetz + Gate-Function + Worktree-Option.
- [ ] `esc:review` enthält Verifikations-Gate, YAGNI-Grep-Prüfung, receiving-review-Disziplin.
- [ ] `esc:ux`/`mockups.md` enthält Design-Lesart, Dials, echte-Systeme-Regel, Anti-Default.
- [ ] Spec-Self-Review-Gate in allen Spec-Skills.
- [ ] `principles.md` um die 5 neuen Kern-Prinzipien ergänzt.
- [ ] Frontmatter (22/22), keine toten Referenzen, JSON valide; README + plugin.json auf v2.0.0.
- [ ] Commit + Tag `v2.0.0` gepusht.

## 10. Offene Fragen

Keine offenen Blocker. Bewusst später (nicht in v2.0.0): `subagent-driven-development`-Verkettung,
`finishing-a-development-branch`, ein `requesting-code-review`-Subagent als eigener Schritt.
