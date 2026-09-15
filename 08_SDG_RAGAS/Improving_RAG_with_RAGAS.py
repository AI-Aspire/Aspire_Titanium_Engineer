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
    # Improving RAG with RAGAS

    A RAG pipeline that works is not the same as one you can improve. To improve it you need questions with known answers and metrics that separate retrieval failures from generation failures. This notebook generates the questions from your corpus pages, scores the pipeline, changes one thing, and scores it again.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Why a weak pipeline on purpose, how a synthetic test set is written by hand for one chunk and generated for the rest, and what four RAGAS metrics each measure.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    A test set generated from your corpus, RAGAS scores on your pipeline, one retrieval change, and the scores again.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Production teams keep the test set under version control and rerun it on every retrieval change. Tell your team your weakest metric and which way it moved.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 35 minutes
    **Reads:** corpus
    **Writes:** testset, ragas_scores
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    This module has its own environment because RAGAS pins the LangChain 0.3 line. Three chat models come from `.env`: the pipeline under test on `LLM_MODEL`, the RAGAS judges on `RAGAS_MODEL`, and the test set generator on `SDG_MODEL`. Each falls back to the one before it. A different judge model avoids a model grading its own work.
    """)
    return


@app.cell
def _():
    import concurrent.futures, json, time, warnings

    warnings.filterwarnings("ignore")
    import pandas as pd
    from langchain_core.documents import Document
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from langchain_qdrant import QdrantVectorStore
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from qdrant_client import QdrantClient
    from qdrant_client.models import Distance, VectorParams

    from helpers.config import (KEY, LLM_BASE, LLM_MODEL, EMBED_BASE, EMBED_MODEL,
                                RAGAS_BASE, RAGAS_MODEL, SDG_MODEL, LLM_TIMEOUT, require, budget)
    from helpers import workspace as ws, ui
    from helpers.llm import chat_model, embeddings_model, judge_model
    from helpers.sdg import tolerant_personas
    from helpers.display import show
    from helpers.rag import format_docs
    from helpers.judge import parse_json

    require("OPENAI_API_KEY")
    app_llm = chat_model(temperature=0)
    judge_llm = judge_model()
    sdg_llm = chat_model(model=SDG_MODEL, base_url=RAGAS_BASE, temperature=0)
    embeddings = embeddings_model()

    CORPUS_DIR = ws.load_path("corpus")
    PAGES = {}
    for p in sorted(CORPUS_DIR.rglob("*.md")):
        rel = p.relative_to(CORPUS_DIR).as_posix()
        if not rel.startswith("wiki/") and rel != "vibe_checks.md":   # the wiki is an index; the vibe checks page is an answer key
            PAGES[rel] = p.read_text(encoding="utf-8")
    print(f"✅ pipeline {LLM_MODEL}; judges {RAGAS_MODEL}; generator {SDG_MODEL}; embeddings {EMBED_MODEL}; {len(PAGES)} pages")
    return (
        ChatPromptTemplate,
        Distance,
        Document,
        LLM_TIMEOUT,
        PAGES,
        QdrantClient,
        QdrantVectorStore,
        RecursiveCharacterTextSplitter,
        StrOutputParser,
        VectorParams,
        app_llm,
        budget,
        concurrent,
        embeddings,
        format_docs,
        judge_llm,
        parse_json,
        pd,
        sdg_llm,
        show,
        time,
        tolerant_personas,
        ui,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line naming three chat models, the embedding model, and a page count above five. Stop here if the import of `ragas` fails later: you are in the shared environment, so run `uv sync` in this module's folder and pick its kernel.
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
    ## Task 1 of 5 — A weak pipeline on purpose

    Index the corpus pages into a disposable in-memory store and answer with a deliberately small `k` of 2, so the retriever fetches two chunks. The prompt stays fixed for the rest of the notebook. When the scores move later, retrieval moved them.
    """)
    return


