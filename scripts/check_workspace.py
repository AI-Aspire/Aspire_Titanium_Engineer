#!/usr/bin/env python3
"""Validate the workspace (or the seed) against the artifact contract.

    python scripts/check_workspace.py --day 2        # everything produced on days 1-2
    python scripts/check_workspace.py --seed         # the committed seed, all days
    python scripts/check_workspace.py --seed --day 1
    python scripts/check_workspace.py --status       # print where each artifact comes from
"""
from __future__ import annotations

import argparse
import os
import sys

from _common import ROOT
sys.path.insert(0, str(ROOT))

from helpers import workspace as ws  # noqa: E402


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", type=int, default=5)
    ap.add_argument("--seed", action="store_true", help="validate data/seed/ instead of the workspace")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args(argv)
    if args.seed:
        os.environ["TE_WORKSPACE"] = str(ws.seed_root())
    if args.status:
        ws.status()
        return 0
    base = ws.root()
    wanted = {m for d, mods in ws.DAYS.items() if d <= args.day for m in mods}
    problems, ok = [], 0
    for name, art in ws.SCHEMA.items():
        if art.producer not in wanted:
            continue
        p = base / art.path
        if not ws._present(p, art.fmt):
            problems.append(f"{name}: missing ({art.path}; written by module {art.producer})")
            continue
        try:
            data = ws._read(p, art.fmt)
        except Exception as e:  # noqa: BLE001
            problems.append(f"{name}: unreadable ({e})")
            continue
        bad = ws.validate(name, data)
        if bad:
            problems.append(f"{name}: " + "; ".join(bad))
        else:
            ok += 1
    label = "seed" if args.seed else "workspace"
    for pr in problems:
        print(f"✗ {pr}")
    if problems:
        print(f"\n{len(problems)} problem(s) in the {label} through day {args.day}; {ok} artifact(s) valid.")
        return 1
    print(f"✓ {label} valid through day {args.day}: {ok} artifact(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
