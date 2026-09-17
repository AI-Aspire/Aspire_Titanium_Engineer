#!/usr/bin/env python3
"""The release gate: a pass rate per metric, a floor, and an exit code.

    uv run --no-sync python scripts/release_gate.py --min-score 0.8
    uv run --no-sync python scripts/release_gate.py --min-score 0.8 --version v2 --min faithfulness=0.9

Reads `deepeval_results` from the workspace (the seed when the workspace does
not have it), prints the pass rate of every metric for every version, holds the
candidate version against the floor with `helpers.evals.gate`, and exits 1 when
any metric is under it or any judge row errored. A pipeline step that runs this
cannot ship a version the evals rejected, and the definition of rejected is one
line the team can read.
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict

from helpers import workspace as ws
from helpers.evals import gate

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")


def pass_rates(rows: list[dict]) -> dict[str, dict[str, float]]:
    """{version: {metric: fraction of rows that passed}}. An errored row is a failure."""
    seen: dict = defaultdict(int)
    hits: dict = defaultdict(int)
    for r in rows:
        key = (str(r.get("version")), str(r.get("metric")))
        seen[key] += 1
        hits[key] += 1 if r.get("passed") and not r.get("error") else 0
    out: dict[str, dict[str, float]] = defaultdict(dict)
    for (version, metric), n in seen.items():
        out[version][metric] = round(hits[(version, metric)] / n, 3)
    return dict(out)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--min-score", type=float, default=0.8, help="floor for every metric (default 0.8)")
    ap.add_argument("--version", help="the candidate version; default: the last one in sorted order")
    ap.add_argument("--min", action="append", default=[], metavar="METRIC=FLOOR",
                    help="a different floor for one metric; repeatable")
    ap.add_argument("--allow-errors", action="store_true", help="do not fail on judge errors")
    args = ap.parse_args(argv)

    rows = ws.load("deepeval_results", quiet=True)
    rates = pass_rates(rows)
    versions = sorted(rates)
    candidate = args.version or versions[-1]
    if candidate not in rates:
        print(f"✗ no rows for version {candidate!r}; have {versions}")
        return 2
    metrics = sorted({m for v in rates.values() for m in v})

    print(f"deepeval_results from the {ws.source('deepeval_results')}: {len(rows)} rows, versions {versions}")
    print(f"{'metric':<18}" + "".join(f"{v:>8}" for v in versions))
    for m in metrics:
        print(f"{m:<18}" + "".join(f"{rates[v].get(m, float('nan')):>8.2f}" for v in versions))

    minimum = {m: args.min_score for m in metrics}
    for spec in args.min:
        metric, _, floor = spec.partition("=")
        minimum[metric.strip()] = float(floor)
    verdict = gate(rates[candidate], minimum)
    errors = sum(1 for r in rows if str(r.get("version")) == candidate and r.get("error"))

    reasons = [f"{m} {rates[candidate].get(m, 'missing')} < {minimum[m]}" for m in verdict["failed"]]
    if errors and not args.allow_errors:
        reasons.append(f"{errors} judge error(s)")
    if reasons:
        print(f"✗ gate failed for {candidate}: " + "; ".join(reasons))
        return 1
    print(f"✓ gate passed for {candidate}: every metric at or above its floor, {errors} judge error(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
