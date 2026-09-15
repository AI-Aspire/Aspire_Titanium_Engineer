"""The retrieval experiments extracted from Retrieval_Ladder.ipynb.

Read this file to inspect the algorithms. Claude can call its CLI; students
can request experiments in ordinary conversation. Nothing runs on import.
"""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import redirect_stdout
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import re
import sys
import time
from datetime import datetime, timezone

from helpers import workspace as ws
from helpers.config import COHERE_KEY, EMBED_MODEL, LLM_MODEL

TOKEN = re.compile(r"[a-z0-9][a-z0-9.-]*")
RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
RUNGS = ("dense", "bm25", "hybrid_rrf", "cross_encoder", "multi_query")


def tokenize(text):
    return TOKEN.findall(text.lower())


class BM25:
    """The notebook's from-scratch BM25: rarity, saturation, length correction.

    Its positive log1p IDF differs from rank_bm25.BM25Okapi's IDF/floor.
    Identical tokenization therefore need not produce identical rankings.
    """

    def __init__(self, texts, k1=1.5, b=0.75):
        self.docs = [tokenize(t) for t in texts]
        self.N, self.k1, self.b = len(self.docs), k1, b
        self.avgdl = sum(len(d) for d in self.docs) / self.N if self.N else 0
        if not self.avgdl:
            raise ValueError("BM25 needs at least one non-empty tokenized document")
        self.df = Counter(t for d in self.docs for t in set(d))
        self.tf = [Counter(d) for d in self.docs]

    def idf(self, term):
        n = self.df.get(term, 0)
        return math.log((self.N - n + 0.5) / (n + 0.5) + 1)

    def score(self, query, i):
        dl, score = len(self.docs[i]), 0.0
        for term in tokenize(query):
            freq = self.tf[i].get(term, 0)
            if freq:
                score += self.idf(term) * freq * (self.k1 + 1) / (
                    freq + self.k1 * (1 - self.b + self.b * dl / self.avgdl))
        return score

    def search(self, query, k=4):
        return sorted(range(self.N), key=lambda i: self.score(query, i), reverse=True)[:k]


def rrf(rankings, k=60):
    """Combine ranks rather than adding incompatible dense and BM25 scores."""
    scores = {}
    for ranking in rankings:
        for rank, chunk in enumerate(ranking, 1):
            scores[chunk] = scores.get(chunk, 0.0) + 1 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)


def score_case(case, ranked, page_of):
    """Hit@k and reciprocal rank, with labels attached to pages, not chunks."""
    for rank, chunk in enumerate(ranked, 1):
        if page_of[chunk] in case["pages"]:
            return 1.0, 1.0 / rank
    return 0.0, 0.0


def read_pages():
    base = ws.load_path("corpus")
    return {p.relative_to(base).as_posix(): p.read_text(encoding="utf-8")
            for p in sorted(base.rglob("*.md"))
            if not p.relative_to(base).as_posix().startswith("wiki/")
            and p.relative_to(base).as_posix() != "vibe_checks.md"}


def load_cases(pages, filename=None):
    cases = json.loads(Path(filename).read_text()) if filename else ws.load("eval_cases")
    errors = ws.validate("eval_cases", cases)
    if errors:
        raise ValueError("Invalid eval cases: " + "; ".join(errors))
    ids = set()
    for case in cases:
        if not isinstance(case['id'], str) or case['id'] in ids:
            raise ValueError("Case IDs must be unique strings")
        ids.add(case['id'])
        if not isinstance(case.get('question'), str) or not case['question'].strip():
            raise ValueError(f"Case {case['id']} needs a non-empty question")
        if not isinstance(case.get('pages'), list) or not all(isinstance(p, str) for p in case['pages']):
            raise ValueError(f"Case {case['id']} needs a pages list (empty means unscored)")
        unknown = set(case['pages']) - set(pages)
        if unknown:
            raise ValueError(f"Case {case['id']} labels pages outside this corpus: {sorted(unknown)}")
    return cases


def label_pages(pages):
    """Original model-assisted labelling; returns proposals for human review."""
    from pydantic import BaseModel
    from helpers.llm import chat_model

    class Evidence(BaseModel):
        pages: list[str]

    digest = "\n".join(f"- {name}: {' '.join(text.split())[:240]}" for name, text in pages.items())
    labeller = chat_model(temperature=0).with_structured_output(Evidence)
    cases = []
    for v in ws.load("vibe_checks"):
        proposed = labeller.invoke(
            "Which of these pages hold the evidence a good answer to the question needs? "
            "Return only page names from the list, or an empty list if none does.\n\n"
            f"PAGES:\n{digest}\n\nQuestion: {v['input']}\nA good answer includes: {v['expected']}")
        cases.append({"id": v['id'], "question": v['input'], "reference": v['expected'],
                      "pages": [p for p in proposed.pages if p in pages]})
    return cases


