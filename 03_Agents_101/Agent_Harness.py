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
    # Agents 101

    An agent is a model with a job description, a toolbox, a budget, and a visible trace. This notebook builds the smallest harness that makes an agent's behaviour inspectable, points its tools at your charter and prompt outputs, and records every conversation as a transcript.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    What an agent is: a model with a job description, a toolbox, a budget, and a trace. Tools are a contract of name, docstring, and schema. The loop, built with one call.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    Four questions derived from your charter, run through the agent with middleware that logs and limits calls, and the conversations saved as transcripts for the judge to score.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    A production harness adds a tool catalogue with auth and audit, persistent traces, and quotas. Tell your team which question called a tool, which did not, and what the trace revealed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 35 minutes
    **Reads:** charter, prompts
    **Writes:** transcripts
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    The chat model comes from `.env`. Nothing here needs embeddings or a vector store. The tools are plain Python over the two artifacts your workspace already holds.
    """)
    return


@app.cell
def _():
    import json, re, textwrap

    from langchain.agents import create_agent
    from langchain.agents.middleware import ModelCallLimitMiddleware, ToolCallLimitMiddleware, before_model
    from langchain.tools import tool
    from langchain_core.messages import AIMessage, ToolMessage
    from langchain_openai import ChatOpenAI

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, require, budget
    from helpers import workspace as ws
    from helpers.llm import chat_model

    require("OPENAI_API_KEY")
    llm = chat_model()

    CHARTER = ws.load("charter")
    PROMPTS = ws.load("prompts")
    print(f"✅ model {LLM_MODEL}; charter {len(CHARTER.split())} words; {len(PROMPTS)} prompt rows")
    return (
        AIMessage,
        CHARTER,
        ModelCallLimitMiddleware,
        PROMPTS,
        ToolCallLimitMiddleware,
        ToolMessage,
        before_model,
        budget,
        create_agent,
        llm,
        re,
        textwrap,
        tool,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with the model, the charter size, and a prompt row count over ten. Stop here if the prompt count is zero: run the prompt patterns notebook first, or let the seed carry it.
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
    ## Task 1 of 6 — Give the agent something to look up

    A tool is a function the model may ask your system to run. The model sees only the name, the docstring, and the input schema, so those three lines are the whole contract. The first tool searches your charter by section; the second searches the prompt outputs; the third records a request and returns an id.
    """)
    return


@app.cell
def _(CHARTER, PROMPTS, re, textwrap, tool):
    STOP = {"a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how", "i", "in", "is", "it", "of",
            "on", "or", "our", "should", "that", "the", "their", "to", "what", "when", "with", "my", "can"}


    def terms(text: str) -> set[str]:
        return {t for t in re.findall(r"[a-z0-9][a-z0-9-]+", text.lower()) if t not in STOP}


    def sections(markdown: str) -> list[dict]:
        out, title, lines = [], "intro", []
        for line in markdown.splitlines():
            if line.startswith("## "):
                if lines:
                    out.append({"title": title, "text": "\n".join(lines).strip()})
                title, lines = line[3:].strip(), []
            else:
                lines.append(line)
        if lines:
            out.append({"title": title, "text": "\n".join(lines).strip()})
        return [s for s in out if s["text"]]


    CHARTER_SECTIONS = sections(CHARTER)
    REQUESTS: list[dict] = []


    @tool
    def search_charter(query: str) -> str:
        """Search the product charter for the section most relevant to the query."""
        q = terms(query)
        ranked = sorted(CHARTER_SECTIONS, key=lambda s: len(q & terms(s["title"] + " " + s["text"])), reverse=True)
        best = ranked[0]
        if not q & terms(best["title"] + " " + best["text"]):
            return "No charter section matched."
        return f"[{best['title']}]\n{textwrap.shorten(best['text'], 700)}"


    @tool
    def search_prompt_outputs(query: str) -> str:
        """Search earlier prompt outputs for an answer already written to a similar question."""
        q = terms(query)
        ranked = sorted(PROMPTS, key=lambda p: len(q & terms(p["input"] + " " + p["output"])), reverse=True)
        hit = ranked[0]
        if not q & terms(hit["input"] + " " + hit["output"]):
            return "No earlier output matched."
        return f"[pattern: {hit['pattern']}]\n{textwrap.shorten(hit['output'], 700)}"


    @tool
    def log_request(summary: str) -> str:
        """Record a request the agent cannot resolve itself. Returns a request id."""
        REQUESTS.append({"id": f"R-{len(REQUESTS) + 1:03d}", "summary": summary})
        return f"Logged as {REQUESTS[-1]['id']}."


    TOOLS = [search_charter, search_prompt_outputs, log_request]
    print([t.name for t in TOOLS])
    print(search_charter.invoke({"query": "what does the product refuse to do"}))
    return TOOLS, search_charter


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the three tool names and a charter section in brackets with its text. Stop here if the search returns no match: your charter has no `##` headings, and the tool splits on those.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 6 — Build the loop

    `create_agent` wires the loop: the model reads the question, decides whether to call a tool, reads the result, and answers. The system prompt is the job description. It names each tool and says what to do with questions outside the product.
    """)
    return


@app.cell
def _(CHARTER, TOOLS, create_agent, llm):
    SYSTEM = f"""You are the assistant described in the charter below. You have three tools:
    - search_charter: for anything about the product, its users, its scope, or its refusals.
    - search_prompt_outputs: for answers already written to similar questions.
    - log_request: when a request needs a person; record it and give the user the id.

    Name the tool result as your source. If a question is outside the product's scope, say so in one sentence.
    Do not invent facts that are not in a tool result.

    CHARTER:
    {CHARTER}
    """

    agent = create_agent(model=llm, tools=TOOLS, system_prompt=SYSTEM)
    print(type(agent).__name__)
    return SYSTEM, agent


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a compiled graph type name. Nothing has run yet.
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
    ## Task 3 of 6 — Ask questions your users would ask

    Rather than type questions for the seed product, let the model derive four from your charter: two inside scope, one that needs a person, one outside scope. Then run the agent on each and keep the full message list.
    """)
    return


