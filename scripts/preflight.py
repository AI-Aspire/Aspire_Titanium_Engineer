#!/usr/bin/env python3
"""Check the network before the first morning.

    python scripts/preflight.py             # every host the course needs
    python scripts/preflight.py --timeout 10

Prints one row per host with a verdict (open, intercepted, blocked) and the
certificate issuer, then the proxy and trust-store variables that are set.
Exits 0 unless every host failed, so a partly blocked network still prints
the table you need to take to whoever runs the proxy.
"""
from __future__ import annotations

import argparse
import sys

from _common import ROOT
sys.path.insert(0, str(ROOT))

from helpers import preflight  # noqa: E402


def table(report: preflight.Report) -> str:
    rows = [("host", "why", "verdict", "issuer or error")]
    for p in report.probes:
        where = p.host if p.port in (80, 443) else f"{p.host}:{p.port}"
        detail = p.issuer if p.connected else p.error
        if p.connected and not p.tls:
            detail = "plain http, no certificate"
        rows.append((where, p.why, p.verdict, detail))
    widths = [max(len(r[i]) for r in rows) for i in range(3)]
    lines = []
    for n, r in enumerate(rows):
        lines.append("  ".join(r[i].ljust(widths[i]) for i in range(3)) + "  " + r[3])
        if n == 0:
            lines.append("  ".join("-" * w for w in widths) + "  " + "-" * 16)
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=float, default=6.0, help="seconds per connection")
    args = ap.parse_args(argv)

    report = preflight.check_egress(timeout=args.timeout)
    print(table(report))
    print()
    if report.proxy_env:
        print("proxy and trust-store variables set: " + ", ".join(sorted(report.proxy_env)))
    else:
        print("proxy and trust-store variables set: none")
    print(str(report))
    print(report.verdict())
    return 1 if report.all_failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
