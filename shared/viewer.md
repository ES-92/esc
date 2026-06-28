# ESC — Doku-Viewer (optional, docsify)

ESC kann die `esc/`-Doku als kleine, lokale **Website** servieren — auf Basis von **docsify**:
zero-build, **kein** `node_modules`, eine `index.html` rendert die vorhandenen Markdown- und
Mermaid-Dateien live. Bewusst leichtgewichtig statt eines schweren Doku-Portals.

Angeboten wird der Viewer **opt-in** an zwei Stellen: bei `esc:init` (als Option) und bei `esc:docs`
(falls noch kein Viewer existiert). Nie ungefragt aufsetzen.

## Was wird angelegt
Alle Dateien liegen unter `esc/` (das Produkt-Root bleibt sauber). Statik, mitcommitbar:

```
esc/
├── viewer/
│   └── index.html       # docsify-Entry (CDN, kein Build)
├── _sidebar.md          # Navigation (aus der Datei-Struktur generiert)
└── .nojekyll            # verhindert _-Ordner-Filterung bei GitHub Pages
```

Inhalt (specs/ + docs/) wird **nicht** kopiert oder umstrukturiert — docsify liest die vorhandenen
Dateien direkt.

## index.html
Kopiere `${CLAUDE_PLUGIN_ROOT}/shared/templates/docsify-index.html` nach `esc/viewer/index.html` und
ersetze `<PROJEKT>` durch den Projektnamen aus `state.yaml`. Kernkonfig: `basePath: '/'` (Server-Root =
`esc/`), `homepage: 'docs/DOCUMENTATION.md'`, `loadSidebar: true`, Mermaid- und Such-Plugin via CDN.

## _sidebar.md generieren
Erzeuge `esc/_sidebar.md` aus den vorhandenen Dateien (Links relativ zu `esc/`). Vorlage:

```markdown
- Überblick
  - [Dokumentation](docs/DOCUMENTATION.md)
  - [Tracker](docs/TRACKER.md)
- Spezifikation
  - [Constitution](specs/constitution.md)
  - [Product Brief](specs/product-brief.md)
  - [PRD](specs/prd.md)
  - [Functional Requirements](specs/requirements/functional.md)
  - [Non-Functional Requirements](specs/requirements/non-functional.md)
  - [UX-Spec](specs/ux-spec.md)
  - [Architektur](specs/architecture/architecture.md)
  - [Epics](specs/epics.md)
- Stories
  - [<id> — <titel>](specs/stories/<datei>.md)
```
Nur Einträge für tatsächlich existierende Dateien aufnehmen; Stories aus `state.yaml`/`stories/` ableiten.

## Servieren — Port IMMER explizit erfragen
1. **Frag den Nutzer nach dem Port** (kein Default, kein Zufallsvorschlag) — als Auswahl mit Freitext-Option.
2. **Prüfe, ob der Port frei ist** (z. B. `python3 -c "import socket; s=socket.socket(); exit(0 if s.connect_ex(('127.0.0.1', PORT)) else 1)"` — Exit 0 = frei). Ist er belegt, sag es und frag erneut.
3. **Starte den statischen Server im Hintergrund** (Bash, run_in_background):
   `python3 -m http.server <PORT> --directory esc`
4. Gib dem Nutzer die **URL**: `http://localhost:<PORT>/viewer/` und den **Stopp-Hinweis**.

Alternative, falls Node bevorzugt: `npx serve esc -l <PORT>` (lädt serve bei Bedarf). Default ist `python3`.

## Lifecycle — ehrlich
Der Skill **startet** den Server, **babysittet** ihn aber nicht. Sag dem Nutzer klar:
- läuft als Hintergrundprozess auf Port `<PORT>`,
- **Stoppen:** den Prozess beenden (z. B. `pkill -f "http.server <PORT>"` oder das Terminal/den Job schließen),
- bei Code-/Doku-Änderungen einfach die Browser-Seite neu laden (docsify liest live).

## Wann was tun
- **Kein Viewer vorhanden + Nutzer will einen:** index.html + _sidebar.md + .nojekyll anlegen, dann servieren.
- **Viewer vorhanden:** `_sidebar.md` bei neuen Dateien aktualisieren; auf Wunsch (mit Port-Frage) servieren.
- **Mermaid rendert nicht:** prüfen, ob das Mermaid-Plugin im `index.html` geladen wird; ggf. Plugin-Variante tauschen.
