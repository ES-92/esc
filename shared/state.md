# ESC — State & Workspace-Konventionen

ESC hält den gesamten Prozess-Zustand auf der Platte (nicht im Kontextfenster). Die Dateien sind
die **Single Source of Truth** — ein frischer Agent kann jederzeit aus ihnen weiterarbeiten.

## Workspace-Layout (im ZIEL-Projekt, das gebaut wird)

```
esc/                          # bewusst KEIN Dot-Ordner (Dot-Ordner werden von IDE/LLM gefiltert)
├── state.yaml                # Prozess-State + Decision-Log — Single Source of Truth
├── TRACKER.md                # Mitlaufender Fortschritts-Tracker
└── docs/                     # die gesamte Produkt-Dokumentation (das Deliverable)
    ├── DOCUMENTATION.md      # lebende Doku-Übersicht (Diagramme)
    ├── constitution.md       # Nicht-verhandelbare Guardrails für die KI-Entwicklung
    ├── product-brief.md      # Phase: discover
    ├── prd.md                # Phase: prd (Überblick; bei Level 0/1 stattdessen quick-spec.md)
    ├── requirements/
    │   ├── functional.md     # FR — funktionale Anforderungen (testbar)
    │   └── non-functional.md # NFR — nicht-funktionale Anforderungen
    ├── ux-spec.md            # Phase: ux (wenn UI-relevant)
    ├── architecture/
    │   ├── architecture.md   # Phase: architecture
    │   └── decisions/        # ADRs (Architecture Decision Records)
    │       └── ADR-0001-<slug>.md
    ├── epics.md              # Phase: epics
    └── stories/
        └── <epic>.<nr>-<slug>.md
```

> Hinweise: `esc/` liegt im jeweiligen Produkt-Projekt, NICHT im ESC-Skill-Repo.
> **Prozess-State** (`state.yaml`, `TRACKER.md`) liegt direkt in `esc/`; die **Produkt-Doku**
> (Specs, FR/NFR, ADRs, Diagramme) gebündelt in `esc/docs/`.

## `esc/state.yaml` — Schema

```yaml
project: "<Projektname>"
created: "YYYY-MM-DD"        # vom Nutzer/Datum übernehmen, nie raten
level: 0                      # 0–4, von esc:init gesetzt (siehe shared/levels.md)
phase: "init"                # init|discover|prd|ux|architecture|epics|deliver|done
artifacts:
  constitution: done          # pending|done|skipped|n/a
  product_brief: n/a
  prd: pending
  ux_spec: n/a
  architecture: n/a
  epics: pending
gates:                        # Pflicht-Vertiefungen abgehakt? (siehe shared/elicitation.md)
  prd_metrics: false
  prd_requirements: false
  architecture_adrs: false
  story_acceptance: false
decisions:                    # Decision-Log — jede wichtige Entscheidung + Begründung
  - id: D-001
    date: "YYYY-MM-DD"
    topic: "Persistenz"
    decision: "PostgreSQL"
    rationale: "Relationale Daten, Team-Erfahrung, ACID nötig"
    alternatives: ["MongoDB (verworfen: keine starken Relationen nötig erwies sich als falsch)"]
stories:
  - id: "1.1"
    title: "Login-Formular"
    status: "todo"            # todo|in_progress|review|done
```

## Regeln für den Umgang mit State
1. **Vor jeder Phase** `state.yaml` lesen → `level` und `phase` prüfen, korrektes Routing wählen.
2. **Nach jedem Schritt** den passenden `artifacts`/`gates`/`stories`-Eintrag aktualisieren.
3. **Jede nicht-triviale Entscheidung** ins `decisions`-Array schreiben — mit `rationale` und
   verworfenen `alternatives`. Das ist das institutionelle Gedächtnis gegen Kontextverlust.
4. **Datumsangaben** immer vom System/Nutzer übernehmen, niemals erfinden.
5. **Nie still überspringen.** Wird eine Phase wegen Level ausgelassen, `artifacts.<x>: n/a` setzen
   und es dem Nutzer mitteilen.
