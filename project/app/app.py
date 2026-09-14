"""The demo app: a chat over your corpus, the artifacts it draws on, and a scorecard.

Run from the repository root:

    uv run streamlit run project/app/app.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
for p in (str(ROOT), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import streamlit as st  # noqa: E402

import agent  # noqa: E402
from helpers import brand  # noqa: E402
from helpers import workspace as ws  # noqa: E402
from helpers.config import COHORT, LLM_MODEL, PROJECT  # noqa: E402

# ── Charter and page ────────────────────────────────────────────────────────

CHARTER = ws.load("charter", quiet=True)
HEADING = next((ln.lstrip("#").strip() for ln in CHARTER.splitlines() if ln.startswith("# ")), "Demo")
TITLE = HEADING.split(":", 1)[1].strip() if HEADING.lower().startswith("charter:") else HEADING

st.set_page_config(page_title=TITLE, layout="wide")
st.markdown(brand.css(), unsafe_allow_html=True)
st.title(TITLE)
st.caption(f"model {LLM_MODEL} · charter from the {ws.source('charter')}")

# ── Sidebar: every artifact and where it comes from ─────────────────────────

with st.sidebar:
    st.subheader("Workspace")
    rows = ["| artifact | source |", "|---|---|"]
    for name in ws.SCHEMA:
        rows.append(f"| `{name}` | {ws.source(name) or 'missing'} |")
    st.markdown("\n".join(rows))
    st.divider()
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

# ── Chat ────────────────────────────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("pages"):
            st.caption("pages used: " + ", ".join(msg["pages"]))

if question := st.chat_input("Ask a question your users would ask"):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        with st.spinner("retrieving and answering"):
            try:
                result = agent.answer(question)
            except Exception as exc:  # noqa: BLE001
                result = {"answer": f"The agent raised {type(exc).__name__}: {exc}", "pages": []}
        st.markdown(result["answer"])
        if result["pages"]:
            st.caption("pages used: " + ", ".join(result["pages"]))
    st.session_state.messages.append({"role": "assistant", "content": result["answer"], "pages": result["pages"]})

# ── Scorecard ───────────────────────────────────────────────────────────────


def criteria() -> list[str]:
    """The criterion column of the table in DEMO_SCORECARD.md."""
    out = []
    for line in (PROJECT / "DEMO_SCORECARD.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and cells[0] and cells[0] != "Criterion" and not set(cells[0]) <= {"-", " "}:
            out.append(cells[0])
    return out


with st.expander("Score this demo"):
    with st.form("scorecard"):
        group = st.text_input("Group", value=COHORT.get("cohort", {}).get("id", "dev"))
        scores = []
        for i, crit in enumerate(criteria()):
            left, right = st.columns([1, 2])
            score = left.slider(crit, 0, 5, 0, key=f"score_{i}")
            note = right.text_input("Evidence or note", key=f"note_{i}", label_visibility="collapsed",
                                    placeholder="which artifact backs this score")
            scores.append({"group": group, "criterion": crit, "score": score, "note": note})
        if st.form_submit_button("Save scorecard"):
            path = ws.save("scorecard", scores, module="project")
            st.success(f"wrote {len(scores)} rows to {path.relative_to(ROOT)}")
