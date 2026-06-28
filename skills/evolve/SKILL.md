---
name: evolve
description: Erarbeitet nach einem fertigen Stand neue Features für ein bestehendes ESC-Produkt — analysiert Produkt, Doku und Code, brainstormt kritisch Feature-Ideen (inkl. Inspiration aus bestehenden kommerziellen Produkten: was der Nutzer mag und eigene Vorschläge der KI mit Begründung), priorisiert sie und legt die ausgewählten direkt als neue Epics und Stories an. Use when the user says "neue Features", "was als Nächstes bauen", "Produkt weiterentwickeln", "esc evolve", or is done with the current scope and wants the next iteration.
argument-hint: "[optional: Richtung/Thema]"
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, WebSearch, WebFetch
---

# esc:evolve — Neue Features erarbeiten

Ziel: aus dem aktuellen, fertigen Stand die **nächste Iteration** entwickeln — neue Features kritisch
erarbeiten, priorisieren und als Epics/Stories in die Pipeline einspeisen. Kein Code hier; dies ist
Discovery + Planung für die Weiterentwicklung.

## Sichtweise & Schärfe
Geführt aus **analytischer** und **Fokus-Sicht** (Bedarf vs. bewusster Verzicht); an Gates greift die
**skeptische Sicht** an (`${CLAUDE_PLUGIN_ROOT}/shared/viewpoints.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/intensity.md`). Abschnitt für Abschnitt (`${CLAUDE_PLUGIN_ROOT}/shared/coauthoring.md`).

## Lies zuerst
- `${CLAUDE_PLUGIN_ROOT}/shared/elicitation.md`, `${CLAUDE_PLUGIN_ROOT}/shared/coauthoring.md`
- `esc/state.yaml`, `esc/docs/prd.md`, `esc/docs/requirements/`, `esc/docs/architecture/`, `esc/docs/epics.md`, `esc/docs/constitution.md`
- Den **tatsächlichen Code** (Glob/Grep) — was existiert bereits, was sind die Lücken?

## Vorbedingung
`esc/state.yaml` muss existieren und ein Grundprodukt sollte stehen (Stories überwiegend `done`). Sonst
auf die reguläre Pipeline (`esc:status`) verweisen.

## Ablauf

### 1. Standortbestimmung
Fasse zusammen: Was kann das Produkt heute (aus Doku + Code), was waren die Non-Goals, wo sind sichtbare
Lücken/Schmerzpunkte? Lass den Nutzer bestätigen/ergänzen.

### 2. Feature-Ideen sammeln
Erarbeite Kandidaten aus mehreren Quellen: offene Annahmen/Risiken aus dem PRD, frühere Non-Goals, die
jetzt dran sein könnten, Nutzer-Schmerzpunkte, naheliegende Erweiterungen. `$ARGUMENTS` als Richtung
nutzen, falls gegeben.

**Inspiration & Wettbewerb** (nach `${CLAUDE_PLUGIN_ROOT}/shared/inspiration.md`, beidseitig):
1. **Frag den Nutzer**, welche Produkte/Apps er mag und *warum* — welche Features/Flows er sich für unser
   Produkt wünscht; destilliere den Bedarf dahinter.
2. **Schlage zusätzlich selbst** relevante (kommerzielle) Produkte vor und sage je konkret, *was* du
   übernehmen würdest, *warum* (Bezug zu unseren Nutzern/Zielen), *wie* angepasst — und *was bewusst nicht*.
   Bei Bedarf via WebSearch aktuellen Stand prüfen.

**Skeptische Sicht:** Für jede Idee fragen „Löst das ein echtes Problem? Wer will das wirklich? Kopieren
wir Oberfläche statt Bedarf?" — Passung zu Zielgruppe/Zielen/Constitution prüfen, nicht blind übernehmen.

### 3. Priorisieren — GATE
Bewerte die Ideen entlang Wert · Aufwand · Risiko · Abhängigkeiten (z. B. als Auswahl/Matrix). Schärfe
mit einer Vertiefungs-Methode (Pre-Mortem/Annahmen-Audit je Level). Der Nutzer wählt, was in diese
Iteration geht.

### 4. Größe je Feature klären
Pro gewähltem Feature grob einstufen (analog Level): Reicht es als Story/Epic, oder braucht es erst
eigenes Requirements-/Architektur-Update? Bei großem Feature auf `esc:prd`/`esc:architecture` für ein
gezieltes Delta verweisen, statt es zu unterschätzen.

### 5. Als Epics/Stories anlegen
Für die ausgewählten Features:
- neues/erweitertes Epic in `esc/docs/epics.md` mit Zielen,
- Stories mit testbaren Akzeptanzkriterien (festes Satzmuster, `shared/requirements-syntax.md`),
- Einträge in `esc/state.yaml` unter `stories` (`status: todo`).
Betroffene Requirements in `esc/docs/requirements/functional.md` ergänzen. Entscheidungen ins `decisions`-Log.

### 6. Routen
state.yaml `phase: deliver`. Tracker & Doku aktualisieren. Schlage `esc:story <id>` für die erste neue
Story vor.

## Definition of Done
- [ ] Feature-Ideen sind kritisch geprüft (echtes Problem, Wert vs. Aufwand), nicht nur gesammelt.
- [ ] Ausgewählte Features als Epics/Stories mit testbaren Akzeptanzkriterien angelegt und in state.yaml registriert.
- [ ] Große Features auf ein PRD-/Architektur-Delta verwiesen statt unterschätzt.
- [ ] Tracker & Doku (`esc:track`, `esc:docs`) aktualisiert.