class Ladder:
    """Same chunks and original five retrieval rungs, with lazy model loading."""

    def __init__(self, pages, chunk_size=800, overlap=120, candidates=12):
        from langchain_core.documents import Document
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        from rank_bm25 import BM25Okapi
        if not pages or chunk_size <= overlap or overlap < 0 or candidates < 1:
            raise ValueError("Need pages, chunk_size > overlap >= 0, and positive candidates")
        self.pages = pages
        self.chunk_size, self.overlap, self.candidates = chunk_size, overlap, candidates
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        self.docs = splitter.split_documents([
            Document(page_content=text, metadata={"page": name}) for name, text in pages.items()])
        for i, doc in enumerate(self.docs):
            doc.metadata['chunk'] = i
        self.chunks = [d.page_content for d in self.docs]
        self.page_of = [d.metadata['page'] for d in self.docs]
        self.scratch = BM25(self.chunks)
        self.library = BM25Okapi([tokenize(c) for c in self.chunks])
        self.store = self.qdrant = self.encoder = self.llm = self.cohere = None
        self.trace = {}

    def prepare(self, rungs):
        """Index/model startup happens before search timing, and is reported separately."""
        os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
        started = time.perf_counter()
        if set(rungs) - {'bm25'} and self.store is None:
            from langchain_qdrant import QdrantVectorStore
            from qdrant_client import QdrantClient
            from qdrant_client.models import Distance, VectorParams
            from helpers.llm import embeddings_model
            embeddings = embeddings_model()
            self.qdrant = QdrantClient(":memory:")
            dim = len(embeddings.embed_query("dimension probe"))
            self.qdrant.create_collection("ladder", vectors_config=VectorParams(size=dim, distance=Distance.COSINE))
            self.store = QdrantVectorStore(client=self.qdrant, collection_name="ladder", embedding=embeddings)
            self.store.add_documents(self.docs)
        if set(rungs) & {'cross_encoder', 'multi_query'} and self.encoder is None:
            from sentence_transformers import CrossEncoder
            self.encoder = CrossEncoder(RERANK_MODEL)
        if 'multi_query' in rungs and self.llm is None:
            from helpers.llm import chat_model
            self.llm = chat_model(temperature=0)
        if 'cohere_rerank' in rungs and self.cohere is None:
            if not COHERE_KEY:
                raise ValueError("cohere_rerank needs COHERE_API_KEY")
            import cohere
            self.cohere = cohere.ClientV2(api_key=COHERE_KEY)
        return round(1000 * (time.perf_counter() - started), 2)

    def bm25_search(self, question, k):
        scores = self.library.get_scores(tokenize(question))
        return sorted(range(len(self.chunks)), key=lambda i: scores[i], reverse=True)[:k]

    def dense_search(self, question, k):
        return [d.metadata['chunk'] for d, _ in self.store.similarity_search_with_score(question, k=k)]

    def hybrid_search(self, question, k):
        return rrf([self.dense_search(question, self.candidates),
                    self.bm25_search(question, self.candidates)])[:k]

    def rerank(self, question, candidates, k):
        scores = self.encoder.predict([(question, self.chunks[i]) for i in candidates])
        return [i for i, _ in sorted(zip(candidates, scores), key=lambda x: -x[1])][:k]

    def expand(self, question):
        reply = self.llm.invoke("Write 3 short, distinct search queries that would find evidence for this question. "
                                f"One per line, no numbering.\n\n{question}")
        text = reply.content if isinstance(reply.content, str) else str(reply.content)
        extras = [line.strip(' -\t') for line in text.splitlines() if line.strip()]
        return [question, *extras][:4]

    def search(self, name, question, k):
        self.trace = {}
        if name == 'bm25':
            return self.bm25_search(question, k)
        if name == 'dense':
            return self.dense_search(question, k)
        if name == 'hybrid_rrf':
            dense = self.dense_search(question, self.candidates)
            sparse = self.bm25_search(question, self.candidates)
            self.trace = {'dense_candidates': self.hits(dense), 'bm25_candidates': self.hits(sparse)}
            return rrf([dense, sparse])[:k]
        if name == 'multi_query':
            rewrites = self.expand(question)
            candidates = rrf([self.hybrid_search(q, self.candidates) for q in rewrites])[:self.candidates]
            self.trace = {'queries': rewrites, 'rerank_candidates': self.hits(candidates)}
            return self.rerank(question, candidates, k)
        candidates = self.hybrid_search(question, self.candidates)
        self.trace = {'rerank_candidates': self.hits(candidates)}
        if name == 'cross_encoder':
            return self.rerank(question, candidates, k)
        if name == 'cohere_rerank':
            result = self.cohere.rerank(model='rerank-v3.5', query=question,
                                       documents=[self.chunks[i] for i in candidates], top_n=k)
            return [candidates[r.index] for r in result.results]
        raise ValueError(f"Unknown rung: {name}")

    def hits(self, ranked):
        return [{'rank': rank, 'chunk': i, 'page': self.page_of[i], 'text': self.chunks[i]}
                for rank, i in enumerate(ranked, 1)]

    def close(self):
        if self.qdrant is not None:
            self.qdrant.close()


