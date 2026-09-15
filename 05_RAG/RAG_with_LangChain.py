import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # RAG with LangChain

    A model answers from what it was trained on, so it guesses at your product's specifics. Retrieval fixes that: find the passages first, then hand them to the model with the question. You build that twice, by hand and then with LangChain, over the pages your workspace produced.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    The retrieval gap, what pasting the whole corpus costs per call, then retrieval as three moves: embed, find the nearest chunks, paste them in. From scratch in thirty lines, rebuilt with a splitter, an embeddings endpoint, and a vector store.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    A corpus rendered from your charter, prompts, transcripts, and vibe checks, indexed locally, and a baseline answer saved for every vibe check.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Production retrieval means structure-aware chunking, incremental re-indexing, hybrid search, and faithfulness checks in CI. Show your team the vibe check that retrieval fixed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 35 minutes
    **Reads:** charter, prompts, transcripts, vibe_checks
    **Writes:** corpus, baseline_runs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    The chat model and the embeddings endpoint come from `.env`. The setup cell renders your charter, prompt outputs, transcripts, and vibe checks into markdown pages under the corpus artifact. Those pages are what you retrieve over, except the vibe checks page, which is the answer key. The vibe check inputs are the questions.
    """)
    return


@app.cell
def _():
    import time
    from operator import itemgetter

    import numpy as np
    from openai import OpenAI

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, EMBED_BASE, EMBED_MODEL, require, budget
    from helpers import workspace as ws, ui
    from helpers.llm import chat_model, client, embeddings_model
    from helpers.display import show
    from helpers.rag import format_docs

    require("OPENAI_API_KEY")
    PAGES = ws.build_corpus()
    CORPUS_DIR = ws.load_path("corpus")
    CORPUS = {}
    for p in PAGES:
        rel = p.relative_to(CORPUS_DIR).as_posix()
        if not rel.startswith("wiki/") and rel != "vibe_checks.md":   # the vibe checks page is the answer key, so it stays out
            CORPUS[rel] = p.read_text(encoding="utf-8")
    VIBES = ws.load("vibe_checks")
    QUESTIONS = [v["input"] for v in VIBES]
    chars = sum(len(t) for t in CORPUS.values())
    print(f"✅ chat {LLM_MODEL}; embeddings {EMBED_MODEL}; {len(CORPUS)} pages, {chars:,} chars; {len(QUESTIONS)} questions")
    return (
        CORPUS,
        EMBED_BASE,
        EMBED_MODEL,
        LLM_MODEL,
        QUESTIONS,
        VIBES,
        budget,
        chat_model,
        client,
        embeddings_model,
        format_docs,
        itemgetter,
        np,
        show,
        time,
        ui,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with both model names, a page count above five, and a question count of at least five. Stop here if the page count is one: only the charter rendered, so the prompts and transcripts artifacts are missing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Learn
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1 of 7 — See the gap

    Ask the model one vibe check with no source text attached. It answers fluently. Compare the answer with what the vibe check says a good answer must include. A confident answer that misses the exact setting, path, or approver is the gap retrieval closes.
    """)
    return