@app.cell
def _(
    ChatPromptTemplate,
    Distance,
    Document,
    PAGES,
    QdrantClient,
    QdrantVectorStore,
    RecursiveCharacterTextSplitter,
    StrOutputParser,
    VectorParams,
    app_llm,
    embeddings,
    format_docs,
    show,
    ui,
):
    def build_store(chunk_size: int, chunk_overlap: int, name: str):
        """Split the pages, embed the chunks, and return a fresh in-memory vector store."""
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        docs = splitter.split_documents([Document(page_content=t, metadata={"page": n}) for n, t in PAGES.items()])
        qdrant = QdrantClient(":memory:")
        dim = len(embeddings.embed_query("dimension probe"))
        qdrant.create_collection(name, vectors_config=VectorParams(size=dim, distance=Distance.COSINE))
        store = QdrantVectorStore(client=qdrant, collection_name=name, embedding=embeddings)
        with ui.spinner(f"embedding {len(docs)} chunks"):
            store.add_documents(docs)
        return store, docs


    RAG_PROMPT = ChatPromptTemplate.from_template(
        "You are the assistant described in the product charter. Answer from the context only.\n"
        "If the answer is not in the context, say so in one sentence.\n\n"
        "Context:\n{context}\n\nQuestion: {question}")
    generate = RAG_PROMPT | app_llm | StrOutputParser()


    def run_rag(retriever, questions: list) -> list:
        """Answer each question and keep the retrieved context, in the row shape RAGAS reads."""
        rows = []
        for q in ui.track(questions, "answering"):
            docs = retriever.invoke(q["question"])
            rows.append({"user_input": q["question"], "retrieved_contexts": [d.page_content for d in docs],
                         "response": generate.invoke({"context": format_docs(docs), "question": q["question"]}),
                         "reference": q["reference"]})
        return rows


    CHUNK_SIZE = 800
    store, chunks = build_store(CHUNK_SIZE, 120, "corpus_800")
    baseline_retriever = store.as_retriever(search_kwargs={"k": 2})
    probe = "What does the product refuse to do?"
    show(generate.invoke({"context": format_docs(baseline_retriever.invoke(probe)), "question": probe}))
    return CHUNK_SIZE, baseline_retriever, build_store, chunks, run_rag, store


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the chunk count while embedding, then a short answer to the probe question drawn from the charter page. Stop here if the answer says the context does not contain it: print the two retrieved chunks and check which pages they came from.
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
    ## Task 2 of 5 — Generate the test set

    To score retrieval you need questions with known answers. The idea by hand: show the model one chunk, ask for a question that chunk answers and the answer drawn only from it. RAGAS does the same at scale. It builds a knowledge graph over the pages, then writes single-hop and multi-hop questions from different personas in varied styles, some terse, some misspelt, the way users type. If your workspace already holds a test set, the cell reuses it so the scores stay comparable from run to run. Delete the file to regenerate.
    """)
    return


@app.cell
def _(chunks, parse_json, sdg_llm, show):
    sample = chunks[min(3, len(chunks) - 1)].page_content
    prompt = ("Read this passage and write ONE question it answers, plus the answer drawn only from it.\n\n"
              f"Passage:\n{sample}\n\nReturn ONLY JSON: {{\"question\": \"...\", \"answer\": \"...\"}}")
    reply = sdg_llm.invoke(prompt)
    example = parse_json(reply.content if isinstance(reply.content, str) else str(reply.content)) or {}
    show(f"By hand, from one chunk:\n\nQ: {example.get('question', '(no clean JSON returned)')}\n\nA: {example.get('answer', '')}")
    return


@app.cell
def _(
    Document,
    LLM_TIMEOUT,
    PAGES,
    budget,
    embeddings,
    pd,
    sdg_llm,
    time,
    tolerant_personas,
    ui,
    ws,
):
    from ragas import RunConfig
    from ragas.embeddings import LangchainEmbeddingsWrapper
    from ragas.llms import LangchainLLMWrapper
    from ragas.testset import TestsetGenerator
    from ragas.testset.persona import Persona
    PERSONAS = [Persona(name='engineer', role_description='Files a ticket when something blocks their work and wants the exact next step.'), Persona(name='helpdesk lead', role_description='Runs the queue and wants repeat questions answered before they reach a person.')]
    # The personas are the people your charter already names. Naming them here
    # skips a generation step and keeps the names short.
    tolerant_personas()
    N_QUESTIONS = budget(8, 4)
    if ws.source('testset') == 'workspace':
        TESTSET = ws.load('testset')
        gen_df = pd.DataFrame(TESTSET).rename(columns={'question': 'user_input', 'synthesizer': 'synthesizer_name'})
        print(f"reusing {len(TESTSET)} questions from {ws.path('testset')}; delete the file to regenerate")
    # RAGAS asks the model which persona each question is for and looks the reply
    # up by exact name. A reply like "engineer (Software Engineer)" would be a
    # KeyError after the whole graph was built; this makes the lookup forgiving.
    else:
        generator = TestsetGenerator(llm=LangchainLLMWrapper(sdg_llm), embedding_model=LangchainEmbeddingsWrapper(embeddings), persona_list=PERSONAS)
        page_docs = [Document(page_content=t, metadata={'page': n}) for n, t in PAGES.items()]
        _t0 = time.time()
        with ui.spinner('building the knowledge graph and writing questions'):
            generated = generator.generate_with_langchain_docs(page_docs, testset_size=N_QUESTIONS, run_config=RunConfig(timeout=int(LLM_TIMEOUT), max_workers=3, max_retries=4))
        gen_df = generated.to_pandas()
        TESTSET = [{'question': r['user_input'], 'reference': r['reference'], 'synthesizer': r.get('synthesizer_name', '')} for _, r in gen_df.iterrows()]
        ws.save('testset', TESTSET)
        print(f'{len(TESTSET)} of {N_QUESTIONS} questions in {time.time() - _t0:.0f}s')
        if len(TESTSET) < N_QUESTIONS:
            print('ℹ fewer than asked: a synthesizer skipped a question it could not build from this corpus')
    gen_df[[c for c in ('user_input', 'reference', 'synthesizer_name') if c in gen_df.columns]]
    return LangchainEmbeddingsWrapper, LangchainLLMWrapper, RunConfig, TESTSET


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a table of questions with the synthesizer that wrote each one, and a count. Some are single-hop and some need two pages. Stop here if you get zero questions, which means the corpus was too small to build a graph from.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Read the generated questions. Which one would a real user never type, and which one is harder than anything in your vibe checks?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 5 — Run the baseline over the test set

    Answer every generated question with the weak pipeline, keeping the retrieved chunks for each. Those chunks are what RAGAS needs to tell a retrieval miss from a generation miss.
    """)
    return


