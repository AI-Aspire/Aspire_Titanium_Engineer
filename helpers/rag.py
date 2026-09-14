"""Small RAG plumbing shared across the LangChain modules."""


def format_docs(docs) -> str:
    """Join retrieved LangChain documents into one context string."""
    return "\n\n".join(d.page_content for d in docs)


def chunk_text(text: str, size: int = 800, overlap: int = 100) -> list[str]:
    """Plain character chunking with overlap. The from-scratch baseline the
    notebooks build first, before a library splitter replaces it."""
    if size <= overlap:
        raise ValueError("size must be larger than overlap")
    out, start = [], 0
    while start < len(text):
        out.append(text[start:start + size])
        start += size - overlap
    return out
