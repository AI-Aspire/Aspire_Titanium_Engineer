#!/usr/bin/env python3
"""Keep notebook outputs (they make the notebook readable on GitHub) but remove
anything that must not be committed: keys, bearer tokens, internal http://
endpoints, home-directory paths, widget state, and oversized outputs.

    python scripts/strip_outputs.py --scrub     # rewrite in place
    python scripts/strip_outputs.py --check     # exit 1 if anything would change
    python scripts/strip_outputs.py --all       # remove every output
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from _common import ROOT, notebooks

SECRET = re.compile(r"sk-[A-Za-z0-9_\-]{8,}|Bearer\s+[A-Za-z0-9_\-.]{8,}|http://[^\s\"'<>]+|/Users/[a-z]+/|/home/[a-z]+/|tvly-[A-Za-z0-9]{8,}")
MAX_BYTES = 50_000


def _text_of(output: dict) -> str:
    parts = []
    if "text" in output:
        parts.append("".join(output["text"]))
    for v in (output.get("data") or {}).values():
        parts.append("".join(v) if isinstance(v, list) else str(v))
    if "ename" in output:
        parts.append(output.get("evalue", "") + "".join(output.get("traceback", [])))
    return "\n".join(parts)


def scrub(nb: dict, *, drop_all: bool = False) -> int:
    changed = 0
    if nb.get("metadata", {}).pop("widgets", None) is not None:
        changed += 1
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        if drop_all:
            if cell.get("outputs") or cell.get("execution_count") is not None:
                cell["outputs"], cell["execution_count"] = [], None
                changed += 1
            continue
        kept = []
        for out in cell.get("outputs", []):
            text = _text_of(out)
            if SECRET.search(text) or len(text.encode("utf-8")) > MAX_BYTES:
                changed += 1
                kept.append({"output_type": "stream", "name": "stdout",
                             "text": ["[output removed before commit: secret, internal endpoint, or too large]\n"]})
            else:
                kept.append(out)
        cell["outputs"] = kept
        if "metadata" in cell and cell["metadata"].pop("widgets", None) is not None:
            changed += 1
    return changed


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("prefix", nargs="?")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--scrub", action="store_true")
    g.add_argument("--check", action="store_true")
    g.add_argument("--all", action="store_true")
    args = ap.parse_args(argv)
    dirty, n = [], 0
    for path in notebooks(args.prefix):
        n += 1
        nb = json.loads(path.read_text(encoding="utf-8"))
        changed = scrub(nb, drop_all=args.all)
        if changed:
            dirty.append((path, changed))
            if not args.check:
                path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for path, changed in dirty:
        verb = "would change" if args.check else "scrubbed"
        print(f"{'✗' if args.check else '✓'} {path.relative_to(ROOT)}: {verb} {changed} output(s)")
    if args.check and dirty:
        print(f"\n{len(dirty)} notebook(s) carry outputs that must not be committed. Run: make scrub")
        return 1
    print(f"✓ {n} notebook(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
