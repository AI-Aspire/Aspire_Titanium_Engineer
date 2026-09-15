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
    # Prompt patterns

    Try seven prompt patterns in Claude Code. Compare the answers and decide what helped. Each example includes a prompt to paste and a recorded response to inspect.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Compare persona, examples, reasoning effort, requested output formats, and supplied facts.

    ### Create
    Add requirements to a draft, generate and test an instruction, then apply the patterns to your own project.

    ### Grow
    Turn useful prompts into templates and test them across representative inputs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 30 minutes
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    Open Claude Code alongside this guide. Keep the same model and effort setting except when testing `/effort`.

    Use `/clear` before independent comparisons. Stay in the same conversation for the self-refine draft and revision. Paste each quoted prompt as one message.

    [Interactive commands](https://code.claude.com/docs/en/commands)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What stays in context

    `/clear` removes conversation history, but application and repository instructions remain. The role you paste is a user instruction; Claude Code manages its own system instructions.

    If Claude reads files or uses tools, it has extra information. Keep that in mind when comparing it with an answer based only on the pasted text.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>About the recorded responses</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">These are actual Claude Code responses, generated programmatically for reference. They used claude-sonnet-5, with tools disabled and repository instructions loaded. Effort was medium except for the low/high comparison. Your responses may differ.</span>
    <span class="paragraph"><a href="data/recorded_responses.json">Recording data</a> contains the exact prompts, responses, and settings.</span></span>
    </details>
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
    ## Task 1 of 7 — Persona

    Compare the same support question with and without a role and response constraints.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### A: baseline

    > A colleague says the VPN connects but they cannot reach the staging database. What should they do first?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore L001 L002 S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">This isn't related to this repo or its coursework — it's a general IT/networking troubleshooting question, not something I can see specifics of (VPN config, staging DB network rules, credentials, etc.). A few generic first steps your colleague could try:</span>
    <ol>
    <li>Confirm what "connects" means — is the VPN client showing "connected" with an assigned IP, and can they reach <em>other</em> internal resources (not just the DB)?</li>
    <li>Check they're pointed at the right host/port for staging (not accidentally prod or a stale config) and that DNS resolves it while on VPN (<code>nslookup</code>/<code>dig</code>).</li>
    <li>Test raw connectivity to the DB port, e.g. <code>nc -zv &lt;host&gt; &lt;port&gt;</code> or <code>telnet &lt;host&gt; &lt;port&gt;</code>, to isolate network reachability from auth/app-level issues.</li>
    <li>Check if split-tunnel VPN config is excluding the DB's subnet.</li>
    </ol>
    <span class="paragraph">They should loop in whoever manages the staging infra/VPN (or check internal docs/Slack) since I don't have visibility into your network setup. Want me to help with something else in the repo instead?</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### B: persona and constraints

    > You are a terse lead engineer. Answer in three sentences or fewer. Give the first diagnostic step and explain why.
    >
    > A colleague says the VPN connects but they cannot reach the staging database. What should they do first?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">Have them run <code>nc -zv &lt;staging-db-host&gt; &lt;port&gt;</code> (or <code>telnet</code>) from their machine — this isolates whether it's a routing/firewall issue on the VPN split-tunnel vs. a DB-level problem (auth, wrong credentials, DB down). VPN "connected" only proves the tunnel is up, not that the specific subnet/port is routed through it.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Takeaway: The persona version is shorter and focuses on reachability; the baseline lists several checks. Role and length constraints changed together, so this does not isolate the effect of persona.

    Ask the room: Which answer gives a clearer first action, and what would you verify before following it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 7 — Few-shot

    Examples teach a local convention. This example support desk handles reservations but routes equipment faults elsewhere. Its scope is different from Deskmate’s.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### A: no examples

    > Classify the request for this example support desk as IN_SCOPE or OUT_OF_SCOPE. Give the label and one sentence explaining it.
    >
    > Request: Can you reserve a meeting room for Thursday?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph"><strong>OUT_OF_SCOPE</strong> — this is a facilities/scheduling request, not something a support desk (presumably handling product/account issues) would resolve.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### B: a local convention

    > Classify the request for this example support desk as IN_SCOPE or OUT_OF_SCOPE. Give the label and one sentence explaining it.
    >
    > Example: Can you book a desk for my office visit?
    > Label: IN_SCOPE. This desk handles workspace reservations.
    >
    > Example: My monitor will not turn on.
    > Label: OUT_OF_SCOPE. This desk routes equipment faults to a separate hardware team.
    >
    > Request: Can you reserve a meeting room for Thursday?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">Label: IN_SCOPE. This is a workspace/room reservation request, same category as the desk-booking example.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Takeaway: The baseline assumes a conventional support scope and says OUT_OF_SCOPE. With examples, it follows the local reservation rule and says IN_SCOPE.

    Ask the room: Which fact did the examples supply that the original request left unspecified?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Write down one convention in your charter that the model could not guess from language alone. That is your first few-shot example.

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 7 — Reasoning effort

    Keep the model and prompt identical while changing `/effort`. This changes the reasoning setting, rather than adding “think carefully” to the prompt. Check which levels your model offers.

    [Effort documentation](https://code.claude.com/docs/en/model-config#adjust-effort-level)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### A: low effort

    Enter `/clear`, then `/effort low` as separate commands. Confirm the active level, start a timer, and send:

    > I need my car cleaned. The car wash is fifty metres away. Should I walk or drive? Give a recommendation and a one-sentence reason.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore S002 -->
    <!-- Preserve the recorded response verbatim. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5 · low effort</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Programmatic recording in a fresh session. CLI-reported API duration: 2.04 seconds. This is not an interactive UI timing measurement. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">Drive — you need the car at the car wash, not yourself, so walking there doesn't accomplish anything.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### B: high effort

    Keep the same model. Enter `/clear`, then `/effort high`. Confirm the level, start a timer, and send the identical prompt:

    > I need my car cleaned. The car wash is fifty metres away. Should I walk or drive? Give a recommendation and a one-sentence reason.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore S002 -->
    <!-- Preserve the recorded response verbatim. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5 · high effort</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Programmatic recording in a fresh session. CLI-reported API duration: 2.73 seconds. This is not an interactive UI timing measurement. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">Drive — you need the car at the car wash to have it cleaned, so walking there wouldn't accomplish the task.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Takeaway: Both recorded answers choose to drive. Higher effort does not necessarily improve a simple answer, and one pair cannot establish a quality or speed advantage. Effort is a resource trade-off to measure, not a correctness guarantee.

    Ask the room: What harder task would make extra reasoning worthwhile?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Repeat and restore

    Compare time and correctness on a few harder questions. Do not assume a longer answer is better. Compare your own timings with each other, not with the recordings’ API durations; they measure different things.

    Restore your original effort setting before continuing; the setting can persist across conversations.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 7 — Requesting an output format

    Compare a free-form brief with a request for named JSON fields. Both prompts include the same facts. Check whether Claude follows the requested format.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### A: loose format

    > Summarise the product described below as a product brief.
    >
    > Deskmate answers internal IT questions using the knowledge base and the requester’s own ticket history. Priya is a backend engineer who needs help reaching staging through the VPN. Marcus is the helpdesk lead who wants fewer repeat questions and an auditable log. Deskmate opens a ticket when it cannot answer. It never resets anything without confirmation, touches unverified entitlements, or repeats another user’s ticket text.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore L001 L002 S001 S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph"><strong>Product Brief: Deskmate</strong></span>
    <span class="paragraph"><strong>One-liner:</strong> An internal IT support assistant that answers employee questions using the knowledge base plus the requester's own ticket history, escalating to a human ticket when it can't help.</span>
    <span class="paragraph"><strong>Personas:</strong>
    - <strong>Priya (backend engineer)</strong> — needs quick, accurate answers to technical questions, e.g., VPN access to staging.
    - <strong>Marcus (helpdesk lead)</strong> — wants fewer repeat/duplicate questions reaching the team and a fully auditable log of what Deskmate said and did.</span>
    <span class="paragraph"><strong>Core behavior:</strong>
    - Answers questions by combining the knowledge base with the requester's own ticket history (personalized, context-aware support).
    - Opens a ticket automatically when it cannot answer a question, ensuring nothing falls through the cracks.</span>
    <span class="paragraph"><strong>Guardrails (things it explicitly will not do):</strong>
    - Never resets anything (accounts, passwords, access, etc.) without explicit user confirmation.
    - Never touches entitlements that haven't been verified.
    - Never repeats or exposes another user's ticket text — keeps requester data siloed.</span>
    <span class="paragraph"><strong>Why it matters:</strong> Reduces repeat tickets and support load (Marcus's goal) while giving engineers like Priya fast self-service answers, without compromising on safety (no silent destructive actions) or privacy (no cross-user data leakage) — and leaves an audit trail for accountability.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore L002 -->
    <!-- Keep the full prompt copyable; long prompts are collapsed. -->
    ### B: explicit fields

    <details>
    <summary>Expand the complete prompt to copy</summary>
    <span class="markdown prose dark:prose-invert contents"><blockquote>
    <span class="paragraph">Extract a product brief from the text below. Return only one JSON object with exactly these fields, without Markdown fences or introductory prose:
    product_name: a string
    users: a list of names in the text
    must_do: a list of stated responsibilities
    must_not_do: a list of stated restrictions</span>
    <span class="paragraph">Do not invent details. Use an empty list for missing list information.</span>
    <span class="paragraph">Deskmate answers internal IT questions using the knowledge base and the requester’s own ticket history. Priya is a backend engineer who needs help reaching staging through the VPN. Marcus is the helpdesk lead who wants fewer repeat questions and an auditable log. Deskmate opens a ticket when it cannot answer. It never resets anything without confirmation, touches unverified entitlements, or repeats another user’s ticket text.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <div class="language-json codehilite"><pre><span></span><code><span class="p">{</span>
    <span class="w">  </span><span class="nt">"product_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Deskmate"</span><span class="p">,</span>
    <span class="w">  </span><span class="nt">"users"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"Priya"</span><span class="p">,</span><span class="w"> </span><span class="s2">"Marcus"</span><span class="p">],</span>
    <span class="w">  </span><span class="nt">"must_do"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
    <span class="w">    </span><span class="s2">"Answer internal IT questions using the knowledge base and the requester's own ticket history"</span><span class="p">,</span>
    <span class="w">    </span><span class="s2">"Open a ticket when it cannot answer"</span>
    <span class="w">  </span><span class="p">],</span>
    <span class="w">  </span><span class="nt">"must_not_do"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
    <span class="w">    </span><span class="s2">"Reset anything without confirmation"</span><span class="p">,</span>
    <span class="w">    </span><span class="s2">"Touch unverified entitlements"</span><span class="p">,</span>
    <span class="w">    </span><span class="s2">"Repeat another user's ticket text"</span>
    <span class="w">  </span><span class="p">]</span>
    <span class="p">}</span>
    </code></pre></div>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Takeaway: The response adds Markdown fences despite the explicit instruction not to. The JSON inside has the requested fields, but the whole response fails direct JSON parsing. A format request does not enforce a schema.

    Ask the room: What would your application need to check before accepting this response?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to Claude

    > Read the tool reference in the README beside this guide. Run prompt_tools.py compare on the active charter. Show the plain JSON request and the schema-enforced result using the same input and fields. Explain ProductBrief and the actual validation outcome. Distinguish a valid shape from correct facts, and report any refusal or unsupported-endpoint error.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see two real API results using the configured experiment model. Both may validate on this run. The enforced call supplies the schema to the API; the plain request relies on following instructions. Stop here if the enforced result is absent or the fields misrepresent the charter. Correct structure does not guarantee correct content.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details><summary>Recorded experiment: schema enforcement</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Real seed-charter run with <code>gpt-4.1-mini</code>. Both calls returned valid product briefs in this run. The enforced call completed with <code>stop</code> and no refusal.</span>
    <span class="paragraph">The plain call passed an independent Pydantic validation check; the enforced call supplied <code>ProductBrief</code> as the API response format and returned a parsed object. Check the contents against the charter even when validation succeeds.</span>
    <span class="paragraph">Exact inputs, schema, response IDs, and both outputs: <code>data/recorded_schema_experiment.json</code>. This is an API experiment run by a repo tool, not a Claude UI response.</span></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 7 — Pasted context

    Ask a question without the relevant facts, then supply them. Use `/clear` between the two prompts so the first answer cannot reuse facts from another example.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### A: missing context

    > Who are the two named users of Deskmate, and what does the product refuse to do? Answer only from information supplied in this conversation. If it is missing, say so.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">That information isn't present in this conversation—no mention of "Deskmate" appears anywhere in the context I've been given.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### B: supplied context

    > Who are the two named users of Deskmate, and what does the product refuse to do? Answer only from the text below. If it is missing, say so.
    >
    > Deskmate answers internal IT questions using the knowledge base and the requester’s own ticket history. Priya is a backend engineer who needs help reaching staging through the VPN. Marcus is the helpdesk lead who wants fewer repeat questions and an auditable log. Deskmate opens a ticket when it cannot answer. It never resets anything without confirmation, touches unverified entitlements, or repeats another user’s ticket text.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">The two named users are Priya (backend engineer needing VPN access to staging) and Marcus (helpdesk lead wanting fewer repeat questions and an auditable log).</span>
    <span class="paragraph">Deskmate refuses to: reset anything without confirmation, touch unverified entitlements, or repeat another user's ticket text.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Takeaway: Without the product facts, Claude acknowledges the gap. With them, it names Priya and Marcus and repeats the three restrictions.

    Ask the room: Can you point to the supplied text supporting every claim in the second answer?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    How large can a pasted document get before this stops being practical, and what would you do then?

    Answer:
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
    ## Task 6 of 7 — Self-refine

    Draft an introduction, then add criteria and request a revision in the same conversation. The first draft was not given the checklist; this tests clearer requirements plus revision.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Turn 1: draft

    > Write a short introduction that tells Priya what Deskmate can help with. Use only the text below.
    >
    > Deskmate answers internal IT questions using the knowledge base and the requester’s own ticket history. Priya is a backend engineer who needs help reaching staging through the VPN. Marcus is the helpdesk lead who wants fewer repeat questions and an auditable log. Deskmate opens a ticket when it cannot answer. It never resets anything without confirmation, touches unverified entitlements, or repeats another user’s ticket text.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">Hi Priya,</span>
    <span class="paragraph">Deskmate answers internal IT questions using the knowledge base and your own ticket history — for example, help reaching staging through the VPN. If it can't answer, it opens a ticket for you rather than guessing. It won't reset anything without your confirmation, won't touch entitlements it can't verify, and won't reuse another user's ticket text. For Marcus and the helpdesk team, this also means fewer repeat questions and an auditable log of what was asked and answered.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Turn 2: add criteria and revise

    > Review your introduction against these criteria:
    > 1. Under 60 words.
    > 2. Names Priya.
    > 3. States at least one supported capability and at least one restriction.
    > 4. Ends by asking what IT issue she needs help with.
    > 5. Adds no claims absent from the supplied text.
    >
    > Give a short critique identifying which criteria pass or fail, then a revised introduction under REVISED. If the draft already meets the criteria, say so; do not invent a flaw.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore L002 S001 S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Continues the draft session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph"><strong>Critique:</strong>
    1. <strong>Fail</strong> — draft is ~79 words, over the 60-word limit.
    2. <strong>Pass</strong> — names Priya.
    3. <strong>Pass</strong> — states a capability (answers IT questions via knowledge base/ticket history) and a restriction (won't reset anything without confirmation).
    4. <strong>Fail</strong> — ends with a statement about Marcus/helpdesk, not a question asking what she needs help with.
    5. <strong>Pass</strong> — no claims beyond the supplied text.</span>
    <span class="paragraph"><strong>REVISED:</strong></span>
    <span class="paragraph">Hi Priya, Deskmate answers internal IT questions using the knowledge base and your own ticket history — helpful for things like reaching staging through the VPN. If it can't answer, it opens a ticket instead of guessing, and it never resets anything without your confirmation. What IT issue can I help you with today?</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Takeaway: Adding the checklist produces a shorter revision that ends by asking about Priya’s issue. These requirements were not supplied to the first draft, so this demonstrates clearer requirements plus revision, not self-critique alone.

    Ask the room: Which improvement follows directly from a requirement you added?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 7 of 7 — Meta-prompting

    Ask Claude to write an instruction, then test it against a simple baseline. For B, replace the recorded instruction with the one Claude just generated. Keep the context and question fixed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Generate an instruction

    > Write a reusable instruction of at most 120 words for an assistant answering Deskmate questions. It will receive product context and a user question separately.
    >
    > It should answer only from supplied facts, acknowledge missing information, respect product restrictions, and offer a supported next action. Prevent invented policies, menu paths, and claims that actions were performed.
    >
    > Return only the instruction. Do not answer a support question yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore L002 S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">Answer the user's question using only the supplied product context. If the needed information isn't present, say so plainly rather than guessing. Never invent policies, menu paths, settings, prices, or steps not explicitly stated in the context. Never claim to have performed an action (e.g., issued a refund, changed a setting, submitted a ticket) — you can only provide information and guidance. Respect any stated product restrictions or limitations exactly as given. If the context doesn't fully resolve the question, acknowledge the gap and suggest a concrete, supported next step (e.g., contacting a specific support channel mentioned in the context, checking a stated resource). Keep responses concise, factual, and free of speculation.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### A: baseline test

    > Answer the support question using only the context supplied.
    >
    > Context:
    > Deskmate answers internal IT questions using the knowledge base and the requester’s own ticket history. Priya is a backend engineer who needs help reaching staging through the VPN. Marcus is the helpdesk lead who wants fewer repeat questions and an auditable log. Deskmate opens a ticket when it cannot answer. It never resets anything without confirmation, touches unverified entitlements, or repeats another user’s ticket text.
    >
    > Question: My VPN connects but I cannot reach staging. What exact menu path should I use to fix it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore L002 S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">I don't have any knowledge base content in the supplied context — only a description of Deskmate's policies (it uses the KB and ticket history, opens a ticket when it can't answer, and never touches unverified entitlements or reuses another user's ticket text). No actual VPN/staging KB article or steps were provided to me.</span>
    <span class="paragraph">Since I have no article giving an exact menu path, I can't answer that specifically — and per the stated behavior, this is exactly the case where Deskmate would open a ticket rather than guess or fabricate steps. If you can share the relevant KB article text, I can walk through the exact menu path from it.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore L001 L002 S002 -->
    <!-- Keep the full prompt copyable; long prompts are collapsed. -->
    ### B: generated instruction test

    <details>
    <summary>Expand the complete prompt to copy</summary>
    <span class="markdown prose dark:prose-invert contents"><blockquote>
    <span class="paragraph">Answer the user's question using only the supplied product context. If the needed information isn't present, say so plainly rather than guessing. Never invent policies, menu paths, settings, prices, or steps not explicitly stated in the context. Never claim to have performed an action (e.g., issued a refund, changed a setting, submitted a ticket) — you can only provide information and guidance. Respect any stated product restrictions or limitations exactly as given. If the context doesn't fully resolve the question, acknowledge the gap and suggest a concrete, supported next step (e.g., contacting a specific support channel mentioned in the context, checking a stated resource). Keep responses concise, factual, and free of speculation.</span>
    <span class="paragraph">Answer the support question using only the context supplied.</span>
    <span class="paragraph">Context:
    Deskmate answers internal IT questions using the knowledge base and the requester’s own ticket history. Priya is a backend engineer who needs help reaching staging through the VPN. Marcus is the helpdesk lead who wants fewer repeat questions and an auditable log. Deskmate opens a ticket when it cannot answer. It never resets anything without confirmation, touches unverified entitlements, or repeats another user’s ticket text.</span>
    <span class="paragraph">Question: My VPN connects but I cannot reach staging. What exact menu path should I use to fix it?</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- lint: ignore S002 -->
    <!-- Preserve the actual response verbatim; long recordings are collapsed. -->
    <details>
    <summary>Recorded response · 2026-09-14 · claude-sonnet-5</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Fresh session; medium effort. Verbatim response:</span>
    <blockquote>
    <span class="paragraph">The context provided doesn't include a knowledge base article or menu path for fixing VPN-to-staging connectivity — only a general description of Deskmate's behavior and the roles of Priya and Marcus. I can't give you exact steps without inventing them.</span>
    <span class="paragraph">Since Deskmate opens a ticket when it cannot answer a question, the concrete next step here would be for a ticket to be opened so someone with access to the actual VPN/staging configuration can provide the correct menu path.</span>
    </blockquote></span>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Takeaway: The generated instruction fits the length limit, and both test answers avoid inventing a menu path. The generated-prompt answer is shorter; this example does not establish a reliability improvement.

    Ask the room: Did the generated instruction improve the answer on the criteria that matter?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Apply the patterns to your project

    Paste the charter your group wrote. Choose your own examples and criteria, then try the patterns on your product. For the activity below, request the named fields and inspect the answer; the group makes the decision.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Stack three patterns in one message: a persona, the charter as context, and a structured output with a decision (`proceed`, `redesign`, `pause`), a rationale, and up to three risks. Ask whether your group should build the product as described. Then explain to a teammate which pattern did the most work.
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

    | Conversation pattern | Production requirement |
    |---|---|
    | Persona and examples | Versioned instructions with explicit message roles and held-out tests |
    | Interactive effort settings | Repeated quality, latency, and usage measurements |
    | Asking for JSON fields | Supported schema enforcement plus format and factual validation |
    | Pasted context | Retrieval with sources and access controls |
    | Draft and revision | Explicit acceptance criteria and independent checks |
    | Generated instructions | Comparison against a baseline across representative tasks |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Compare actual answers, including failures.
    - Check claims against source facts; a model’s critique can also be wrong.
    - Make your own product choices and explain the evidence behind them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Pick five representative questions and define success before comparing prompts.
    - Repeat trials to see whether an apparent improvement holds.
    - Choose examples from real conventions your users need the assistant to follow.
    """)
    return


if __name__ == "__main__":
    app.run()