@app.cell
def _(TESTSET, baseline_retriever, run_rag, show, time):
    _t0 = time.time()
    baseline_rows = run_rag(baseline_retriever, TESTSET)
    print(f'answered {len(baseline_rows)} questions in {time.time() - _t0:.0f}s')
    show('Q: ' + baseline_rows[0]['user_input'] + '\n\nBaseline answer: ' + baseline_rows[0]['response'][:400])
    return (baseline_rows,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the count of answered questions and the first question with its baseline answer. Stop here if an answer is empty: the pipeline model timed out, so raise the timeout on `app_llm`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 5 — Measure with RAGAS

    Four metrics, each a judge call. Faithfulness: is every claim in the answer supported by the retrieved chunks. Answer relevancy: does the answer address the question. Context precision: are the retrieved chunks the ones the reference needs, ranked high. Context recall: did retrieval surface what the reference answer needs at all. The last two are the ones a small `k` hurts.
    """)
    return


@app.cell
def _(
    LLM_TIMEOUT,
    LangchainEmbeddingsWrapper,
    LangchainLLMWrapper,
    RunConfig,
    baseline_rows,
    concurrent,
    embeddings,
    judge_llm,
    time,
):
    from ragas import EvaluationDataset, evaluate
    from ragas.metrics import Faithfulness, LLMContextPrecisionWithReference, LLMContextRecall, ResponseRelevancy
    METRICS = [Faithfulness(), ResponseRelevancy(strictness=1), LLMContextPrecisionWithReference(), LLMContextRecall()]
    judge = LangchainLLMWrapper(judge_llm)
    judge_emb = LangchainEmbeddingsWrapper(embeddings)
    COLUMNS = ['faithfulness', 'answer_relevancy', 'context_precision', 'context_recall']

    def score(rows: list) -> dict:
        """Mean of each metric over the rows, keyed by the four column names above."""

        def _run():
            return evaluate(EvaluationDataset.from_list(rows), metrics=METRICS, llm=judge, embeddings=judge_emb, run_config=RunConfig(timeout=int(LLM_TIMEOUT), max_retries=4, max_workers=3))  # a worker thread has no running event loop, so RAGAS gets a clean one of its own
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            means = pool.submit(_run).result().to_pandas().select_dtypes('number').mean()
        out = {}
        for col, value in means.items():
            key = 'context_precision' if 'context_precision' in col else col
            if key in COLUMNS:
                out[key] = round(float(value), 3)
        return out
    _t0 = time.time()
    baseline_scores = score(baseline_rows)
    print(f'scored in {time.time() - _t0:.0f}s')
    baseline_scores
    return COLUMNS, baseline_scores, score


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the scoring time and a dict with the four metric names and values between 0 and 1. Stop here if a value is NaN: the judge could not parse one row, which is normal for one row and a problem for all of them, so rerun once.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which of the four metrics is lowest, and does that point at retrieval or at the model? What one change would you make first?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 5 — Change one thing and measure again

    Raise `k` from 2 to 6 and run the same evaluation. Same prompt, same questions, same judge, so any movement is retrieval. Then save both rows. Context recall should climb. Faithfulness and relevancy can rise, hold, or dip, because more context is also more text to wander into. With a handful of questions the numbers are noisy; recall is the solid signal.
    """)
    return


