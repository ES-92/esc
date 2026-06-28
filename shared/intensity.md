# ESC — Intensitäts-Regler (Schärfe nach Level)

Wie hart ESC kritisch nachfragt, **skaliert mit dem Level** aus `esc/state.yaml`. So wird Kleinkram
(Level 0/1) zügig erledigt, während große Vorhaben (Level 3/4) kompromisslos geprüft werden.
Der Regler ist bewusst **scharf** eingestellt: die skeptische Sichtweise und die Audits greifen früh.

## Die Staffel

| Level | Sichtweisen | Skeptische Sicht | Annahmen-Audit | Skeptischer Zweit-Pass | Mehr-Perspektiven-Runde |
|------|-------------|------------------|----------------|------------------------|--------------------------|
| **0** | leise angedeutet | **1 Einwand** am Akzeptanz-Gate | – | – | – |
| **1** | je Phase | an **allen** Gates (je 2–3 Einwände) | bei Requirements | – | – |
| **2** | voll ausgespielt | alle Gates, hartnäckig | **alle Gates** | PRD + Architektur | auf Wunsch |
| **3** | voll | maximal, bohrt nach | alle Gates | **alle großen Artefakte** | auf Wunsch |
| **4** | voll + Runde | maximal | alle Gates | alle Artefakte | **automatisch an Schlüssel-Gates** |

> „Gates" sind die kritischen Punkte (PRD-Metriken, Requirements, Architektur-Entscheidungen,
> Story-Akzeptanzkriterien) plus jede Stelle, an der ein Artefakt `done` werden soll.

## Die drei Schärfe-Mechaniken

### 1. Skeptische Sichtweise am Gate
Bevor ein Artefakt/Abschnitt als `done` markiert wird, wird es aus der **skeptischen Sichtweise**
(`viewpoints.md`) angegriffen — **konkrete** Einwände gegen *genau dieses* Artefakt, nie generisch:
1. Einwände als **Auswahl** auflisten (AskUserQuestion, max. 4 pro Runde — bei mehr in Folgerunden
   chunken). Jeder Einwand benennt: *was* schwach ist, *warum*, *was fehlt*.
2. Pro Einwand entscheidet der Nutzer: **adressieren** (nachschärfen) oder **bewusst akzeptieren**
   (Begründung → `decisions`-Log).
3. Erst wenn jeder Einwand ausgeräumt **oder** akzeptiert ist, schließt das Gate (`gates.<x>: true`).
Anzahl je Level: 0→1, 1→2–3, 2→3–4, 3/4→so viele wie nötig.

### 2. Annahmen-Audit (ab Level 1 bei Requirements, ab Level 2 an allen Gates)
Vor dem Gate werden **alle impliziten Annahmen** des Abschnitts explizit aufgelistet und einzeln
angegriffen: „Diese Annahme stimmt nur, wenn… — woher wissen wir das?". Unbelegte, kritische Annahmen
werden zu offenen Fragen oder Requirements.

### 3. Skeptischer Zweit-Pass (`esc:challenge`)
Ab Level 2 (laut Tabelle) wird ein fertiges Artefakt zusätzlich von einem **frischen Subagenten**
gegengelesen — bewusst *ohne* die Konversationshistorie, gegen Betriebsblindheit:
- Input: Artefakt + zugehörige Akzeptanz-/Qualitätskriterien + Constitution.
- Output: **Befunde** (Schweregrad, Ort, Problem, Vorschlag) — **keine** Rückfragen (das Auswahl-Tool
  steht Subagenten nicht zur Verfügung).
- Die Befunde werden im Hauptlauf als Auswahl präsentiert (adressieren/akzeptieren).

## Regeln für die Phasen-Skills
- Lies zu Beginn `level` und richte Gate-Schärfe + Sichtweisen-Ausspielung danach.
- An jedem Gate **immer** die skeptische Sichtweise anlegen (Schärfe je Level). Audit/Zweit-Pass je Tabelle.
- Akzeptierte Einwände, verworfene Alternativen und Audit-Ergebnisse gehören ins `decisions`-Log.
- Bei Level 0/1 nicht übertreiben: ein Vorhaben darf sich nicht „zu Tode geprüft" anfühlen.
