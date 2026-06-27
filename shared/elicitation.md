# ESC — Elicitation-Protokoll

Dieses Protokoll definiert, **wie** ESC im Terminal mit dem Nutzer interagiert. Alle Phasen-Skills
verwenden es. Ziel: geführte, kritisch hinterfragende Konversation statt Monolog — der Nutzer trifft
Entscheidungen, die KI hält sie fest.

## Goldene Regeln
1. **Immer warten.** Stelle eine Frage (oder eine eng zusammengehörige Gruppe) und **warte auf die
   Antwort des Nutzers, bevor du weitermachst.** Beantworte dich niemals selbst.
2. **Nummerierte Optionen, mehrere pro Zeile.** Biete konkrete Auswahlmöglichkeiten an, kompakt in
   einer oder wenigen Zeilen, plus immer eine offene Option.
3. **Eine Entscheidung pro Schritt.** Nicht 8 Fragen auf einmal. Lieber kurze, fokussierte Runden.
4. **Defaults vorschlagen.** Leite aus Kontext (Codebase, bisherige Antworten) eine empfohlene Option
   ab und markiere sie. Der Nutzer kann mit Enter/„1" bestätigen.
5. **Sofort persistieren.** Schreibe jede Antwort unmittelbar in das zugehörige Artefakt bzw. ins
   Decision-Log (`esc/state.yaml`), bevor du die nächste Frage stellst.
6. **Kritisch bleiben.** Nimm Antworten nicht unkritisch hin. Decke Widersprüche, fehlende Fälle und
   unausgesprochene Annahmen auf — dafür gibt es die Vertiefungs-Methoden (unten).

## Frage-Format (Standard)

```
❓ Schritt 2/5 — Zielgruppe

Wer ist die primäre Zielgruppe?
  1) Endkunden (B2C)   2) Unternehmen (B2B)   3) Interne Teams   4) Entwickler/API
  5) Etwas anderes — beschreibe es

→ Antworte mit Zahl(en) oder eigenem Text. (Empfehlung aus Kontext: 2)
```

- Mehrfachauswahl explizit erlauben, wo sinnvoll: „Mehrere möglich, z. B. `1,3`".
- Bei freier Eingabe nachhaken, bis die Antwort konkret genug für eine testbare Spec ist.
- Optional kann das native `AskUserQuestion`-Tool genutzt werden, wenn 2–4 saubere Optionen reichen;
  für >4 Optionen oder freie Diskussion das Markdown-Menü oben verwenden.

## Vertiefungs-Methoden (kritisches Hinterfragen)

Nach jedem fertig erarbeiteten Abschnitt (z. B. ein PRD-Kapitel, eine Architektur-Entscheidung) bietet
der Skill an, den Abschnitt mit **einer** Methode zu schärfen. Format:

```
🔍 Abschnitt „Erfolgsmetriken" entworfen. Vertiefen?
  1) Pre-Mortem — „Angenommen es scheitert in 6 Monaten — warum?"
  2) Stakeholder-Runde — Sichten von Nutzer, Dev, Business, Support gegenüberstellen
  3) Red-Team — Annahmen aktiv angreifen, Lücken suchen
  4) 5-mal-Warum — Ursache hinter dem Ziel freilegen
  5) Erste-Prinzipien — auf Grundwahrheiten herunterbrechen
  [r] andere Methoden zeigen   [x] passt, weiter

→ Zahl wählen oder [x].
```

### Methoden-Katalog (kontextabhängig 4–5 anbieten)
- **Pre-Mortem** — Scheitern in der Zukunft annehmen, Ursachen rückwärts ableiten.
- **Stakeholder-Runde** — gleiche Frage aus Sicht verschiedener Rollen beantworten (Nutzer, Dev, Business, Support, Security).
- **Red-Team vs. Blue-Team** — eine Seite greift die Spec an, die andere verteidigt.
- **5-mal-Warum** — wiederholt „Warum?" fragen, um zur Wurzel zu kommen.
- **Erste-Prinzipien** — Annahmen entfernen, von Grundwahrheiten neu aufbauen.
- **Tree-of-Thoughts** — mehrere Lösungswege parallel andenken, dann besten wählen.
- **Edge-Case-Jagd** — Grenzfälle, Fehlerpfade, Nebenläufigkeit, leere/maximale Eingaben systematisch durchgehen.
- **Annahmen-Audit** — alle impliziten Annahmen auflisten und einzeln auf Gültigkeit prüfen.
- **Inversions-Test** — „Was würde dieses Feature garantiert ruinieren?" und dann das Gegenteil sichern.
- **MoSCoW** — Must/Should/Could/Won't, um Scope zu schärfen.

## Gate-Regel (Pflicht-Vertiefung)
An kritischen Gates ist die Vertiefung **nicht optional** — der Skill verlangt mindestens **eine**
Methode, bevor das Artefakt als `done` markiert wird. Gates sind:
- PRD: Erfolgsmetriken, funktionale Requirements (mind. eine Edge-Case-Jagd).
- Architektur: jede ADR mit Trade-off-Begründung (mind. eine Red-Team- oder Pre-Mortem-Runde).
- Epics/Stories: Akzeptanzkriterien vor dem Readiness-Gate.

Diese Pflicht-Gates holen bewusst die in BMAD v6 verloren gegangene erzwungene Elicitation aus v4 zurück.
