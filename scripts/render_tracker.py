#!/usr/bin/env python3
"""Rendert esc/docs/TRACKER.md deterministisch aus esc/state.yaml.

Best-effort-Helfer für ESC. Wird er nicht ausgeführt (z. B. PyYAML fehlt),
rendert der Skill den Tracker stattdessen selbst. Bricht den Workflow nie ab (Exit 0).

Aufruf:  python3 render_tracker.py [pfad/zu/esc]
Default-Pfad: ./esc
"""
import sys
import os
from datetime import date

PHASES = [
    ("init", "Init", "constitution"),
    ("discover", "Discover", "product_brief"),
    ("prd", "PRD", "prd"),
    ("ux", "UX", "ux_spec"),
    ("architecture", "Architektur", "architecture"),
    ("epics", "Epics", "epics"),
    ("deliver", "Deliver", None),
]

STATUS_ICON = {"done": "✓ done", "pending": "○ pending", "skipped": "– skipped", "n/a": "– n/a"}


def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
        return v[1:-1]
    if v in ("true", "True"):
        return True
    if v in ("false", "False"):
        return False
    if v in ("null", "~", ""):
        return None
    if v.lstrip("-").isdigit():
        return int(v)
    return v


def _load_min(text):
    """Toleranter Parser für ESCs bekanntes state.yaml-Schema (stdlib-only).
    Unterstützt: Top-Level-Skalare, ein-stufige Maps (artifacts/gates) und Listen von Maps
    (decisions/stories) mit 2-Space-Einrückung."""
    lines = [l for l in text.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    root, i = {}, 0
    n = len(lines)

    def indent(l):
        return len(l) - len(l.lstrip(" "))

    while i < n:
        line = lines[i]
        if indent(line) != 0 or ":" not in line:
            i += 1
            continue
        key, _, val = line.lstrip().partition(":")
        key = key.strip()
        val = val.strip()
        if val:
            root[key] = _scalar(val)
            i += 1
            continue
        # Block: entweder Map-Kinder oder Listen-Items
        i += 1
        if i < n and lines[i].lstrip().startswith("- "):
            items = []
            while i < n and indent(lines[i]) > 0 and lines[i].lstrip().startswith("- "):
                item_indent = indent(lines[i])
                first = lines[i].lstrip()[2:]
                d = {}
                if ":" in first:
                    k, _, v = first.partition(":")
                    d[k.strip()] = _scalar(v)
                i += 1
                while i < n and indent(lines[i]) > item_indent and ":" in lines[i]:
                    k, _, v = lines[i].lstrip().partition(":")
                    d[k.strip()] = _scalar(v)
                    i += 1
                items.append(d)
            root[key] = items
        else:
            d = {}
            while i < n and indent(lines[i]) > 0 and ":" in lines[i] and not lines[i].lstrip().startswith("- "):
                k, _, v = lines[i].lstrip().partition(":")
                d[k.strip()] = _scalar(v)
                i += 1
            root[key] = d
    return root


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "esc"
    state_path = os.path.join(base, "state.yaml")
    if not os.path.exists(state_path):
        print(f"[render_tracker] {state_path} nicht gefunden — übersprungen.")
        return 0
    try:
        with open(state_path, encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"[render_tracker] state.yaml nicht lesbar ({e}) — übersprungen.")
        return 0
    s = None
    try:
        import yaml  # type: ignore
        s = yaml.safe_load(text) or {}
    except Exception:
        try:
            s = _load_min(text) or {}
        except Exception as e:
            print(f"[render_tracker] state.yaml nicht parsebar ({e}) — Skill rendert selbst.")
            return 0

    project = s.get("project", "Unbenannt")
    level = s.get("level", "?")
    phase = s.get("phase", "?")
    artifacts = s.get("artifacts", {}) or {}
    gates = s.get("gates", {}) or {}
    decisions = s.get("decisions", []) or []
    stories = s.get("stories", []) or []

    def cls(key):
        if key == phase:
            return "active"
        st = artifacts.get(key)
        if st == "done":
            return "done"
        if st in ("n/a", "skipped"):
            return "skipped"
        return "pending"

    # Pipeline-Mermaid
    ids = [slug[:5] for slug, _, _ in PHASES]
    chain = " --> ".join(f"{slug[:5]}([{label}])" for slug, label, _ in PHASES)
    mermaid = ["```mermaid", "flowchart LR", f"  {chain}"]
    mermaid += [
        "  classDef done fill:#2e7d32,color:#fff,stroke:#1b5e20;",
        "  classDef active fill:#1565c0,color:#fff,stroke:#0d47a1;",
        "  classDef pending fill:#eceff1,color:#546e7a,stroke:#b0bec5;",
        "  classDef skipped fill:#fafafa,color:#bdbdbd,stroke:#e0e0e0,stroke-dasharray:4 3;",
    ]
    for slug, label, akey in PHASES:
        nid = slug[:5]
        c = "active" if slug == phase else cls(akey) if akey else "pending"
        mermaid.append(f"  class {nid} {c};")
    mermaid.append("```")

    # Story-Status
    counts = {"done": 0, "in_progress": 0, "review": 0, "todo": 0}
    for st in stories:
        counts[st.get("status", "todo")] = counts.get(st.get("status", "todo"), 0) + 1

    out = []
    out.append(f"# 📊 ESC Tracker — {project}")
    out.append(f"_Aktualisiert: {date.today().isoformat()} · Level {level} · Aktuelle Phase: {phase}_\n")
    out.append("## Pipeline-Fortschritt")
    out += mermaid
    out.append("\n## Artefakte\n| Artefakt | Status |\n|---|---|")
    labels = {"constitution": "Constitution", "product_brief": "Product Brief", "prd": "PRD",
              "ux_spec": "UX-Spec", "architecture": "Architektur", "epics": "Epics & Stories"}
    for k, lbl in labels.items():
        out.append(f"| {lbl} | {STATUS_ICON.get(artifacts.get(k, 'pending'), artifacts.get(k, '?'))} |")
    out.append("\n## Gates (kritische Pflicht-Vertiefung)\n| Gate | Erledigt |\n|---|---|")
    glabels = {"prd_metrics": "PRD: Erfolgsmetriken", "prd_requirements": "PRD: Requirements (Edge-Cases)",
               "architecture_adrs": "Architektur: ADRs", "story_acceptance": "Stories: Akzeptanzkriterien"}
    for k, lbl in glabels.items():
        out.append(f"| {lbl} | {'✓' if gates.get(k) else '✗'} |")
    out.append("\n## Stories")
    out.append("```mermaid\npie showData title Story-Status")
    out.append(f'  "Done" : {counts.get("done",0)}')
    out.append(f'  "In Arbeit" : {counts.get("in_progress",0)}')
    out.append(f'  "Review" : {counts.get("review",0)}')
    out.append(f'  "Offen" : {counts.get("todo",0)}')
    out.append("```")
    if stories:
        out.append("| ID | Titel | Status |\n|---|---|---|")
        for st in stories:
            out.append(f"| {st.get('id','?')} | {st.get('title','')} | {st.get('status','todo')} |")
    out.append("\n## Decision-Log\n| ID | Thema | Entscheidung | Begründung |\n|---|---|---|---|")
    for d in decisions:
        out.append(f"| {d.get('id','')} | {d.get('topic','')} | {d.get('decision','')} | {d.get('rationale','')} |")

    docs_dir = os.path.join(base, "docs")
    os.makedirs(docs_dir, exist_ok=True)
    target = os.path.join(docs_dir, "TRACKER.md")
    with open(target, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"[render_tracker] {target} geschrieben.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
