#!/usr/bin/env python3
"""Write images/banner.svg from cohort.toml and the AI Aspire palette.

Paper ground, a hairline rule, the AI Aspire mark at left, the wordmark
"Titanium Engineer" in slate, and (when cohort.toml names a client) a small
pill at the right. The logo PNG is embedded as base64 so the SVG is one file.
"""
from __future__ import annotations

import base64
import struct
import sys
import tomllib

from _common import ROOT

sys.path.insert(0, str(ROOT))
from helpers.brand import PALETTE  # noqa: E402

LOGO = ROOT / "images" / "logo" / "aiaspire.png"
OUT = ROOT / "images" / "banner.svg"
W, H = 1600, 400


def png_size(path) -> tuple[int, int]:
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    w, h = struct.unpack(">II", head[16:24])
    return w, h


def main() -> int:
    with (ROOT / "cohort.toml").open("rb") as fh:
        cfg = tomllib.load(fh)
    cohort, banner = cfg.get("cohort", {}), cfg.get("banner", {})
    p = PALETTE
    lw, lh = png_size(LOGO)
    logo_h = 150
    logo_w = round(lw * logo_h / lh)
    b64 = base64.b64encode(LOGO.read_bytes()).decode()
    x_logo, y_logo = 96, (H - logo_h) // 2
    x_text = x_logo + logo_w + 72

    pill = ""
    label = " · ".join(v for v in (cohort.get("name"), cohort.get("city"), cohort.get("client")) if v)
    if banner.get("show_client", True) and cohort.get("client"):
        tw = 18 * len(label) + 48
        pill = (
            f'<rect x="{W - 96 - tw}" y="{H // 2 - 26}" width="{tw}" height="52" rx="26" '
            f'fill="{p["surface"]}" stroke="{p["neutral_300"]}" stroke-width="1.5"/>'
            f'<text x="{W - 96 - tw / 2}" y="{H // 2 + 9}" text-anchor="middle" font-family="Inter, Helvetica, Arial, sans-serif" '
            f'font-size="26" fill="{p["neutral_700"]}">{label}</text>'
        )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Titanium Engineer, by AI Aspire">
  <rect width="{W}" height="{H}" fill="{p['paper']}"/>
  <line x1="0" y1="{H - 1}" x2="{W}" y2="{H - 1}" stroke="{p['neutral_200']}" stroke-width="2"/>
  <image x="{x_logo}" y="{y_logo}" width="{logo_w}" height="{logo_h}" xlink:href="data:image/png;base64,{b64}"/>
  <text x="{x_text}" y="{H // 2 + 2}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="88" font-weight="700" fill="{p['slate_900']}" letter-spacing="-1">Titanium Engineer</text>
  <text x="{x_text + 4}" y="{H // 2 + 62}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="30" fill="{p['neutral_600']}">A five-day intensive for enterprise engineers · aiaspire.ai</text>
  {pill}
</svg>
"""
    OUT.write_text(svg, encoding="utf-8")
    print(f"✓ {OUT.relative_to(ROOT)} ({len(svg) // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
