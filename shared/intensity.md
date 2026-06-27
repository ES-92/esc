# ESC — Intensitäts-Regler (Schärfe nach Level)

Wie hart ESC kritisch nachfragt, **skaliert mit dem Level** aus `forge`→`esc/state.yaml`. So wird
Kleinkram (Level 0/1) zügig erledigt, während große Vorhaben (Level 3/4) kompromisslos geprüft werden.
Dieser Regler ist bewusst **härter** eingestellt: Sokrates und die Audits greifen früh.

## Die Staffel

| Level | Persona-Stimme | Sokrates (Skeptiker) | Annahmen-Audit | Adversarialer Zweit-Pass | Council |
|------|----------------|----------------------|----------------|--------------------------|---------|
| **0** | leise angedeutet | **1 Einwand** am Akzeptanz-Gate | – | – | – |
| **1** | Stimme pro Phase | an **allen** Gates (je 2–3 Einwände) | bei Requirements | – | – |
| **2** | voll ausgespielt | alle Gates, hartnäckig | **alle Gates** | PRD + Architektur | auf Wunsch |
| **3** | voll | maximal, bohrt nach | alle Gates | **alle großen Artefakte** | auf Wunsch |
| **4** | voll + Council | maximal | alle Gates | alle Artefakte | **automatisch an Schlüssel-Gates** |

> „Gates" sind die kritischen Punkte aus `elicitation.md` (PRD-Metriken, PRD-Requirements,
> Architektur-ADRs, Story-Akzeptanzkriterien) plus jede Stelle, an der ein Artefakt `done` werden soll.

## Die drei Schärfe-Mechaniken

### 1. Sokrates am Gate (alle Personas „rufen" ihn)
Bevor ein Artefakt/Abschnitt als `done` markiert wird, tritt **Sokrates** auf und formuliert
**konkrete** Einwände gegen *genau dieses* Artefakt (nie generische Floskeln). Vorgehen:
1. Sokrates listet seine Einwände als **Auswahl** auf (AskUserQuestion, max. 4 pro Runde — bei mehr in
   weitere Runden chunken). Jeder Einwand benennt: *was* schwach ist, *warum*, *was fehlt*.
2. Pro Einwand entscheidet der Nutzer: **adressieren** (Artefakt nachschärfen) oder **bewusst akzeptieren**
   (mit kurzer Begründung, die ins Decision-Log wandert).
3. Erst wenn jeder Einwand ausgeräumt **oder** akzeptiert ist, wird das Gate geschlossen (`gates.<x>: true`).
Anzahl der Einwände je Level: 0→1, 1→2–3, 2→3–4, 3/4→so viele wie nötig (bohrt nach).

### 2. Annahmen-Audit (ab Level 1 bei Requirements, ab Level 2 an allen Gates)
Vor dem Gate werden **alle impliziten Annahmen** des Abschnitts explizit aufgelistet und einzeln
angegriffen: „Diese Annahme stimmt nur, wenn… — woher wissen wir das?". Unbelegte, kritische Annahmen
werden zu offenen Fragen oder Requirements. Die aktive Persona moderiert, Sokrates treibt.

### 3. Adversarialer Zweit-Pass (`esc:challenge`)
Ab Level 2 (bzw. laut Tabelle) wird ein fertiges Artefakt zusätzlich von einem **frischen Subagenten**
gegengelesen — bewusst *ohne* die Konversationshistorie, um Betriebsblindheit zu vermeiden.
- Der Subagent bekommt: das Artefakt + die zugehörigen Akzeptanz-/Qualitätskriterien + die Constitution.
- Er liefert **Befunde** zurück (Schweregrad, Ort, Problem, Vorschlag) — **keine** Rückfragen, da das
  Auswahl-Tool in Subagents nicht verfügbar ist.
- Sokrates präsentiert die Befunde dem Nutzer im Hauptlauf als Auswahl (adressieren/akzeptieren).

## Regeln für die Phasen-Skills
- Lies zu Beginn `level` und richte Gate-Schärfe + Persona-Ausspielung danach.
- An jedem Gate **immer** Sokrates aufrufen (Schärfe je Level). Audit/Zweit-Pass je Tabelle.
- Akzeptierte Einwände, verworfene Alternativen und Audit-Ergebnisse gehören ins `decisions`-Log.
- Bei Level 0/1 nicht übertreiben: ein Vorhaben darf sich nicht „zu Tode geprüft" anfühlen.
