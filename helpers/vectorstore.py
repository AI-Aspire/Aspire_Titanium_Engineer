"""On-disk, embedded Qdrant. Embed the corpus once into a local folder and every
notebook reads it back in milliseconds. No server to run.

Qdrant's local mode is single-writer: one process may hold the folder open at a
time. `local_client` keeps a notebook to ONE cached handle, so re-running a
connect cell is safe. If you see "Storage folder ... already accessed by another
instance", another kernel holds it. Restart that kernel or this one.
"""
from pathlib import Path

from helpers.config import ROOT

LOCAL_QDRANT = ROOT / ".qdrant_local"   # gitignored; persists across sessions
COLLECTION = "workspace_corpus"

_clients: dict[str, object] = {}


def local_client(path=LOCAL_QDRANT):
    """One embedded QdrantClient per path per process."""
    from qdrant_client import QdrantClient

    key = str(path)
    if key not in _clients:
        Path(key).mkdir(parents=True, exist_ok=True)
        _clients[key] = QdrantClient(path=key)
    return _clients[key]


def load_local_store(embeddings, *, collection=COLLECTION, path=LOCAL_QDRANT):
    """Wrap an already-built local collection as a LangChain QdrantVectorStore.

    Raises if the index is not there yet. The RAG module builds it; later
    modules reuse it.
    """
    from langchain_qdrant import QdrantVectorStore

    client = local_client(path)
    if not (client.collection_exists(collection) and client.count(collection).count):
        raise RuntimeError(
            f"No local '{collection}' index at {path} yet. Run the RAG notebook "
            f"first to build it."
        )
    return QdrantVectorStore(client=client, collection_name=collection, embedding=embeddings)
