#!/usr/bin/env python3
"""Generate a marimo .py next to every source .ipynb, or check they are current.

The .ipynb is the source of truth. `marimo convert` strips outputs, so a
notebook with fresh outputs still converts to the same .py.

    python scripts/make_marimo.py            # write every NN_*/**/*.py
    python scripts/make_marimo.py --check    # exit 1 if any .py is stale or missing
    python scripts/make_marimo.py 05         # one module
"""
from __future__ import annotations

import argparse
import ast
import difflib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from _common import ROOT, notebooks

GENERATED_LINE = "__generated_with"


def render_disclosures(source: str) -> str:
    """Render Markdown inside HTML disclosures, which marimo leaves literal."""
    import marimo as mo

    pattern = r"(<details\b[^>]*>\s*<summary\b[^>]*>.*?</summary>)(.*?)(</details>)"
    return re.sub(pattern, lambda m: m[1] + "\n" + mo.md(m[2].strip()).text + "\n" + m[3],
                  source, flags=re.S)


def convert(nb: Path, out: Path) -> None:
    doc = json.loads(nb.read_text(encoding="utf-8"))
    for cell in doc["cells"]:
        if cell["cell_type"] == "markdown":
            cell["source"] = render_disclosures("".join(cell["source"])).splitlines(keepends=True)
    with tempfile.TemporaryDirectory() as td:
        prepared = Path(td) / nb.name
        prepared.write_text(json.dumps(doc), encoding="utf-8")
        subprocess.run([sys.executable, "-m", "marimo", "convert", str(prepared), "-o", str(out)],
                       check=True, capture_output=True, text=True)


def _normalise(text: str) -> str:
    """The mirror with the marimo version line removed, as a canonical form.

    `marimo convert` writes code through `ast.unparse`, whose choice of
    quotes inside f-strings has changed between CPython patch releases, so
    two machines can print the same notebook differently. Comparing the
    parsed tree ignores that; the text is the fallback for anything that
    does not parse.
    """
    body = "\n".join(l for l in text.splitlines() if GENERATED_LINE not in l).strip()
    try:
        return ast.dump(ast.parse(body))
    except SyntaxError:
        return body


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("prefix", nargs="?")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    stale, n = [], 0
    for nb in notebooks(args.prefix):
        py = nb.with_suffix(".py")
        n += 1
        if args.check:
            with tempfile.TemporaryDirectory() as td:
                tmp = Path(td) / "nb.py"
                convert(nb, tmp)
                fresh = _normalise(tmp.read_text(encoding="utf-8"))
            have = _normalise(py.read_text(encoding="utf-8")) if py.exists() else ""
            if have != fresh:
                # Say what changed, not only that something did: the same
                # notebook can convert differently on another machine.
                diff = list(difflib.unified_diff(have.splitlines(), fresh.splitlines(),
                                                 "committed", "fresh", lineterm="", n=1))
                stale.append((py, diff[:40]))
        else:
            convert(nb, py)
            print(f"✓ {py.relative_to(ROOT)}")
    if args.check:
        for p, diff in stale:
            print(f"✗ stale or missing: {p.relative_to(ROOT)}  (run: make marimo)")
            for line in diff:
                print(f"    {line}")
        if stale:
            return 1
        print(f"✓ {n} marimo mirror(s) are current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
