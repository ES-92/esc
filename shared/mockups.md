# ESC — Visuelle UX-Erarbeitung (Mockups, optional)

Ein **intensiver, visueller** Weg, die UX zu erarbeiten: pro Schlüssel-Screen **3–4 HTML/CSS/JS-Mockup-
Varianten** zum Auswählen, mit **Live-Preview im Browser**. Bewusst **token-intensiver** — daher
**opt-in** (der `ux`-Skill fragt vorher). Der Standard-Weg bleibt rein textbasiert.

## Eisernes Prinzip: Mockup ≠ Spec
Mockups sind **abgeleitete Exploration**, nicht die Spezifikation. Sie leben in `esc/docs/mockups/`
(abgeleitet, nicht von Hand zu pflegen). Die **`esc/specs/ux-spec.md` bleibt die Quelle der Wahrheit**.
Nach der Auswahl wird die gewählte Richtung **in die Spec destilliert**. Ein Mockup ist **visuelle
Referenz, kein Implementierungs-Vertrag** — der Dev folgt weiter Specs + Constitution + Architektur.

## Grundlage
Alle Mockups gründen auf den **vorhandenen Specs**: PRD-Requirements & Zustände, Constitution
(inkl. evtl. gesetzter Marke/Farbwelt), Screen-Inventar aus der UX-Phase. Nichts erfinden, was den Specs
widerspricht.

## Ablauf

### 1. Schlüssel-Screens bestimmen
Wähle mit dem Nutzer die **1–3 wichtigsten** Screens/Flows. Mockups dafür erstellen; danach **fragen**,
ob weitere Screens ebenfalls visuell erarbeitet werden sollen (nicht ungefragt alles durchmocken).

### 2. Fidelity-Modus erfragen (Auswahl)
Pro Lauf den Nutzer wählen lassen:
- **Wireframe** — Graustufen, nur Anordnung & Flow, kein visuelles Design (am günstigsten).
- **Struktur zuerst** — schlicht, Layout & Interaktion; Farbe/Effekte später als optionaler Polish-Pass.
- **Volle Fidelity** — sofort mit Farbton, Typografie und Effekten (beeindruckend, aber teurer).

### 2a. Design-Lesart & Dials (design-taste, gegen generisches Aussehen)
Bevor du Pixel setzt, **lies den Brief** und gib **einen** Einzeiler aus:
> „Lese das als: <Seitentyp> für <Zielgruppe>, mit <Vibe>-Sprache, Richtung <Design-System/Ästhetik>."

Setze drei **Dials** (aus dem Brief; bei Produkt-UI/Trust-first konservativ): `DESIGN_VARIANZ` (Symmetrie ↔
Chaos), `BEWEGUNG` (statisch ↔ cinematisch), `DICHTE` (luftig ↔ vollgepackt). Sie steuern Layout/Motion/Dichte.

**Echte Design-Systeme statt nachbauen:** liest der Brief als bekanntes System (Fluent, Material 3, Carbon,
Polaris, Primer, GOV.UK/USWDS, Radix, shadcn, Tailwind …), nutze das **offizielle Paket** und baue sein CSS
nicht von Hand nach; **ein** System pro Projekt. Ist es nur eine *Ästhetik* (Glassmorphism, Bento, Editorial,
Brutalism …), ehrlich mit nativem CSS/Tailwind bauen und im Kommentar kennzeichnen.

**Anti-Default-Disziplin (nicht reflexartig):** keine KI-Lila-Verläufe, kein zentrierter Hero über dunklem
Mesh, keine drei gleichen Feature-Cards, kein generisches Glassmorphism überall, kein Inter + slate-900 als
Reflex. Bewusst darüber hinausgehen — passend zur Design-Lesart.

### 3. Varianten erzeugen (3–4 je Screen)
Erzeuge **eigenständige Single-File-HTML** (inline CSS/JS, **kein Build**, kein npm) je Variante:
`esc/docs/mockups/<screen-slug>/variant-1.html` … `variant-4.html`.
- Die Varianten müssen sich **konzeptionell** unterscheiden (Layout, Informationshierarchie,
  Interaktionsmuster) — nicht nur in der Farbe.
