# ESC — Inspiration & Wettbewerb (kritisch)

Gute Produkte entstehen nicht im luftleeren Raum. ESC zieht in **Analyse** (`discover`) und bei **neuen
Features** (`evolve`) bewusst Inspiration aus bestehenden, oft kommerziellen Produkten — **kritisch**,
nie als blindes Kopieren. Es läuft in **zwei Richtungen**: vom Nutzer eingebracht *und* von der KI
aktiv vorgeschlagen.

## Die zwei Richtungen

### A) Nutzer-getrieben — „was magst du und warum?"
Frag den Nutzer offen: **Welche Produkte/Apps magst du** (auch aus anderen Domänen)? **Was genau** daran
(ein Feature, ein Flow, die Haptik/Tonalität, ein Geschäftsmodell, eine Detaillösung)? **Warum** gefällt
es dir? Für jeden Punkt destilliert die KI den **dahinterliegenden Bedarf** und prüft, ob und wie er sich
auf *dieses* Projekt übertragen lässt.

### B) KI-getrieben — proaktive Vorschläge
Danach schlägt die KI **zusätzlich von sich aus** 2–5 relevante (kommerzielle) Produkte/Anwendungen vor —
auch aus angrenzenden Branchen — und sagt je konkret: **was** sie davon übernehmen würde, **warum** (Bezug
zu unserem Problem/Nutzer), **wie** angepasst — *und* **was sie bewusst nicht** übernehmen würde
(Anti-Pattern, schlechter Fit). Bei Bedarf via WebSearch/WebFetch den aktuellen Stand prüfen.

## Kritische Regeln (skeptische Sicht greift an)
- **Bedarf statt Oberfläche.** Nicht das sichtbare Feature kopieren, sondern den Job-to-be-done dahinter
  verstehen und für uns neu lösen. „Gefällt mir" ≠ „passt zu uns".
- **An uns rückbinden.** Jede Übernahme muss zu *unserer* Zielgruppe, *unseren* Zielen und der
  *Constitution* passen — sonst raus. Begründung explizit machen.
- **Verzicht benennen.** Was wir bewusst *nicht* übernehmen (und warum) gehört dazu → speist Non-Goals.
- **Anti-Patterns lernen.** Auch Fehler/Schwächen anderer Produkte erfassen, um sie zu vermeiden.
- **Keine Plagiate.** Inspiration ja, 1:1-Klon (Marke, geschützte Inhalte) nein.

## Ablauf
1. **Sammeln (A):** Nutzer nennt Produkte + was + warum (Auswahl/offen, sofort festhalten).
2. **Destillieren:** je Punkt → Bedarf dahinter, Übertragbarkeit auf uns, kritische Passungsprüfung.
3. **Vorschlagen (B):** KI nennt 2–5 weitere Produkte mit „übernehmen / warum / wie / nicht übernehmen".
4. **Entscheiden:** Nutzer wählt, was übernommen wird (Auswahl). Übernahmen + Begründung sowie bewusste
   Verzichte festhalten; Entscheidungen ins `decisions`-Log.

## Output-Abschnitt „Inspiration & Wettbewerb"
Als Abschnitt im Product Brief (bzw. in der `evolve`-Feature-Analyse):

```markdown
## Inspiration & Wettbewerb

| Quelle (Produkt) | Was übernehmen | Warum (Bezug zu uns) | Anpassung |
|---|---|---|---|
| <Produkt> | <Feature/Flow/Prinzip> | <Bedarf, Passung zu Ziel/Nutzer> | <wie für uns> |

**Bewusst NICHT übernommen:** <Produkt/Feature> — weil <Grund> (→ Non-Goal).
**Vermiedene Anti-Patterns:** <was andere falsch machen> — wir lösen es durch <…>.
```
