---
name: debug
description: Systematisches Debugging bei Bug, Testfehler oder unerwartetem Verhalten — findet die ROOT CAUSE, bevor irgendein Fix vorgeschlagen wird. Vier Phasen, Rückwärts-Tracing zur Quelle, Fix an der Quelle statt am Symptom. Use when the user says "debug", "Fehler finden", "Bug", "Test schlägt fehl", "warum passiert das", "esc debug", or before proposing any fix.
argument-hint: "[Symptom/Fehlermeldung]"
allowed-tools: Read, Glob, Grep, Bash, Edit, AskUserQuestion
---

# esc:debug — Ursache vor Fix

Ziel: die **eigentliche Ursache** finden, bevor irgendetwas geändert wird. Symptom-Fixe sind ein
Fehlschlag. Geführt aus **skeptischer + pragmatischer** Sicht (`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`).

```
EISERNES GESETZ: KEINE FIXES OHNE ROOT-CAUSE-ANALYSE ZUERST
```
Solange Phase 1 nicht abgeschlossen ist, darfst du keinen Fix vorschlagen. Verletzung des Buchstabens
ist Verletzung des Geistes.

## Die vier Phasen (jede vor der nächsten abschließen)

### Phase 1 — Ursache untersuchen
1. Fehlermeldung/**Stacktrace vollständig** lesen (nicht nur die erste Zeile).
2. **Konsistent reproduzieren.** Nicht reproduzierbar → mehr Daten sammeln, **nicht raten**.
3. **Letzte Änderungen** prüfen (`git diff`, jüngste Commits, Dependencies, Config).
4. In Mehr-Komponenten-Systemen an **jeder Grenze instrumentieren** (Logs/Asserts) und **einmal** laufen
   lassen, um zu sehen **WO** es bricht.
5. **Datenfluss rückwärts tracen:** den fehlerhaften Wert vom Symptom zurück bis zum **ursprünglichen
   Auslöser** verfolgen („was hat das aufgerufen?"). **Fix an der Quelle, nicht am Symptom.**

### Phase 2 — Muster-Analyse
Funktionierendes Beispiel finden und **vollständig** vergleichen; **jede** Differenz benennen (nichts als
„kann nicht wichtig sein" abtun); Abhängigkeiten verstehen.

### Phase 3 — Hypothese & Test
Eine Hypothese formulieren: „Ich vermute **X** ist die Ursache, weil **Y**." Minimal testen — kleinste
mögliche Änderung, **eine Variable**. Verifizieren, bevor es weitergeht. Bei Unklarheit ehrlich: „Ich
verstehe X nicht."

### Phase 4 — Umsetzung
1. **Zuerst** einen **scheiternden Testfall** schreiben, der den Bug reproduziert (siehe `esc:implement`, ROT-GRÜN).
2. **Einen** Fix an der Quelle umsetzen — **kein** „wo ich schon dabei bin".
3. Verifizieren (Regressionstest rot→grün).
4. **Bei ≥3 gescheiterten Fixversuchen: STOPP** — nicht die x-te Hypothese, sondern die **Architektur**
   infrage stellen. „Halten wir an diesem Muster nur aus Trägheit fest?"

## Warnsignale — STOPP (zurück zu Phase 1)
„Quick-Fix jetzt, später untersuchen" · „einfach X ändern und schauen" · „ist wahrscheinlich X, fixe das" ·
Lösung vorschlagen, bevor der Datenfluss getract ist · „ein Fixversuch noch" (bei bereits 2+) · „jeder Fix
deckt an anderer Stelle ein neues Problem auf".

## Definition of Done
- [ ] Ursache ist **belegt** (Phase 1 abgeschlossen, rückwärts zur Quelle getract).
- [ ] Ein Fix an der Quelle; Regressionstest rot→grün (mit gezeigter Ausgabe).
- [ ] Keine Nebenbei-Änderungen; bei ≥3 Fehlversuchen wurde die Architektur hinterfragt.