- Realistische Beispieldaten; die wichtigsten **Zustände** sichtbar oder umschaltbar (leer/lädt/fehler);
  responsives Grundgerüst.
- Für Stil-Fidelity nur bei Bedarf + Netz CDN nutzen (z. B. Tailwind Play CDN, Google Fonts); sonst plain CSS.
- Erzeuge **eine einzige Galerie-Seite** `esc/docs/mockups/index.html`, die **alle** Varianten **aller**
  bearbeiteten Screens auf *einer* Seite zeigt — je Variante ein `<iframe src="<screen-slug>/variant-N.html">`
  mit Beschriftung, gruppiert pro Screen (z. B. horizontal scrollbare Reihe je Screen). Alles auf einen Blick,
  keine Einzel-URLs. Die `variant-N.html` bleiben eigenständig (fürs Archiv); die Galerie bettet sie nur ein.

### 4. Live-Preview (Static-Server, Port erfragen, Auto-Stop)
Wie `shared/viewer.md`: **Port immer explizit erfragen** und auf frei prüfen. Server **im Hintergrund**
starten und die **PID merken** (`python3 -m http.server <PORT> --directory esc`). Der primäre Stopp ist
das explizite Killen der PID am Ende (Schritt 7). Zusätzlich einen **portablen Watchdog** als Sicherheitsnetz
setzen (kein `timeout` — fehlt auf macOS): `( sleep 1800; kill <PID> 2>/dev/null ) &`.
Gib dem Nutzer **eine** URL: `http://localhost:<PORT>/docs/mockups/` (die Galerie mit allen Varianten).
Bei Änderungen genügt Seite neu laden. Der Server wird **am Ende automatisch beendet** (Schritt 7).

### 5. Auswählen (kritisch)
Pro Screen wählt der Nutzer eine Variante (AskUserQuestion). Die **skeptische Sicht** greift an: Passt es
zum *Bedarf* (nicht nur „sieht cool aus")? Zustände/Fehlerpfade abgedeckt? Barrierefreiheit & Responsive
ehrlich geprüft (Tastatur, Fokus, Kontrast)? Freie Anpassungswünsche aufnehmen und einarbeiten.

### 6. Optionaler Polish-Pass
Wenn nicht schon „Volle Fidelity" und gewünscht: auf die **gewählte** Variante einen Stil-Pass —
Farbton/Palette, Typo, Effekte (Auswahl an Paletten/Stilrichtungen anbieten). Weiterhin Single-File.

### 7. In die Spec destillieren, archivieren, Server beenden
- Gewählte Richtung in `esc/specs/ux-spec.md` festhalten: Layout, Komponenten, Verhalten, Zustände als
  Text — **plus Verweis** auf das gewählte Mockup (markiert als „visuelle Referenz, kein bindender Code").
- **Verworfene** Varianten nach `esc/docs/mockups/_archiv/<screen-slug>/` verschieben (Referenz, klar abgelegt).
- Die gewählte Variante bleibt unter `esc/docs/mockups/<screen-slug>/`.
- **Server automatisch beenden:** die in Schritt 4 gemerkte PID killen (z. B. `kill <PID>` bzw.
  `pkill -f "http.server <PORT>"`), kurz „Preview-Server beendet" bestätigen. Nicht laufen lassen.

## Regeln
- Single-file, self-contained, kein npm/Build, keine Server-Logik in den Mockups.
- **Eine** Galerie-Seite für alle Mockups; Preview-Server mit Auto-Stop (Timeout + am Ende PID killen), nie dauerhaft laufen lassen.
- Schlüssel-Screens zuerst; Umfang nur auf Nachfrage ausweiten (Token-Bewusstsein).
- Mockups widersprechen nie den Specs; Widersprüche ansprechen, nicht still glätten.
- Am Ende ist die **ux-spec.md** vollständig — auch ohne dass jemand die Mockups öffnet.
