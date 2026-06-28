---
name: sources
description: Registriert und synchronisiert externe GitHub/GitLab-Repos als bindende Quellen der Wahrheit für inhaltliche Vorgaben (SOPs, Arbeitsanweisungen, Geräte-/Standort-Specs, Vorschriften). Klont sie flach in einen gitignorierten Cache und pflegt eine Registry, die Specs und Review einhalten müssen. Use when the user says "externe Quelle", "SOP/Arbeitsanweisung anbinden", "Repo als Quelle", "esc sources", or wants specs grounded in an external content repo.
argument-hint: "[add|list|sync|remove] [repo-url]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion, WebFetch
---

# esc:sources — Externe Quellen der Wahrheit (bindend)

Ziel: inhaltliche Vorgaben aus anderen Repos (SOPs, Arbeitsanweisungen, Geräte-/Standort-Details,
Vorschriften) **verbindlich** in ESC einbinden — registriert, gepinnt, zitierbar. Das externe Repo
bleibt die Quelle; ESC verlinkt und cached es, einverleibt es nicht.

**Verbindlichkeit:** Alle registrierten Quellen sind **bindend** — Specs und Umsetzung MÜSSEN sie
einhalten; Abweichungen sind **Blocker** im Review (`esc:review` prüft das).

## Lies zuerst
- `esc/specs/sources.md` (Registry, falls vorhanden), `esc/state.yaml`

## Aktion aus `$ARGUMENTS` (sonst per Auswahl erfragen): add · list · sync · remove

### add — Quelle registrieren
1. Erfrage: **Repo-URL** (GitHub/GitLab), **Ref zum Pinnen** (Branch/Tag/Commit — für „Quelle der
   Wahrheit" wichtig), **relevante Pfade/Globs** (welche Dokumente zählen), kurzes **Label** + **Warum**.
2. Stelle sicher, dass der Cache **gitignored** ist: `esc/.cache/` in die `.gitignore` des Produkt-Roots
   aufnehmen (anlegen, falls keine existiert).
3. **Flach klonen** in den Cache:
   `git clone --depth 1 --branch <ref> <url> esc/.cache/sources/<slug>`
   (bei sehr großen Repos optional sparse-checkout auf die relevanten Pfade; bei Commit-Pin danach
   `git fetch --depth 1 origin <commit> && git checkout <commit>`).
   Schlägt es fehl (privat/keine Auth): Nutzer bitten, sich zu authentifizieren (`gh auth login` /
   `glab auth login` / git-Credentials) und erneut versuchen. Niemals Tokens in Dateien schreiben.
4. In `esc/specs/sources.md` eintragen (Tabelle, siehe unten). Entscheidung ins `decisions`-Log.

### list — Registry zeigen
`esc/specs/sources.md` zusammenfassen: je Quelle ID, Label, Repo, Pin, Pfade, Cache-Status (geklont?).

### sync — Cache aktualisieren
Je Quelle `git -C esc/.cache/sources/<slug> fetch` + auf den gepinnten Ref bringen. **Hat sich der
Upstream über den Pin hinaus geändert** (neuer Commit auf dem Branch), melde das deutlich und schlage
**`esc:correct-course`** vor — geänderte bindende Quellen sind ein Korrektur-Anlass.

### remove — Quelle entfernen
Registry-Eintrag + Cache-Ordner entfernen (nach Rückfrage).

## Registry-Format (`esc/specs/sources.md`)
```markdown
# Quellen der Wahrheit (extern, BINDEND)

Diese Quellen sind verbindlich: Specs und Umsetzung MÜSSEN sie einhalten; Abweichungen sind Blocker im
Review. Inhalte liegen im Cache `esc/.cache/sources/` (gitignored); beim Zitieren mit Pfad/Abschnitt referenzieren.

| ID | Label | Repo | Pin (Ref) | Relevante Pfade | Cache | Warum |
|----|-------|------|-----------|------------------|-------|-------|
| S-001 | SOP Wareneingang | github.com/org/sops | v2024.3 | docs/wareneingang.md | esc/.cache/sources/sops | Compliance-Pflicht |
```

## Nutzung durch andere Phasen
- `discover`/`prd`/`architecture`/`story` lesen die relevanten gecachten Quell-Dokumente und **zitieren**
  sie in den Specs (`Quelle: <repo>/<pfad>#<abschnitt>`) — Traceability.
- `review` prüft die Umsetzung gegen die bindenden Quellen; Verstöße sind Blocker.
- `bind` nimmt `sources.md` in die CLAUDE.md auf, damit der Dev-Agent die Quellen kennt.

## Definition of Done
- [ ] `esc/specs/sources.md` aktuell; Cache geklont und auf den Pin gebracht; `esc/.cache/` ist gitignored.
- [ ] Jede Quelle hat Pin, relevante Pfade und Begründung; keine Secrets in Dateien.
