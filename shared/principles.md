# ESC — Leitprinzipien

Diese Prinzipien gelten für alle ESC-Skills. Sie sind die Haltung hinter dem Prozess.

## 1. Spec vor Code
Erst entscheiden WAS und WARUM, dann WIE, dann erst Code. Jede Phase erzeugt ein Artefakt, das die
nächste speist. Code ist die letzte, nicht die erste Aktivität.

## 2. Specs sind Guardrails für die KI
Specs existieren, um der KI-Implementierung **klare Grenzen** zu setzen: was gebaut wird, was nicht
(Non-Goals), welche Regeln gelten (Constitution), wann es fertig ist (EARS-Akzeptanzkriterien).
Eine gute Spec lässt keinen Raum für Halluzination oder Scope-Creep.

## 3. WAS vor WIE
`esc:discover` und `esc:prd` beschreiben Problem, Nutzer, Anforderungen — **ohne** Technologie.
Technologieentscheidungen fallen bewusst erst in `esc:architecture`. Dieselbe Spec könnte mit
verschiedenen Stacks umgesetzt werden.

## 4. Testbar oder es zählt nicht
Anforderungen und Akzeptanzkriterien in EARS-Notation (`shared/ears-guide.md`). Vage Aussagen
(„schnell", „benutzerfreundlich") werden zurückgewiesen und in messbare Form gebracht.

## 5. Begründungen festhalten (gegen den v6-Fehler)
Jede wichtige Entscheidung wird mit **Trade-offs und verworfenen Alternativen** ins Decision-Log
geschrieben. Bei Technologie immer 2–3 Optionen mit Pro/Contra zeigen, bevor empfohlen wird.

## 6. Kritisch hinterfragen ist Pflicht, nicht Kür
An definierten Gates ist die Vertiefung (Pre-Mortem, Red-Team, Edge-Case-Jagd …) verpflichtend.
Bequemes Durchwinken ist nicht vorgesehen. Siehe `shared/elicitation.md`.

## 7. Single Source of Truth auf der Platte
Der Zustand lebt in `esc/`, nicht im Chatverlauf. Jeder Skill liest und schreibt diese Dateien,
sodass die Arbeit pausier-, fortsetz- und übergebbar ist.

## 8. Just-in-Time-Kontext
Es wird nur geladen/erzeugt, was der aktuelle Schritt braucht. Story-Kontext entsteht pro Story zum
Zeitpunkt der Umsetzung, nicht alles vorab.

## 9. Right Altitude
Specs sind weder Pseudo-Code (zu detailliert, verwischt Spec/Code-Grenze) noch vage Wünsche.
Präzise definieren, was zählt — den Rest dem Urteil der KI überlassen.

## 10. Verifikation statt Behauptung
Kein „fertig" ohne Beleg: Tests existieren und laufen, Build ist grün, Akzeptanzkriterien erfüllt.
Niemals über Tests oder Status lügen.
