# ESC — Kritische Sichtweisen

ESC betrachtet jedes Artefakt aus mehreren **kritischen Sichtweisen**. Eine Sichtweise ist keine
Figur, sondern eine **Linse**: eine bestimmte Art, ein Ergebnis anzugreifen und zu schärfen. Jede
Phase wird primär von einer Sichtweise geführt; an den Gates greift zusätzlich die **skeptische
Sichtweise** an. Ziel ist schärferes Denken durch wechselnde Blickwinkel.

## Grundregeln
1. **Substanz vor Etikett.** Die Sichtweise ist nur nützlich, wenn sie *konkret* angreift — auf genau
   dieses Artefakt bezogen, nie mit generischen Floskeln.
2. **Kurz halten.** Ein, zwei pointierte Einwände, dann zur Sache.
3. **Intensität nach Level** (siehe `intensity.md`): bei Level 0 nur angedeutet, bei 3/4 voll ausgespielt.
4. **Verantwortung bleibt.** Eine Sichtweise darf provozieren, muss aber zu einem verwertbaren,
   korrekten Ergebnis führen.

## Die Sichtweisen

| Sichtweise | Phase | Fokus | Greift an | Leitfrage |
|---|---|---|---|---|
| **Analytisch** | `discover` | Evidenz statt Annahme | Wunschdenken, unbelegter Bedarf | „Woher *wissen* wir das? Wo sind die Daten?" |
| **Fokus** | `prd` | Prioritäten, Non-Goals, Metriken | Feature-Wildwuchs, vage Ziele | „Was bauen wir bewusst **nicht**? Woran messen wir Erfolg?" |
| **Nutzer** | `ux` | Erlebnis & Fehlerpfade | vergessene Leer-/Fehlerzustände | „Wie fühlt sich der schlechteste Moment an?" |
| **Architektur** | `architecture` | Trade-offs & Einfachheit | unnötige Komplexität, Hype ohne Grund | „Welche Annahme trägt das? Was bereuen wir in 2 Jahren?" |
| **Planung** | `epics`/`story` | Slicing & Abhängigkeiten | horizontale/zu große Stücke | „Ist das wirklich vertikal und unabhängig?" |
| **Pragmatisch** | `implement` | funktionierender, getesteter Code | fehlende Tests, Scope-Creep | „Läuft es? Beweise es mit grünen Tests." |
| **🔪 Skeptisch** | `review` + **alle Gates** | Advocatus Diaboli (zentraler Biss) | jede Schwäche, die durchrutschen will | „Und *warum* glaubst du das? Was, wenn das Gegenteil stimmt?" |
| **Prinzipien** | `init`/`status` | Guardrails & Constitution | Scope-Creep, verletzte Grenzen | „Bleibt das innerhalb unserer Regeln?" |

## Die skeptische Sichtweise (an Gates)
Bevor ein Artefakt als `done` gilt, wird es aus der **skeptischen Sichtweise** angegriffen:
**konkrete** Einwände gegen *dieses* Artefakt (Anzahl je Level, siehe `intensity.md`), jeweils mit:
*was* schwach ist, *warum*, *was fehlt*. Jeder Einwand wird **adressiert** (nachgeschärft) oder
**bewusst akzeptiert** (Begründung → Decision-Log). Erst dann schließt das Gate.

## Mehrere Sichtweisen auf Abruf
- **`esc:consult`** — eine einzelne Sichtweise auf eine Frage anlegen.
- **`esc:council`** — mehrere Sichtweisen prallen aufeinander (Mehr-Perspektiven-Runde).
- **`esc:challenge`** — skeptischer Zweit-Pass durch einen frischen, kontextlosen Subagenten.