@app.cell
def _(CHARTER, llm):
    from pydantic import BaseModel
    from typing import List

    class Questions(BaseModel):
        in_scope: List[str]
        needs_a_person: str
        out_of_scope: str
    derived = llm.with_structured_output(Questions).invoke("From this charter write two questions a user would ask that the product should answer, one request that needs a person to act, and one question outside the product's scope. Write them in the user's own words.\n\n" + CHARTER)
    QUESTIONS = derived.in_scope[:2] + [derived.needs_a_person, derived.out_of_scope]
    for _q in QUESTIONS:
        print('-', _q)
    return (QUESTIONS,)


@app.cell
def _(AIMessage, QUESTIONS, ToolMessage, agent, textwrap):
    def run(agent_, question: str) -> dict:
        """Invoke the agent and return the final answer plus the trace."""
        result = agent_.invoke({'messages': [{'role': 'user', 'content': question}]})
        msgs = result['messages']
        turns, tool_calls = ([{'role': 'user', 'content': question}], [])
        for m in msgs:
            if isinstance(m, AIMessage):
                for c in m.tool_calls or []:
                    tool_calls.append({'name': c['name'], 'args': c['args'], 'result': ''})
                if m.content:
                    turns.append({'role': 'assistant', 'content': m.content if isinstance(m.content, str) else str(m.content)})
            elif isinstance(m, ToolMessage) and tool_calls:
                tool_calls[-1]['result'] = str(m.content)[:800]
        return {'turns': turns, 'tool_calls': tool_calls, 'answer': turns[-1]['content']}
    RUNS = []
    for _i, _q in enumerate(QUESTIONS, 1):
        _r = run(agent, _q)
        RUNS.append({'id': f't{_i:02d}', **_r})
        print(f"[t{_i:02d}] {_q}\n  tools: {[c['name'] for c in _r['tool_calls']] or 'none'}\n  {textwrap.shorten(_r['answer'], 240)}\n")
    return RUNS, run


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see four runs, each with the tools it called and a short answer. The out-of-scope question should call no tool and decline in one sentence. Stop here if every run calls every tool: the docstrings are too vague.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which question should have caused a tool call and which should have stayed out of scope? Did the trace agree with you?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 6 — Watch the loop, step by step

    A final answer can hide a messy route. Streaming the updates shows each model step and each tool result as it happens. Judge the behaviour by the trace, not by the polish of the last message.
    """)
    return


@app.cell
def _(AIMessage, QUESTIONS, ToolMessage, agent, textwrap):
    def stream(agent_, question: str) -> None:
        for chunk in agent_.stream({"messages": [{"role": "user", "content": question}]}, stream_mode="updates"):
            for node, update in chunk.items():
                print(f"--- {node}")
                for m in (update or {}).get("messages", []):
                    if isinstance(m, ToolMessage):
                        print("tool result:", textwrap.shorten(str(m.content), 300))
                    elif isinstance(m, AIMessage) and m.tool_calls:
                        print("tool call:", [(c["name"], c["args"]) for c in m.tool_calls])
                    elif getattr(m, "content", ""):
                        print("answer:", textwrap.shorten(str(m.content), 300))


    stream(agent, QUESTIONS[0])
    return (stream,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a `model` node that emits a tool call, a `tools` node with the result, and a second `model` node with the answer. Stop here if the model node answers with no tool call on an in-scope question: the system prompt is not steering it to the tools.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 6 — Add middleware

    Middleware wraps the loop without rewriting it. A logging hook shows how many messages each model step sees. A model-call limit stops a runaway loop. Both are the kind of control a production owner asks for before a demo.
    """)
    return


