---
name: test
description: Generiert automatisierte Tests (Unit/Integration/E2E) für ein Feature oder eine Story aus deren Akzeptanzkriterien und führt sie aus — im Test-Framework des Projekts, im Rahmen der Constitution. Use when the user says "Tests generieren", "Testabdeckung", "E2E-Tests für [Feature]", "esc test", or wants tests for an existing feature/story without re-implementing it.
argument-hint: "[story-id oder Feature/Bereich]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# esc:test — Tests aus Akzeptanzkriterien generieren

Ziel: testbare Akzeptanzkriterien in **echte, laufende Tests** überführen — für eine Story oder ein
bestehendes Feature. Ergänzt `esc:implement` (das Story-begleitend testet) um einen gezielten Test-Pass.

## Sichtweise & Schärfe
Aus der **pragmatischen Sicht** — Tests müssen real laufen und das Kriterium wirklich prüfen, nicht nur
existieren (`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`). Kein „grün durch leere Tests".

## Lies zuerst
- Ziel aus `$ARGUMENTS`: Story (`esc/specs/stories/<id>-*.md`) oder Feature/Bereich.
- Zugehörige Akzeptanzkriterien/Requirements (`esc/specs/requirements/functional.md`), `esc/specs/constitution.md`.
- Bestehendes **Test-Setup** im Code (Framework, Ordner, Muster) via Glob/Grep — daran anlehnen.

## Ablauf
1. **Kriterien sammeln:** die zu deckenden Akzeptanzkriterien/Requirements auflisten. Fehlt das Test-
   Framework in der Constitution, aus dem Code ableiten oder den Nutzer fragen.
2. **Testplan:** je Kriterium die passende Ebene (Unit/Integration/E2E) und Fälle (Happy Path +
   Edge-/Fehlerpfade aus der Spec) festlegen. Kurz mit dem Nutzer bestätigen.
3. **Tests schreiben:** an bestehende Muster/Ordner/Naming halten; aussagekräftige Assertions, die das
   Kriterium echt prüfen. Keine trivialen Tautologien.
4. **Ausführen & belegen:** Tests via Bash laufen lassen, Ausgabe zeigen. Rot/grün ehrlich berichten.
   Decken sie ein Kriterium *nicht*, das benennen statt zu kaschieren.
5. **Abdeckung melden:** welches Kriterium durch welchen Test gedeckt ist; offene Lücken markieren.

## Definition of Done
- [ ] Jedes adressierte Akzeptanzkriterium ist durch mindestens einen aussagekräftigen, laufenden Test gedeckt.
- [ ] Tests folgen den Projekt-Konventionen; Ausgabe wurde gezeigt (kein „grün" ohne Beleg).
- [ ] Nicht abgedeckte Kriterien sind explizit benannt.
