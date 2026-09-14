#!/usr/bin/env python3
"""Regenerate data/seed/ by running the notebooks headlessly against the seed
workspace, in module order, with small budgets and fixed random seeds.

    python scripts/make_seed.py                 # modules 02..21
    python scripts/make_seed.py --through 08    # stop after module 08
    python scripts/make_seed.py --only 09

Hand-authored seed inputs are never overwritten by this script:
    data/seed/pitch/charter.md
    data/seed/corpus/kb/*.md
    data/seed/transcripts/tickets_raw.jsonl
Everything else under data/seed/ is produced by a notebook.

Afterwards it anonymises emails and phone numbers and validates the result.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

from _common import ROOT, notebooks, own_env

SEED = ROOT / "data" / "seed"
HAND_AUTHORED = {"pitch/charter.md", "transcripts/tickets_raw.jsonl"}
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"\b(?:\+?1[ -]?)?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}\b")


def anonymise() -> int:
    n = 0
    for p in SEED.rglob("*"):
        if not p.is_file() or p.suffix not in {".md", ".jsonl", ".json", ".csv"}:
            continue
        rel = str(p.relative_to(SEED))
        if rel in HAND_AUTHORED or rel.startswith("corpus/kb/"):
            continue
        text = p.read_text(encoding="utf-8")
        new = EMAIL.sub("person@example.com", text)
        new = PHONE.sub("555-0100", new)
        if new != text:
            p.write_text(new, encoding="utf-8")
            n += 1
    return n


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--through", default="21")
    ap.add_argument("--only")
    ap.add_argument("--timeout", type=int, default=1800)
    args = ap.parse_args(argv)
    env = dict(os.environ, TE_WORKSPACE=str(SEED), TE_SEED_MODE="1", PYTHONHASHSEED="0")
    failures = []
    for nb in notebooks():
        module = nb.relative_to(ROOT).parts[0]
        num = module[:2]
        if num == "01":
            continue
        if args.only and not module.startswith(args.only):
            continue
        if num > args.through[:2]:
            break
        mdir = ROOT / module
        cmd = (["uv", "run", "--project", str(mdir)] if own_env(mdir) else ["uv", "run", "--all-groups"]) + \
              ["python", str(ROOT / "scripts/check_execute.py"), "--single", str(nb), "--timeout", str(args.timeout)]
        r = subprocess.run(cmd, env=env, text=True)
        if r.returncode:
            failures.append(nb)
    changed = anonymise()
    print(f"anonymised {changed} file(s)")
    check = subprocess.run([sys.executable, str(ROOT / "scripts/check_workspace.py"), "--seed",
                            "--day", "5" if not args.only else "5"], text=True)
    if failures:
        for f in failures:
            print(f"✗ {f.relative_to(ROOT)}")
        return 1
    return check.returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