@app.cell
def _(
    ModelCallLimitMiddleware,
    QUESTIONS,
    SYSTEM,
    TOOLS,
    before_model,
    create_agent,
    llm,
    stream,
):
    @before_model
    def log_before_model(state, runtime):
        """Print a compact view of each model step."""
        print(f"[middleware] model call with {len(state['messages'])} message(s)")


    observed = create_agent(model=llm, tools=TOOLS, system_prompt=SYSTEM,
                            middleware=[log_before_model, ModelCallLimitMiddleware(run_limit=4, exit_behavior="end")])
    stream(observed, QUESTIONS[2])
    return log_before_model, observed


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a `[middleware]` line before each model step and the run ending within four model calls. Stop here if the middleware never prints: check the import of `before_model`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    What did the middleware make visible that the final answer hid? When would a limit of four be too low?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 6 — Save the transcripts

    Every run so far is a conversation with tool calls attached. Saving them makes them the material the judge scores and the corpus later notebooks retrieve over. Include the runs with middleware so the judge sees both.
    """)
    return


@app.cell
def _(QUESTIONS, RUNS, budget, observed, run, ws):
    TRANSCRIPTS = [{'id': r['id'], 'turns': r['turns'], 'tool_calls': r['tool_calls'], 'question': r['turns'][0]['content']} for r in RUNS]
    extra = budget(4, 2)
    for _i, _q in enumerate(QUESTIONS[:extra], len(RUNS) + 1):
        _r = run(observed, _q)
        TRANSCRIPTS.append({'id': f't{_i:02d}', 'turns': _r['turns'], 'tool_calls': _r['tool_calls'], 'question': _q, 'variant': 'observed'})
    ws.save('transcripts', TRANSCRIPTS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with at least six rows written. Stop here if it says fewer than four: a run above failed silently.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Give the agent a tool-call budget: at most one call to `search_charter` per run. Then ask a question that tempts it to search twice, and read the trace. Explain to a teammate what the budget blocked and what it cost.
    """)
    return


@app.cell
def _(
    ModelCallLimitMiddleware,
    SYSTEM,
    TOOLS,
    ToolCallLimitMiddleware,
    create_agent,
    llm,
    log_before_model,
    search_charter,
    stream,
):
    budgeted = create_agent(model=llm, tools=TOOLS, system_prompt=SYSTEM, middleware=[
        log_before_model,
        ModelCallLimitMiddleware(run_limit=4, exit_behavior="end"),
        ToolCallLimitMiddleware(tool_name=search_charter.name, run_limit=1, exit_behavior="continue"),
    ])
    stream(budgeted, "Compare what the product must do with what it refuses to do, using separate lookups for each.")
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
    | Three local tools over two files | A tool catalogue over live systems with auth, audit logs, rate limits |
    | One `create_agent` harness | Versioned agent configs with staged environments and rollback |
    | Streaming printed to a cell | Persistent traces in an observability tool, searchable per run |
    | Logging and call limits | Guardrails, retries, circuit breakers, per-tenant quotas |
    | Four hand-derived questions | Regression suites that replay known failures before release |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - A model-call and tool-call budget on every run, with the exit behaviour written down.
    - Every tool call logged with its arguments and result, kept long enough to audit.
    - An approval step before any tool that changes state outside the agent.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Write a trace assertion: fail if an in-scope question is answered without a `search_charter` call. Run it over the saved transcripts.
    - Have tools return a `found` flag and change the system prompt so the agent asks a clarifying question when evidence is weak.
    - Add approval middleware that pauses before `log_request`, prints the proposed summary, and waits for a yes.
    """)
    return


if __name__ == "__main__":
    app.run()
