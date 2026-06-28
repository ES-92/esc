# ESC — Scale-Adaptive Levels (0–4)

ESC passt die Prozess-Tiefe an die Größe des Vorhabens an. Nicht jedes Vorhaben
braucht ein PRD oder eine Architektur. `esc:init` klassifiziert einmalig und schreibt
`level` nach `esc/state.yaml`. Die folgenden Phasen blenden sich danach ein oder aus.

## Klassifizierung

| Level | Name | Umfang (Faustregel) | Beispiele |
|------|------|--------------------|-----------|
| **0** | Atomarer Change | 1 Story, < 1 Tag | Bugfix, Copy-Änderung, Config, kleiner Refactor |
| **1** | Kleines Feature | 1–10 Stories, kein Architektur-Risiko | Neues Formularfeld, Endpoint, Filter |
| **2** | Mittleres Feature | 5–15 Stories, etwas Architektur | Neuer Bounded Context, Integration, Auth-Flow |
| **3** | Komplexes System | 12–40 Stories, mehrere Subsysteme | Neues Produkt-Modul, Plattform-Fähigkeit |
| **4** | Enterprise / Produkt | 40+ Stories, mehrere Teams/Produkte | Greenfield-Produkt, Plattform |

### Erkennungs-Heuristiken (für `esc:init`)
- **Story-Anzahl** (geschätzt), **Anzahl betroffener Subsysteme**, **Neuheitsgrad** (Greenfield vs. Brownfield),
 **Architektur-Risiko** (neue Technologie/Persistenz/externe Integration?), **Reversibilität**.
- Im Zweifel **eine Stufe niedriger** wählen — Phasen lassen sich jederzeit per Opt-in nachziehen.

## Welche Phasen pro Level (Default)

| Phase \ Level | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `esc:init` (Constitution + State) | ✓ | ✓ | ✓ | ✓ | ✓ |
| `esc:discover` (Product Brief) | – | optional | ✓ | ✓ | ✓ |
| `esc:prd` (Requirements) | Quick-Spec¹ | Quick-Spec¹ | ✓ | ✓ | ✓ |
| `esc:ux` (UX-Spec) | – | wenn UI | wenn UI | wenn UI | ✓ |
| `esc:architecture` (ADRs) | – | – | leicht² | ✓ | ✓ |
| `esc:epics` (Epics & Stories) | 1 Story | ✓ | ✓ | ✓ | ✓ |
| `esc:story` + `esc:implement` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `esc:review` | ✓ | ✓ | ✓ | ✓ | ✓ |

¹ **Quick-Spec**: ein einziges schlankes Dokument (`esc/docs/quick-spec.md`) statt vollem PRD —
  Problem, Lösung, Akzeptanzkriterien (testbar), betroffene Dateien. `esc:prd` erkennt Level 0/1
  automatisch und erzeugt diese Kurzform.
² **leicht**: nur ADRs für die ein, zwei nicht-trivialen Entscheidungen, kein volles Architektur-Dokument.

## Routing-Regel
Jeder Phasen-Skill prüft zu Beginn `level` in `esc/state.yaml`. Ist die Phase für das Level
nicht vorgesehen, weist der Skill freundlich darauf hin und schlägt den nächsten sinnvollen
Schritt vor — überspringt aber nicht stillschweigend (der Nutzer kann jede Phase per Opt-in erzwingen).
