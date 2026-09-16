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
    # Retrieval ladder

    Ask your coding assistant to run real retrieval experiments, then inspect what each method found. Compare dense search, BM25, fusion, reranking, and query expansion on the same questions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Review suggested evidence pages and compare the retrieval methods on identical chunks.

    ### Create
    Measure hit rate, MRR, and search time. Use the per-case results to decide where extra retrieval work helps.

    ### Grow
    Test the smallest retrieval pipeline that meets your quality and latency needs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 40 minutes

    Reads: corpus and vibe checks.

    Writes: eval cases and measured ladder only when you ask the tool to save them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    Open the repository in a coding assistant with file and terminal access. Follow the messages below; the README documents the experiment tools and environment setup.

    Product documentation: [Codex](https://developers.openai.com/codex/), [Claude Code](https://code.claude.com/docs/en/overview), [VS Code Copilot](https://code.visualstudio.com/docs/agents/overview).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ask your assistant

    > Read `06_Advanced_Retrieval/README.md` and inspect `06_Advanced_Retrieval/retrieval_tools.py`. Use the inspect command to show which corpus is active, how many pages it has, and which pages are excluded. Do not run a model experiment yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Every rung uses the same chunks. The tools exclude the wiki index and the vibe-check answer-key page from retrieval. Their results say whether inputs came from your workspace or the seed example.

    Your assistant should execute the repo tool, not substitute its own file search for dense search or BM25. Ask it to show the tool result if the explanation is unclear.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Terms you will use

    | Term | Meaning |
    |---|---|
    | Dense search | Embedding similarity, useful for related meanings |
    | BM25 | Word matching weighted by rarity, frequency, and document length |
    | RRF | Combine ranks from several lists |
    | Cross-encoder | Score a question and candidate passage together |
    | Multi-query | Search several rewrites, then combine the candidates |
    | Hit rate | Fraction of questions with an evidence page in the top results |
    | MRR | Average reciprocal rank of the first result from an evidence page |
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
    ## Task 1 of 4 — Choose the evidence pages

    A score needs an answer key. For each question, identify pages containing evidence for the expected answer. Record page names rather than chunk IDs so the answer key still works if the chunk size changes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ask your assistant

    > Use the label command in `06_Advanced_Retrieval/retrieval_tools.py` to suggest evidence pages for the current vibe-check questions. Show each question, its expected answer, the suggested pages, and relevant passages from those pages.
    >
    > Let me review and correct the suggestions before using them as the answer key. If I question a suggestion, open the page and help me check whether it supports the expected answer. Use an empty page list when no page provides evidence.
    >
    > Keep the proposals in a temporary case file outside the workspace. Apply my corrections and confirm the reviewed answer key. Retain that file for scoring; do not save to the workspace yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Open each suggested page and check whether it contains evidence for answering the question. The tool sends its model only the first 240 characters of each page, so it may miss evidence later in the text.

    A missing evidence page can make a useful result score as a miss. An empty page list excludes the question from retrieval scoring. For an out-of-scope question, include a page only if it supports the expected refusal.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 4 — Dense and sparse

    Dense search can find related meanings when words differ. BM25 can reward exact terms such as setting names and error strings. Test their actual rankings before deciding which works better.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ask your assistant

    > Use `06_Advanced_Retrieval/retrieval_tools.py` to compare dense and BM25 for: My VPN connects but I cannot reach staging.
    >
    > Keep the default chunks and top four results. Show the page names and matching excerpts, including the scratch BM25 ranking. Explain what the code does differently from the library BM25. Use the returned results rather than guessing which retriever should win.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the source, BM25 combines term rarity, frequency saturation, and document-length correction. The scratch version and library use different IDF formulas, so their rankings may differ even with the same tokenizer.

    Dense and sparse scores are on different scales. Compare ranks and evidence quality; do not add the raw scores together.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Recorded experiment: one question</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Seed corpus, 28 pages, 65 chunks, top four. Recorded 2026-09-15 (UTC).</span>
    <table>
    <thead>
    <tr>
    <th>Method</th>
    <th>Top pages, in rank order</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>dense</td>
    <td>prompts/meta-prompt-applied.md; transcripts/t01.md; kb/vpn.md; transcripts/t01.md</td>
    </tr>
    <tr>
    <td>bm25</td>
    <td>transcripts/t01.md; transcripts/t02.md; transcripts/t05.md; charter.md</td>
    </tr>
    </tbody>
    </table>
    <span class="paragraph">These are actual tool results. Repeated page names are different chunks from the same page. Page and chunk references, text hashes, and settings are in <a href="data/recorded_experiments.json">the experiment record</a>.</span></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Pick the question where dense and BM25 disagree most. Which words in the question did BM25 lock onto, and which meaning did dense search chase instead?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 4 — Fuse, rerank, expand

    RRF combines ranks using one divided by sixty plus the rank. Reranking reorders a shortlist; it cannot recover a page absent from that shortlist. Multi-query asks the question several ways before combining and reranking candidates.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ask your assistant

    > Use `06_Advanced_Retrieval/retrieval_tools.py` to run all five rungs with default settings for: My VPN connects but I cannot reach staging. Show the dense and BM25 candidate lists used by RRF, the shortlist before reranking, and the generated query rewrites. Compare the final top four results. Identify a page that moved up or disappeared and trace what happened using the tool output.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Keep the question, chunks, and candidate count fixed while comparing rungs. Check whether a rewrite preserves the original intent and whether the evidence made it into the candidate pool.

    More processing does not guarantee a better ranking. Its benefit depends on the corpus, the question, and the model.
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
    ## Task 4 of 4 — Score the ladder

    Hit rate asks whether an evidence page appears among the top results. Reciprocal rank rewards finding it sooner: rank one gives one, rank four gives one quarter, and a miss gives zero. Average those values to obtain MRR.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ask your assistant

    > Use `06_Advanced_Retrieval/retrieval_tools.py` to score all five rungs with top four results, passing our reviewed case file with `--cases`. If the file or my review is missing, ask me before running.
    >
    > Show hit rate, MRR, search time, and the per-question reciprocal-rank matrix. List skipped questions. Keep the reviewed evidence pages fixed and do not save workspace artifacts.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Recorded experiment: measured ladder</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">5 seed cases; top four; embeddings text-embedding-3-small; rewrites gpt-4.1-mini. Recorded 2026-09-15 (UTC).</span>
    <table>
    <thead>
    <tr>
    <th>Retriever</th>
    <th style="text-align: right;">Hit rate</th>
    <th style="text-align: right;">MRR</th>
    <th style="text-align: right;">Search ms/query</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>dense</td>
    <td style="text-align: right;">0.800</td>
    <td style="text-align: right;">0.533</td>
    <td style="text-align: right;">192.06</td>
    </tr>
    <tr>
    <td>bm25</td>
    <td style="text-align: right;">0.200</td>
    <td style="text-align: right;">0.067</td>
    <td style="text-align: right;">0.26</td>
    </tr>
    <tr>
    <td>hybrid_rrf</td>
    <td style="text-align: right;">0.400</td>
    <td style="text-align: right;">0.150</td>
    <td style="text-align: right;">201.25</td>
    </tr>
    <tr>
    <td>cross_encoder</td>
    <td style="text-align: right;">0.200</td>
    <td style="text-align: right;">0.200</td>
    <td style="text-align: right;">310.67</td>
    </tr>
    <tr>
    <td>multi_query</td>
    <td style="text-align: right;">0.200</td>
    <td style="text-align: right;">0.200</td>
    <td style="text-align: right;">1798.72</td>
    </tr>
    </tbody>
    </table>
    <span class="paragraph">Search time excludes model loading and index construction. This is one sequential run, not a latency benchmark. The full record contains the answer key, ranked chunks, rewrites, timings, and model settings.</span></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Read the per-question results before the averages. The answer key may omit another page containing the same evidence; inspect excerpts before concluding a retriever is useless.

    Measure latency repeatedly before choosing a configuration. Query embeddings and query expansion are included in search time; initial model loading and index construction are reported separately.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Read the per-case matrix, not the averages. Which case separates the rungs, and would you pay the top rung's latency for that one case?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try your own question

    Tell your assistant your question and the pages you identified as evidence. Ask it to use the same tool and settings for each retriever. The source accepts reviewed cases and different chunk sizes or candidate counts, so you can change one variable and rerun without rewriting the algorithms.

    A finding applies to the cases you tested. Failing to find a separating question does not establish that dense retrieval is sufficient for every future question.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Write one question over your corpus where exactly one retriever gets the right page at rank 1. Identify its evidence pages, run it through every rung, and write one sentence on why that rung won. If you cannot find such a question, that is a finding too: dense search is enough for this corpus.
    """)
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

    | Experiment | Production requirement |
    |---|---|
    | Suggested evidence pages | Reviewed evidence and new cases from real user questions |
    | An index rebuilt for each run | Incremental indexing and a refresh policy |
    | One chunk size and candidate count | Settings evaluated on held-out cases |
    | A local reranker | Model versions and a serving latency budget |
    | One pipeline for every question | Routing based on measured question types |
    | A single score table | Regression checks over time |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Keep the answer key out of the retrieval index and review evidence pages before scoring.
    - Record the corpus, models, settings, and actual results; never invent a ranking or metric.
    - Compare quality and repeated latency measurements before adopting a more expensive rung.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Change chunk size while keeping the evidence pages fixed, then measure again.
    - Compare exact-token questions with paraphrases before trying a router.
    - Cache embeddings or rewrites and measure the effect on latency.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>About the recorded experiments</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">These recordings use the seed corpus and five seed questions. Their answer key is preserved in <code>data/recorded_experiments.json</code>; your reviewed evidence pages may produce different scores. No live workspace artifacts were changed.</span>
    <span class="paragraph">To keep your results, ask your assistant to run score with <code>--cases</code> pointing to your reviewed file and <code>--save</code>. This runs a new experiment and saves its answer key and measurements through the workspace helper.</span></span>
    </details>
    """)
    return


if __name__ == "__main__":
    app.run()