@app.cell
def _(
    CHUNK_SIZE,
    COLUMNS,
    TESTSET,
    baseline_scores,
    pd,
    run_rag,
    score,
    store,
    ui,
    ws,
):
    improved_retriever = store.as_retriever(search_kwargs={"k": 6})
    improved_rows = run_rag(improved_retriever, TESTSET)
    improved_scores = score(improved_rows)

    SCORES = [{"variant": "baseline k=2", **baseline_scores, "k": 2, "chunk_size": CHUNK_SIZE},
              {"variant": "improved k=6", **improved_scores, "k": 6, "chunk_size": CHUNK_SIZE}]
    ws.save("ragas_scores", SCORES)
    compare = pd.DataFrame(SCORES).set_index("variant")[COLUMNS].T
    compare["delta"] = compare.iloc[:, 1] - compare.iloc[:, 0]
    compare.index.name = "metric"
    ui.table(compare, title="baseline vs improved, same prompt and questions")
    return SCORES, compare


@app.cell
def _(compare):
    import matplotlib.pyplot as plt
    from helpers.brand import matplotlib_style

    plt.rcParams.update(matplotlib_style())
    ax = compare[[c for c in compare.columns if c != "delta"]].plot.bar(figsize=(8, 3.6), rot=0)
    ax.set_ylim(0, 1.05); ax.set_ylabel("score"); ax.set_xlabel(""); ax.set_title("RAGAS metrics before and after one change")
    for c in ax.containers:
        ax.bar_label(c, fmt="%.2f", padding=2, fontsize=8)
    plt.tight_layout(); plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with two rows written, a table with a delta column, and a bar chart with two bars per metric. Stop here if every delta is exactly zero: both runs used the same retriever, so check that `improved_retriever` has `k` set to 6.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Change a different thing: the chunk size. Rebuild the store at 400 characters, keep `k` at 6, score again, and add the row to the saved scores. Then say which change moved which metric, and which `k` and chunk size you would ship for these questions.
    """)
    return


@app.cell
def _(COLUMNS, SCORES, TESTSET, build_store, pd, run_rag, score, ui, ws):
    MY_CHUNK_SIZE = 400
    small_store, small_chunks = build_store(MY_CHUNK_SIZE, 60, f"corpus_{MY_CHUNK_SIZE}")
    my_rows = run_rag(small_store.as_retriever(search_kwargs={"k": 6}), TESTSET)
    my_scores = score(my_rows)
    SCORES.append({"variant": f"chunks {MY_CHUNK_SIZE} k=6", **my_scores, "k": 6, "chunk_size": MY_CHUNK_SIZE})
    ws.save("ragas_scores", SCORES)
    ui.table(pd.DataFrame(SCORES).set_index("variant")[COLUMNS], title="three variants")
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
    | Eight questions generated from a few pages | Hundreds of questions across the corpus, filtered for quality |
    | A few personas and query styles | Personas and styles tuned to real user traffic |
    | Four metrics run once in a notebook | Metric suites tracked over time per release |
    | `k` and chunk size changed by hand | Sweeps over chunking, retrieval, and rerankers |
    | A before and after chart | An eval gate in CI that blocks a regression |
    | One judge model | Several judges with human spot checks and bias controls |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - The synthetic test set reviewed by a person before it gates anything.
    - Metric thresholds agreed before the change, not after.
    - Generator model and version recorded with every test set.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Inspect the knowledge graph the generator built with `generator.knowledge_graph` and explain why it asked one multi-hop question.
    - Pass a `query_distribution` to weight multi-hop questions higher and see which metric drops first.
    - Wrap the evaluation in a script that exits non-zero when context recall falls below a threshold, and run it before any retrieval change merges.
    """)
    return


if __name__ == "__main__":
    app.run()
