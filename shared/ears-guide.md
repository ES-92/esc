# EARS — Easy Approach to Requirements Syntax

EARS (Rolls-Royce, Mavin et al. 2009) macht Anforderungen **eindeutig und testbar**, indem es sie
in feste Satzmuster zwingt. ESC nutzt EARS für funktionale Requirements (im PRD) und für
Akzeptanzkriterien (in Stories). Für Mensch UND KI leicht zu parsen und 1:1 in Testfälle überführbar.

## Grundregel
- Verb **MUSS** (verbindlich) statt „sollte" (Empfehlung). Genau **eine** prüfbare Reaktion pro Requirement.
- Feste Klausel-Reihenfolge: Vorbedingung → Auslöser → System → Reaktion.

## Die 5 Muster (+ komplex)

| Muster | Schlüsselwort | Schablone | Beispiel |
|---|---|---|---|
| **Ubiquitär** | (keins) | Das `<System>` **MUSS** `<Reaktion>`. | Das System **MUSS** alle Passwörter mit bcrypt hashen. |
| **Ereignis** | **WENN** | **WENN** `<Auslöser>`, **MUSS** das `<System>` `<Reaktion>`. | **WENN** ein Nutzer auf „Speichern" klickt, **MUSS** das System die Eingaben validieren. |
| **Zustand** | **SOLANGE** | **SOLANGE** `<Zustand>`, **MUSS** das `<System>` `<Reaktion>`. | **SOLANGE** kein Nutzer angemeldet ist, **MUSS** das System nur die Login-Seite anzeigen. |
| **Unerwünscht** | **FALLS … DANN** | **FALLS** `<unerwünschte Bedingung>`, **DANN MUSS** das `<System>` `<Reaktion>`. | **FALLS** die Zahlung fehlschlägt, **DANN MUSS** das System eine verständliche Fehlermeldung zeigen und den Warenkorb erhalten. |
| **Optional** | **WO** | **WO** `<Feature vorhanden>`, **MUSS** das `<System>` `<Reaktion>`. | **WO** Zwei-Faktor-Auth aktiviert ist, **MUSS** das System nach dem Passwort einen Code abfragen. |
| **Komplex** | SOLANGE+WENN | **SOLANGE** `<Zustand>`, **WENN** `<Auslöser>`, **MUSS** das `<System>` `<Reaktion>`. | **SOLANGE** der Nutzer Premium ist, **WENN** ein Export gestartet wird, **MUSS** das System das PDF ohne Wasserzeichen erzeugen. |

## Qualitäts-Checkliste je Requirement
- [ ] Genau **ein** „MUSS" und **eine** Reaktion (sonst aufteilen).
- [ ] Auslöser/Bedingung explizit (kein implizites „normalerweise").
- [ ] Reaktion **beobachtbar/testbar** (kein „benutzerfreundlich", „schnell" ohne Schwelle).
- [ ] Messbare Schwellen, wo nötig (z. B. „innerhalb von 200 ms", „bis zu 10 MB").
- [ ] Frei von Implementierungsdetails (WAS, nicht WIE) — außer es ist eine bewusste Vorgabe.

## Anti-Beispiele → Korrektur
- ✗ „Die Suche soll schnell sein." → ✓ „**WENN** ein Nutzer eine Suche absendet, **MUSS** das System die ersten Ergebnisse innerhalb von 500 ms anzeigen."
- ✗ „Fehler werden behandelt." → ✓ „**FALLS** die API einen 5xx-Fehler liefert, **DANN MUSS** das System bis zu 3-mal mit Backoff erneut versuchen und danach eine Fehlermeldung zeigen."
