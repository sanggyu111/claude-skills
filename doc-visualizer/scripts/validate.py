#!/usr/bin/env python3
"""Check the doc-data JSON inside a doc-visualizer HTML page.

Usage: python3 validate.py page.html
Prints problems and exits 1 if any; prints a short summary and exits 0 otherwise.
"""
import json
import re
import sys

BLOCK_TYPES = {"flow", "timeline", "compare", "stats", "cards", "callout", "text"}
VISUAL_TYPES = BLOCK_TYPES - {"text"}
NODE_KINDS = {"input", "process", "store", "output", "decision", "concept"}


def main(path):
    html = open(path, encoding="utf-8").read()
    m = re.search(r'<script id="doc-data" type="application/json">(.*?)</script>', html, re.S)
    if not m:
        return ["doc-data script block not found"], None
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return [f"JSON parse error: {e}"], None

    problems = []
    if not data.get("title"):
        problems.append("missing title")
    title_tag = re.search(r"<title>(.*?)</title>", html[:8192], re.S)
    if not title_tag or title_tag.group(1).strip() != data.get("title", "").strip():
        problems.append("<title> tag does not match data title (replace the template's title)")
    if not data.get("tldr"):
        problems.append("missing tldr")

    sections = data.get("sections") or []
    if not sections:
        problems.append("no sections")
    seen_ids = set()
    has_flow = False
    for i, s in enumerate(sections, 1):
        where = f"section {i} ({s.get('heading', '?')})"
        sid = s.get("id", "")
        if sid and not re.fullmatch(r"[a-z0-9-]+", sid):
            problems.append(f"{where}: id must be lowercase letters, digits, '-'")
        if sid in seen_ids:
            problems.append(f"{where}: duplicate id '{sid}'")
        seen_ids.add(sid)
        blocks = s.get("blocks") or []
        types = [b.get("type") for b in blocks]
        for t in types:
            if t not in BLOCK_TYPES:
                problems.append(f"{where}: unknown block type '{t}'")
        if not any(t in VISUAL_TYPES for t in types):
            problems.append(f"{where}: no visual block (only text)")
        for b in blocks:
            if b.get("type") == "flow":
                has_flow = True
                problems += check_flow(b, where)
            if b.get("type") == "compare":
                cols = len(b.get("columns") or [])
                for r in b.get("rows") or []:
                    if len(r) != cols:
                        problems.append(f"{where}: compare row {r[:1]} has {len(r)} cells, expected {cols}")
    return problems, {"sections": len(sections), "has_flow": has_flow}


def check_flow(b, where):
    out = []
    nodes = b.get("nodes") or []
    ids = [n.get("id") for n in nodes]
    if len(set(ids)) != len(ids):
        out.append(f"{where}: flow has duplicate node ids")
    idset = set(ids)
    for n in nodes:
        if n.get("kind") not in NODE_KINDS:
            out.append(f"{where}: node '{n.get('id')}' kind '{n.get('kind')}' is not one of {sorted(NODE_KINDS)}")
        if len(n.get("label", "")) > 20:
            out.append(f"{where}: node label too long: '{n.get('label')}'")
    for e in b.get("edges") or []:
        if e.get("from") not in idset or e.get("to") not in idset:
            out.append(f"{where}: edge {e.get('from')} -> {e.get('to')} points to a missing node")
    for k, st in enumerate(b.get("steps") or [], 1):
        missing = [f for f in st.get("focus") or [] if f not in idset]
        if missing:
            out.append(f"{where}: step {k} focuses missing nodes {missing}")
    if not b.get("steps"):
        out.append(f"{where}: flow has no steps (step-through is the point)")
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    problems, summary = main(sys.argv[1])
    if problems:
        print("Problems:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print(f"OK: {summary['sections']} sections, flow: {'yes' if summary['has_flow'] else 'no'}")
