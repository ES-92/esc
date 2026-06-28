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

### 3. Varianten erzeugen (3–4 je Screen)
Erzeuge **eigenständige Single-File-HTML** (inline CSS/JS, **kein Build**, kein npm) je Variante:
`esc/docs/mockups/<screen-slug>/variant-1.html` … `variant-4.html`.
- Die Varianten müssen sich **konzeptionell** unterscheiden (Layout, Informationshierarchie,
  Interaktionsmuster) — nicht nur in der Farbe.
- Realistische Beispieldaten; die wichtigsten **Zustände** sichtbar oder umschaltbar (leer/lädt/fehler);
  responsives Grundgerüst.
- Für Stil-Fidelity nur bei Bedarf + Netz CDN nutzen (z. B. Tailwind Play CDN, Google Fonts); sonst plain CSS.
- Lege je Screen eine kleine Übersicht `index.html` an, die die Varianten verlinkt (zum schnellen Vergleich).

### 4. Live-Preview (Static-Server, Port erfragen)
Wie `shared/viewer.md`: lokalen Server starten, **Port immer explizit erfragen** und auf frei prüfen:
`python3 -m http.server <PORT> --directory esc` (Hintergrund). Gib dem Nutzer die URLs:
`http://localhost:<PORT>/docs/mockups/<screen-slug>/` (Übersicht) bzw. `/variant-N.html`.
Lifecycle ehrlich: Server **starten**, nicht babysitten — Stopp-Hinweis nennen. Bei Änderungen Seite neu laden.

### 5. Auswählen (kritisch)
Pro Screen wählt der Nutzer eine Variante (AskUserQuestion). Die **skeptische Sicht** greift an: Passt es
zum *Bedarf* (nicht nur „sieht cool aus")? Zustände/Fehlerpfade abgedeckt? Barrierefreiheit & Responsive
ehrlich geprüft (Tastatur, Fokus, Kontrast)? Freie Anpassungswünsche aufnehmen und einarbeiten.

### 6. Optionaler Polish-Pass
Wenn nicht schon „Volle Fidelity" und gewünscht: auf die **gewählte** Variante einen Stil-Pass —
Farbton/Palette, Typo, Effekte (Auswahl an Paletten/Stilrichtungen anbieten). Weiterhin Single-File.

### 7. In die Spec destillieren + archivieren
- Gewählte Richtung in `esc/specs/ux-spec.md` festhalten: Layout, Komponenten, Verhalten, Zustände als
  Text — **plus Verweis** auf das gewählte Mockup (markiert als „visuelle Referenz, kein bindender Code").
- **Verworfene** Varianten nach `esc/docs/mockups/_archiv/<screen-slug>/` verschieben (Referenz, klar abgelegt).
- Die gewählte Variante bleibt unter `esc/docs/mockups/<screen-slug>/`.

## Regeln
- Single-file, self-contained, kein npm/Build, keine Server-Logik in den Mockups.
- Schlüssel-Screens zuerst; Umfang nur auf Nachfrage ausweiten (Token-Bewusstsein).
- Mockups widersprechen nie den Specs; Widersprüche ansprechen, nicht still glätten.
- Am Ende ist die **ux-spec.md** vollständig — auch ohne dass jemand die Mockups öffnet.
