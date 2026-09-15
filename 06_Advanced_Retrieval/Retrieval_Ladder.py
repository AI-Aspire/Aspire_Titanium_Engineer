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
    Inspect the evidence labels and compare the retrieval methods on identical chunks.

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

    Reads: corpus, vibe checks, and existing eval cases when available.

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

    > Read the README beside the Retrieval ladder notebook and inspect its retrieval_tools.py interface. Use the inspect command to show which corpus is active, how many pages it has, and which pages are excluded. Check the existing evidence cases too. Do not run a model experiment yet.
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
    | Hit rate | Fraction of questions with a labelled page in the top results |
    | MRR | Average reciprocal rank of the first labelled result |
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
    ## Task 1 of 4 — Label the evidence

    A score needs an answer key. For each question, identify pages that contain evidence, not just matching words. Label pages rather than chunk IDs so the labels can survive a chunk-size change.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ask your assistant

    > Use the retrieval tools to propose evidence-page labels for the current vibe checks. Compare them with the existing eval cases. Show one question, its proposed pages, and the relevant source text. Wait for me to review the labels before treating new proposals as the answer key. Do not save anything yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Check the full pages; the model only sees short digests when proposing labels. A missing label can make a useful result score as a miss. An empty page list means the case is excluded from retrieval scoring, not that the system passed it.

    An out-of-scope question may still have a relevant policy page explaining the refusal. Review that distinction rather than automatically deleting its labels.
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

    > Use retrieval_tools.py to compare dense and BM25 for: My VPN connects but I cannot reach staging.
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

    > Run the same question through all five retrieval rungs with the default settings. Show the dense and BM25 candidate lists used by RRF, the shortlist before reranking, and the generated query rewrites. Compare the final top four results. Identify a page that moved up or disappeared and trace what happened using the tool output.
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

    Hit rate asks whether a labelled page appears among the top results. Reciprocal rank rewards finding it sooner: rank one gives one, rank four gives one quarter, and a miss gives zero. Average those values to obtain MRR.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ask your assistant

    > Use retrieval_tools.py to score all five rungs on the same evidence cases and top-four setting. Use my reviewed labels if I provided them; otherwise use the existing cases and state their source. Show hit rate, MRR, search time, and the per-case reciprocal-rank matrix. List any skipped cases. Do not change labels to improve a score or save workspace artifacts.
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
    <span class="paragraph">Search time excludes model loading and index construction. This is one sequential run, not a latency benchmark. The full record contains labels, ranked chunks, rewrites, timings, and model settings.</span></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Read the per-case results before the averages. Page-based labels can miss duplicated evidence on another page; inspect excerpts before concluding a retriever is useless.

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

    Write one question over your corpus where exactly one retriever gets the right page at rank 1. Label its pages, run it through every rung, and write one sentence on why that rung won. If you cannot find such a question, that is a finding too: dense search is enough for this corpus.
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
    | Proposed page labels | Reviewed evidence and new cases from real user questions |
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

    - Keep the answer key out of the retrieval index and review labels before scoring.
    - Record the corpus, models, settings, and actual results; never invent a ranking or metric.
    - Compare quality and repeated latency measurements before adopting a more expensive rung.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Change chunk size while keeping page labels fixed, then measure again.
    - Compare exact-token questions with paraphrases before trying a router.
    - Cache embeddings or rewrites and measure the effect on latency.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>About the recorded experiments</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">The recordings were produced by <code>retrieval_tools.py</code> on the seed corpus. Proposed labels are included as proposals, not treated as reviewed truth. Scoring used the existing seed eval cases. No live workspace artifacts were changed for these recordings.</span>
    <span class="paragraph">If you want to keep an experiment for later workflows, ask your assistant to run the score tool with its save option. That writes only the actual cases and measured ladder through the workspace helper.</span></span>
    </details>
    """)
    return


if __name__ == "__main__":
    app.run()
