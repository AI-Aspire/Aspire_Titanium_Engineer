"""The starter agent behind the demo app: retrieve, then answer.

Keyword retrieval over the corpus pages in the workspace, then one chat
completion that answers only from those pages. No embeddings, no vector store.
Replace this module with the agent your group built; the app only needs
`answer(question) -> {"answer": str, "pages": [str]}`.
"""
from __future__ import annotations

import re
import sys
import textwrap
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from openai import OpenAI  # noqa: E402

from helpers import workspace as ws  # noqa: E402
from helpers.llm import client
from helpers.config import KEY, LLM_BASE, LLM_MODEL  # noqa: E402

STOP = {"a", "an", "and", "are", "as", "at", "be", "for", "from", "how", "i", "in", "is", "it",
        "of", "on", "or", "the", "to", "what", "when", "with", "my", "can", "do", "you", "me"}
SYSTEM = """You are the assistant described in the charter. Answer only from the pages supplied.
Name the page you used in brackets. If the pages do not answer the question, say so in one sentence."""


def terms(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9][a-z0-9-]+", text.lower()) if t not in STOP}


def pages() -> list[dict]:
    """Every markdown page in the corpus, from the workspace or the seed."""
    base = ws.load_path("corpus")
    return [{"name": str(p.relative_to(base)), "text": p.read_text(encoding="utf-8")}
            for p in sorted(base.rglob("*.md"))]


def retrieve(question: str, k: int = 3) -> list[dict]:
    q = terms(question)
    ranked = sorted(pages(), key=lambda p: len(q & terms(p["text"])), reverse=True)
    return [p for p in ranked[:k] if q & terms(p["text"])]


@lru_cache(maxsize=1)
def _client() -> OpenAI:
    return client()


def answer(question: str) -> dict:
    """Retrieve, then answer from the retrieved pages only."""
    hits = retrieve(question)
    if not hits:
        return {"answer": "No corpus page matches that question.", "pages": []}
    evidence = "\n\n".join(f"[{p['name']}]\n{textwrap.shorten(p['text'], 1500)}" for p in hits)
    reply = _client().chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": f"PAGES:\n{evidence}\n\nQUESTION:\n{question}"}],
    )
    return {"answer": reply.choices[0].message.content or "", "pages": [p["name"] for p in hits]}


if __name__ == "__main__":
    print(answer(" ".join(sys.argv[1:]) or "How do I reach staging over the VPN?"))
