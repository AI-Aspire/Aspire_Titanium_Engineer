#!/usr/bin/env python3
"""Render images/diagrams/src/*.dot to images/diagrams/*.svg with graphviz,
using the AI Aspire palette. Skips cleanly when `dot` is not installed.
"""
from __future__ import annotations

import shutil
import subprocess
import sys

from _common import ROOT

SRC = ROOT / "images" / "diagrams" / "src"
OUT = ROOT / "images" / "diagrams"


def main() -> int:
    dot = shutil.which("dot")
    files = sorted(SRC.glob("*.dot"))
    if not files:
        print("no diagram sources")
        return 0
    if not dot:
        print("graphviz `dot` not found; install it (brew install graphviz) to render diagrams")
        return 0
    for f in files:
        out = OUT / (f.stem + ".svg")
        subprocess.run([dot, "-Tsvg", str(f), "-o", str(out)], check=True)
        print(f"✓ {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