@app.cell
def _(LLM_MODEL, QUESTIONS, VIBES, client, show):
    chat = client()


    def ask_plain(question: str) -> str:
        """Ask the chat model directly, with no retrieved context."""
        resp = chat.chat.completions.create(model=LLM_MODEL, messages=[{"role": "user", "content": question}])
        return resp.choices[0].message.content.strip()


    QUESTION = QUESTIONS[0]
    print("Q:", QUESTION)
    print("A good answer includes:", VIBES[0]["expected"], "\n")
    show(ask_plain(QUESTION))
    return QUESTION, ask_plain, chat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the question, the expected content, and a fluent answer with no page named as a source. Stop here if the model refuses to answer at all: check that `LLM_MODEL` in `.env` is a chat model.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 7 — What it costs to paste everything

    Before building retrieval, measure the alternative: paste every page into the prompt and ask. Streaming shows when the first token arrives, and that wait is mostly the server reading the prompt. Two orderings, two calls each. With the corpus first and the question last, a server with a prefix cache reuses the corpus on the second call. With the question first, every byte after it shifts, so the cache is useless. Four calls, and the only thing that changes between them is where the question sits.
    """)
    return


@app.cell
def _(CORPUS, LLM_MODEL, QUESTION, QUESTIONS, budget, chat, time, ui):
    N_PAGES = budget(len(CORPUS), 6)  # the first pages of the corpus, as many as fit the window
    PASTED = '\n\n'.join((f'# {name}\n{text}' for name, text in list(CORPUS.items())[:N_PAGES]))
    Q1, Q2 = (QUESTION, QUESTIONS[1] if len(QUESTIONS) > 1 else QUESTION)
    STYLE = 'Answer in one sentence.'

    def corpus_first(question: str) -> list:
        """The stable text first, the varying question last: a prefix a cache can reuse."""
        return [{'role': 'system', 'content': f'Knowledge base:\n\n{PASTED}\n\n{STYLE}'}, {'role': 'user', 'content': question}]

    def question_first(question: str) -> list:
        """The varying question first: everything after it shifts, so nothing is reusable."""
        return [{'role': 'user', 'content': f'{question}\n\n{STYLE}\n\nKnowledge base:\n\n{PASTED}'}]

    def first_token(messages: list, usage: bool=True) -> tuple:
        """Milliseconds to the first streamed token, plus prompt and cached tokens if the server reports usage."""
        t0 = time.perf_counter()
        ms = prompt_tokens = cached = None
        extra = {'stream_options': {'include_usage': True}} if usage else {}
        try:
            stream = chat.chat.completions.create(model=LLM_MODEL, messages=messages, stream=True, **extra)
        except Exception as e:
            if usage and 'stream_options' in str(e):
                return first_token(messages, usage=False)
            raise
        for chunk in stream:  # noqa: BLE001  a server that does not know stream_options rejects the whole call
            delta = chunk.choices[0].delta if chunk.choices else None
            if ms is None and delta and (delta.content or getattr(delta, 'reasoning_content', None) or getattr(delta, 'reasoning', None)):
                ms = round(1000 * (time.perf_counter() - t0))
            if chunk.usage:
                prompt_tokens = chunk.usage.prompt_tokens
                details = chunk.usage.prompt_tokens_details
                cached = details.cached_tokens if details else None
        return (ms, prompt_tokens, cached)
    ROWS = []
    for ordering, build in (('corpus first', corpus_first), ('question first', question_first)):
        for call, q in ((1, Q1), (2, Q2)):
            with ui.spinner(f'{ordering}, call {call}'):
                ms, ptok, cached = first_token(build(q))
            ROWS.append({'ordering': ordering, 'call': call, 'first_token_ms': ms, 'prompt_tokens': ptok, 'cached_tokens': cached})

    def cell(v, missing: str) -> str:
        return missing if v is None else f'{v:,}'
    print(f'{N_PAGES} pages pasted, {len(PASTED):,} chars; two questions, each ordering asked Q1 then Q2\n')
    print(f"{'ordering':<16}{'call':>5}{'first token ms':>16}{'prompt tokens':>15}{'cached tokens':>15}")
    for _r in ROWS:
        print(f"{_r['ordering']:<16}{_r['call']:>5}{cell(_r['first_token_ms'], 'no token'):>16}{cell(_r['prompt_tokens'], 'not reported'):>15}{cell(_r['cached_tokens'], 'not reported'):>15}")

    def ms_of(ordering: str, call: int):
        return next((r['first_token_ms'] for r in ROWS if r['ordering'] == ordering and r['call'] == call))
    a1, a2, b1, b2 = (ms_of('corpus first', 1), ms_of('corpus first', 2), ms_of('question first', 1), ms_of('question first', 2))
    cached_second = next((r['cached_tokens'] for r in ROWS if r['ordering'] == 'corpus first' and r['call'] == 2))
    if cached_second:
        print(f'\nThe server reports {cached_second:,} cached prompt tokens on the second corpus-first call: that is the prefix cache.')
    elif all((v for v in (a1, a2, b1, b2))) and a2 * 1.5 < a1 and (not b2 * 1.5 < b1):
        print(f'\nThe second corpus-first call reached its first token {a1 / a2:.1f}x faster than the first, and question-first did not: that is the prefix cache.')
    else:
        print('\nNo cache signal from this server: the first-token times are alike and usage reports no cached tokens, so the corpus is read in full on every call.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a four-row table with a first-token time per call and, where the server reports usage, prompt and cached tokens, then one sentence saying whether a cache showed. Stop here if a call raises a context length error: lower `N_PAGES` so the pasted corpus fits the model's window.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What the table says

    Every call reads the corpus before it writes a word. A prefix cache changes the price of that reading:

    | | Roughly |
    |---|---|
    | Writing a prefix into the cache | more than an ordinary input token |
    | Reading it back | an order of magnitude less |
    | Break-even | about one re-read |

    Ordering decides whether you get it. Anything that varies before the stable text, a timestamp, a user id, the question, invalidates every token after it: same tokens, same answer, full price. Retrieval is the other way to keep the prefix small: send only the passages that matter and the prompt stays short with or without a cache.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which of the four calls was cheapest, and what in the table tells you? If your corpus grew tenfold, which cost grows with it under each ordering, and at what point does retrieval win even on a server with a cache?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 7 — RAG from scratch

    Retrieval is three moves. Embed the chunks and the question into vectors. Find the chunks whose vectors sit closest to the question. Paste those chunks into the prompt. Here it is by hand over every corpus page, so nothing is hidden. The chunker is a slice with an overlap; the ranking is one line of cosine similarity.
    """)
    return


