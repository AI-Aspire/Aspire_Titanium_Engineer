"""AI Aspire palette and CSS for anything that renders HTML: Streamlit apps,
notebook display helpers, generated diagrams. Values come from the platform's
design tokens ("paper and ink", 2026).

Rules that travel with the palette:
- slate is for structure and actions
- clay is only for human-origin content (quotes, names, evidence)
- bronze is for warnings, always with an icon, never colour alone
- the logo navy and orange stay inside the logo
"""
from __future__ import annotations

PALETTE = {
    "paper": "#F9F8F4",
    "surface": "#FFFFFF",
    "ink": "#16130E",
    "neutral_200": "#E6E2D8",
    "neutral_300": "#D6D0C2",
    "neutral_600": "#5A544B",
    "neutral_700": "#433E36",
    "slate_950": "#222F3D",
    "slate_900": "#324457",
    "slate_700": "#55718F",
    "slate_600": "#6A89AB",
    "slate_100": "#ECF3FA",
    "clay_700": "#9A5C48",
    "clay_600": "#B77258",
    "clay_100": "#F9EFEB",
    "bronze_700": "#856A3F",
    "bronze_300": "#DECFB8",
    "bronze_100": "#F6F1E9",
    "logo_navy": "#003064",
    "logo_orange": "#F86400",
}

PRIMARY = PALETTE["slate_700"]
FONT_SANS = '"Inter", "InterVariable", ui-sans-serif, system-ui, sans-serif'
FONT_SERIF = '"Newsreader", "Charter", "Iowan Old Style", Georgia, serif'
FONT_MONO = '"JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace'

# Categorical series for charts, in order of use.
SERIES = [PALETTE["slate_700"], PALETTE["clay_600"], PALETTE["bronze_700"],
          PALETTE["slate_950"], PALETTE["neutral_600"]]


def css() -> str:
    """A stylesheet for Streamlit and other HTML surfaces."""
    p = PALETTE
    return f"""
    <style>
    :root {{
      --paper: {p['paper']}; --surface: {p['surface']}; --ink: {p['ink']};
      --slate: {p['slate_900']}; --slate-hover: {p['slate_950']}; --slate-soft: {p['slate_100']};
      --clay: {p['clay_700']}; --clay-soft: {p['clay_100']};
      --bronze: {p['bronze_700']}; --bronze-soft: {p['bronze_100']};
      --rule: {p['neutral_200']};
    }}
    html, body, [data-testid="stAppViewContainer"] {{
      background: var(--paper); color: var(--ink); font-family: {FONT_SANS};
    }}
    h1, h2, h3 {{ font-family: {FONT_SERIF}; font-weight: 500; letter-spacing: 0; }}
    code, pre {{ font-family: {FONT_MONO}; }}
    .stButton > button {{
      background: var(--slate); color: #fff; border: 1px solid var(--slate);
      border-radius: 0.5rem; box-shadow: none;
    }}
    .stButton > button:hover {{ background: var(--slate-hover); border-color: var(--slate-hover); }}
    blockquote {{ border-left: 2px solid var(--clay); color: var(--clay); font-family: {FONT_SERIF}; font-style: italic; }}
    .warn {{ background: var(--bronze-soft); border: 1px solid {p['bronze_300']}; color: var(--bronze); padding: .5rem .75rem; border-radius: .5rem; }}
    hr {{ border: 0; border-top: 1px solid var(--rule); }}
    </style>
    """


def matplotlib_style() -> dict:
    """rcParams for charts that match the palette."""
    p = PALETTE
    return {
        "figure.facecolor": p["paper"], "axes.facecolor": p["paper"],
        "axes.edgecolor": p["neutral_300"], "axes.labelcolor": p["neutral_700"],
        "xtick.color": p["neutral_600"], "ytick.color": p["neutral_600"],
        "text.color": p["ink"], "axes.prop_cycle": _cycler(),
        "axes.spines.top": False, "axes.spines.right": False,
        "grid.color": p["neutral_200"], "axes.grid": True, "axes.grid.axis": "y",
        "font.family": "sans-serif", "font.sans-serif": ["Inter", "Helvetica", "Arial"],
    }


def _cycler():
    from matplotlib import cycler
    return cycler(color=SERIES)
