#!/usr/bin/env python3
"""Verify every relative link in markdown files and notebook markdown cells
points at something that exists. External links are not checked; open those
by hand before committing.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from _common import ROOT

SKIP = {".git", ".venv", "node_modules", "__pycache__", ".ipynb_checkpoints", "__marimo__", ".qdrant_local"}
MD_LINK = re.compile(r"\[[^\]]*\]\(\s*<?([^)\s>]+)>?\s*(?:\"[^\"]*\")?\)")
HTML_ATTR = re.compile(r'(?:src|href)\s*=\s*"([^"]+)"')


def _external(t: str) -> bool:
    return t.startswith(("http://", "https://", "mailto:", "#", "data:", "//"))


def _check_text(text: str, base: Path, label: str, broken: list, counter: list) -> None:
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"`[^`]*`", "", line)   # links inside inline code are examples, not links
        for m in (*MD_LINK.finditer(line), *HTML_ATTR.finditer(line)):
            target = m.group(1).strip()
            if not target or _external(target):
                continue
            part = unquote(target.split("#", 1)[0])
            if not part:
                continue
            counter[0] += 1
            if not (base / part).resolve().exists():
                broken.append((label, lineno, target))


def main() -> int:
    broken, counter, files = [], [0], 0
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or any(s in p.parts for s in SKIP):
            continue
        rel = p.relative_to(ROOT)
        if p.suffix == ".md":
            files += 1
            _check_text(p.read_text(encoding="utf-8", errors="replace"), p.parent, str(rel), broken, counter)
        elif p.suffix == ".ipynb":
            files += 1
            nb = json.loads(p.read_text(encoding="utf-8"))
            for k, cell in enumerate(nb.get("cells", [])):
                if cell.get("cell_type") == "markdown":
                    _check_text("".join(cell.get("source", [])), p.parent, f"{rel}[cell {k}]", broken, counter)
    for label, lineno, target in broken:
        print(f"✗ {label}:{lineno} -> {target}  (does not exist)", file=sys.stderr)
    if broken:
        print(f"\n{len(broken)} broken link(s) of {counter[0]} checked", file=sys.stderr)
        return 1
    print(f"✓ {counter[0]} relative links OK across {files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