def provenance(pages, ladder=None):
    return {
        'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
        'corpus_source': ws.source('corpus'),
        'corpus_sha256': hashlib.sha256(json.dumps(pages, sort_keys=True).encode()).hexdigest(),
        'page_count': len(pages), 'chat_model': LLM_MODEL, 'embedding_model': EMBED_MODEL,
        'reranker': RERANK_MODEL, 'rrf_constant': 60,
        'packages': {name: importlib.metadata.version(name) for name in
                     ['rank-bm25', 'langchain-text-splitters', 'sentence-transformers', 'qdrant-client']},
        **({'chunk_count': len(ladder.chunks), 'chunk_size': ladder.chunk_size,
            'chunk_overlap': ladder.overlap, 'candidates': ladder.candidates} if ladder else {}),
    }


def evaluate(ladder, cases, rungs, k):
    scored = [c for c in cases if c['pages']]
    if not scored:
        raise ValueError("No cases have evidence labels; review labels before scoring")
    rows, details = [], []
    for name in rungs:
        hits, rrs, elapsed = [], [], 0.0
        for case in scored:
            start = time.perf_counter()
            ranked = ladder.search(name, case['question'], k)
            ms = 1000 * (time.perf_counter() - start)
            elapsed += ms
            hit, rr = score_case(case, ranked, ladder.page_of)
            hits.append(hit); rrs.append(rr)
            details.append({'case': case['id'], 'question': case['question'], 'retriever': name,
                            'hit': hit, 'rr': rr, 'ms': round(ms, 2),
                            'results': ladder.hits(ranked), 'trace': ladder.trace})
        rows.append({'retriever': name, 'hit_rate': round(sum(hits) / len(hits), 3),
                     'mrr': round(sum(rrs) / len(rrs), 3), 'k': k, 'cases': len(scored),
                     'ms_per_query': round(elapsed / len(scored), 2)})
    return rows, details


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('command', choices=['inspect', 'cases', 'label', 'compare', 'score'])
    ap.add_argument('--page', help='Read one page by its corpus-relative name')
    ap.add_argument('--cases', help='Reviewed JSON list of eval cases; otherwise use workspace/seed')
    ap.add_argument('--question', help='Question for compare (no answer labels are passed to search)')
    ap.add_argument('--rungs', nargs='+', choices=[*RUNGS, 'cohere_rerank'], default=list(RUNGS))
    ap.add_argument('--k', type=int, default=4)
    ap.add_argument('--chunk-size', type=int, default=800)
    ap.add_argument('--overlap', type=int, default=120)
    ap.add_argument('--candidates', type=int, default=12)
    ap.add_argument('--save', action='store_true', help='For score only: save actual eval_cases and ladder through helpers.workspace')
    args = ap.parse_args(argv)
    if args.k < 1 or args.candidates < args.k:
        ap.error('Require candidates >= k >= 1')
    if args.save and args.command != 'score':
        ap.error('--save is only supported for score')
    # Libraries and workspace notices may print; stdout remains one JSON value.
    with redirect_stdout(sys.stderr):
        pages = read_pages()
        info = provenance(pages)
        if args.command == 'inspect':
            if args.page:
                if args.page not in pages:
                    raise ValueError('Unknown corpus page: ' + args.page)
                result = {**info, 'page': args.page, 'text': pages[args.page]}
            else:
                result = {**info, 'pages': [{'page': p, 'digest': ' '.join(t.split())[:240]}
                                          for p, t in pages.items()]}
        elif args.command == 'label':
            result = {**info, 'status': 'proposals requiring human review', 'cases': label_pages(pages)}
        elif args.command == 'cases':
            result = {**info, 'cases_source': 'file' if args.cases else ws.source('eval_cases'),
                      'cases': load_cases(pages, args.cases)}
        else:
            if args.command == 'compare' and not args.question:
                ap.error('compare requires --question')
            cases = load_cases(pages, args.cases) if args.command == 'score' else None
            ladder = Ladder(pages, args.chunk_size, args.overlap, args.candidates)
            try:
                startup = ladder.prepare(args.rungs)
                result = {**provenance(pages, ladder), 'startup_ms': startup,
                          'timing_note': 'Search timings exclude index construction/model loading; include query embeddings and query expansion where used. Single sequential run, not a latency benchmark.'}
                if args.command == 'compare':
                    result.update(question=args.question, k=args.k, rankings={})
                    for name in args.rungs:
                        start = time.perf_counter()
                        ranked = ladder.search(name, args.question, args.k)
                        result['rankings'][name] = {'ms': round(1000 * (time.perf_counter() - start), 2),
                                                   'results': ladder.hits(ranked), 'trace': ladder.trace}
                    result['scratch_bm25'] = ladder.hits(ladder.scratch.search(args.question, args.k))
                else:
                    rows, details = evaluate(ladder, cases, args.rungs, args.k)
                    result.update(cases_source='file' if args.cases else ws.source('eval_cases'),
                                  cases=cases, skipped_cases=[c['id'] for c in cases if not c['pages']],
                                  ladder=rows, per_case=details, saved=False)
                    if args.save:
                        ws.save('eval_cases', cases)
                        ws.save('ladder', rows)
                        result['saved'] = True
            finally:
                ladder.close()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