@app.cell
def _(CORPUS, EMBED_BASE, EMBED_MODEL, QUESTION, ask_plain, client, np, show):
    embed_client = client(base_url=EMBED_BASE)

    def embed(texts, batch=64):
        """Embed a list of strings -> one NumPy row per string."""
        out = []
        for i in range(0, len(texts), batch):
            resp = embed_client.embeddings.create(model=EMBED_MODEL, input=texts[i:i + batch])
            out = out + [d.embedding for d in resp.data]
        return np.array(out)
    chunks, page_of = ([], [])
    for name, text in CORPUS.items():
        for i in range(0, len(text), 700):
    # Fixed-size chunks with an overlap, tagged with the page they came from.
            chunks.append(text[i:i + 800])
            page_of.append(name)
    vecs = embed(chunks)
    qvec = embed([QUESTION])[0]

    def top_k(qvec, vecs, k=4):
        """Indices of the k chunks closest to the question (cosine similarity)."""
        sims = vecs @ qvec / (np.linalg.norm(vecs, axis=1) * np.linalg.norm(qvec))
        return sims.argsort()[::-1][:k]
    idx = top_k(qvec, vecs, k=4)
    print(f'{len(chunks)} chunks; pages retrieved:', [page_of[i] for i in idx])
    context = '\n\n'.join((chunks[i] for i in idx))
    show(ask_plain(f'Use ONLY this context to answer.\n\nContext:\n{context}\n\nQuestion: {QUESTION}'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the chunk count, the pages the four closest chunks came from, then an answer that uses the expected setting or path. Stop here if the retrieved pages are all transcripts and the answer is still vague: the charter page missed the top four, so raise `k` to 8.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 7 — The same pipeline in LangChain

    The library replaces three pieces. The splitter respects paragraph and sentence boundaries instead of cutting mid-word. The embeddings wrapper batches calls. The vectors go into Qdrant, an on-disk database built for nearest-neighbour search, instead of a NumPy array. It runs embedded in this process, so there is no server to start. Rerunning the cell reuses the index.
    """)
    return


@app.cell
def _(CORPUS, embeddings_model, time, ui):
    from langchain_core.documents import Document
    from langchain_openai import OpenAIEmbeddings
    from langchain_qdrant import QdrantVectorStore
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from qdrant_client.models import Distance, VectorParams
    from helpers.vectorstore import COLLECTION, LOCAL_QDRANT, local_client
    embeddings = embeddings_model()
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
    docs = splitter.split_documents([Document(page_content=t, metadata={'page': n}) for n, t in CORPUS.items()])  # let the embed server tokenize its own input
    print(f'{len(CORPUS)} pages -> {len(docs)} chunks')
    REINDEX = False
    client_1 = local_client()
    ready = client_1.collection_exists(COLLECTION) and client_1.count(COLLECTION).count == len(docs)
    if ready and (not REINDEX):  # True forces a rebuild, for example after changing the chunking
        vectorstore = QdrantVectorStore(client=client_1, collection_name=COLLECTION, embedding=embeddings)
        print(f"Reusing the local '{COLLECTION}' collection ({len(docs)} chunks in {LOCAL_QDRANT.name}/).")  # one embedded Qdrant handle per process; rerunning this cell is safe
    else:
        if client_1.collection_exists(COLLECTION):
            client_1.delete_collection(COLLECTION)
        dim = len(embeddings.embed_query('dimension probe'))
        client_1.create_collection(COLLECTION, vectors_config=VectorParams(size=dim, distance=Distance.COSINE))
        vectorstore = QdrantVectorStore(client=client_1, collection_name=COLLECTION, embedding=embeddings)
        t0 = time.time()
        with ui.spinner('embedding and indexing the corpus'):
            vectorstore.add_documents(docs)
        print(f'Indexed {len(docs)} chunks into local Qdrant in {time.time() - t0:.0f}s.')
    return (vectorstore,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the page and chunk counts, then either an indexing time or a reuse line. Stop here if you see a storage folder already accessed error: another kernel holds the local Qdrant folder, so shut that kernel down and rerun.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    What did the library add over the from-scratch version, in one sentence each for the splitter, the embeddings wrapper, and the vector store?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 7 — Wire it into a chain

    LangChain composes the steps with `|`, the way a shell pipes commands. The chain takes a question, runs the retriever, fills the prompt, calls the model, and returns text in one `invoke`. Read it top to bottom: the question goes to the retriever, `format_docs` joins the chunks, and the prompt, model, and parser turn that into an answer.
    """)
    return


@app.cell
def _(QUESTION, chat_model, format_docs, itemgetter, show, vectorstore):
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI

    llm = chat_model(temperature=0)

    prompt = ChatPromptTemplate.from_template(
        "You are the assistant described in the product charter. Answer from the context only.\n"
        "If the answer is not in the context, say so in one sentence.\n\n"
        "Context:\n{context}\n\nQuestion: {question}"
    )


    def with_retriever(retriever):
        """question -> retriever -> prompt -> model -> text"""
        return ({"context": itemgetter("question") | retriever | format_docs,
                 "question": itemgetter("question")}
                | prompt | llm | StrOutputParser())


    rag_chain = with_retriever(vectorstore.as_retriever(search_kwargs={"k": 4}))
    show(rag_chain.invoke({"question": QUESTION}))
    return (with_retriever,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the same vibe check answered from the corpus, with the setting or path the expected text names. Stop here if the answer says the context does not contain it: print the retrieved chunks and check which pages they came from.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Create
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 7 — Retrieval quality is a dial

    The chain is only as good as what the retriever feeds it. `k`, the number of chunks fetched, is the simplest dial. Too few and the passage never reaches the model. More chunks give a better chance the answer is supported, at the cost of a longer prompt. Run the same question at two settings and compare.
    """)
    return


@app.cell
def _(QUESTION, QUESTIONS, show, vectorstore, with_retriever):
    def answer_with_k(question: str, k: int):
        """The answer and the chunks the model saw."""
        retriever = vectorstore.as_retriever(search_kwargs={'k': k})
        contexts = [d.page_content for d in retriever.invoke(question)]
        return (with_retriever(retriever).invoke({'question': question}), contexts)
    SPLIT_Q = QUESTIONS[1] if len(QUESTIONS) > 1 else QUESTION
    print('Q:', SPLIT_Q)
    for _k in (1, 8):
        _answer, _contexts = answer_with_k(SPLIT_Q, _k)
        print(f'── k = {_k}: {len(_contexts)} chunks, {sum((len(c) for c in _contexts)):,} chars of context')
        show(_answer)
    return SPLIT_Q, answer_with_k


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see two answers to one question, with the chunk and character counts for each. Stop here if both answers look equally good to you: that is normal, and it is why retrieval gets scored against reference answers rather than read by eye.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    At `k = 1`, which chunk carried the answer, and what in the question made its vector land close? Would a different phrasing of the question have missed it?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 7 of 7 — Answer every vibe check and save

    Run the chain over every vibe check and keep the record flat: question, answer, and the chunks the model saw. That file is the baseline the retrieval ladder and the RAGAS scores are measured against. Keep the contexts. Without them nobody can tell whether a wrong answer was a retrieval miss or a model miss.
    """)
    return


@app.cell
def _(LLM_MODEL, VIBES, answer_with_k, budget, ui, ws):
    K = 4
    RUNS = []
    for v in ui.track(VIBES[:budget(len(VIBES), 3)], 'answering'):
        _answer, _contexts = answer_with_k(v['input'], K)
        RUNS.append({'question': v['input'], 'answer': _answer, 'contexts': _contexts, 'expected': v['expected'], 'k': K, 'model': LLM_MODEL})
    ws.save('baseline_runs', RUNS)
    for _r in RUNS:
        print(f"Q: {_r['question']}\n   expects: {_r['expected']}\n   got: {_r['answer'][:200]}\n")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with one row per vibe check, then each question with its expected content and the answer. Stop here if a row has an empty contexts list: the retriever returned nothing, so the index is empty.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Reading two answers side by side is the trap Task 6 named. Let your judge decide instead. Score the `k = 1` and `k = 8` answers with a judge that sees what the vibe check expects. Then change one thing, the chunk size or `k`, and score again. Tell a teammate which change moved the score and which one only changed the wording.
    """)
    return


@app.cell
def _(SPLIT_Q, VIBES, answer_with_k):
    from helpers.judge import make_judge
    quality = make_judge('quality', 'Question: {question}\nA good answer includes: {reference}\nAnswer: {response}\n\nScore 0-10 how completely and accurately the answer covers what a good answer includes.', needs_reference=True)
    reference = next((v['expected'] for v in VIBES if v['input'] == SPLIT_Q), '')
    for _k in (1, 8):
        _answer, _ = answer_with_k(SPLIT_Q, _k)
        verdict = quality({'question': SPLIT_Q, 'response': _answer, 'reference': reference})
        print(f"k={_k}: score={verdict['score']}  {verdict['rationale']}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Grow
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## From prototype to production

    | What we built | Production equivalent |
    |---|---|
    | Pages rendered from four workspace artifacts | Many sources with cleaning, metadata, and structure-aware chunking |
    | A single dense retriever | Hybrid search with a reranker on top |
    | A fixed `k` picked by hand | Retrieval settings tuned against an eval set |
    | Reindex when the chunk count changes | Incremental pipelines that reindex as documents change |
    | One embedded Qdrant collection on disk | A replicated vector database with access control |
    | Reading the answer | Faithfulness and context checks in CI |
    | Four timed calls | Cache hit rate tracked per request |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Re-index on a schedule or on change, never when someone remembers.
    - Every answer carries the chunk ids it was grounded on.
    - Access control on the index so a user only retrieves pages they may read.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Carry each chunk's page name as metadata and have the chain return the answer plus the pages it drew from, so every answer is checkable.
    - Add a metadata filter so the retriever only searches transcripts, and compare with the charter-only view on the same question.
    - Reindex the same chunks with a second embedding model into a second collection and count which one retrieves the charter page more often.
    """)
    return


if __name__ == "__main__":
    app.run()
