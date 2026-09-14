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

    Before you reach for retrieval, a framework, or a new model, try prompting better. It is the cheapest lever you have. This notebook builds seven prompt patterns from scratch against your own charter, and saves every input and output so later notebooks can retrieve over them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Seven prompt patterns, each shown weak first: persona, few-shot, reasoning budget, structured output, pasted context, self-refine, meta-prompting. Why each one works, in one call each.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    A pitch for your product refined against explicit criteria, a system prompt for your assistant written by the model, and every prompt of the session saved as your first corpus.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Prompts in production are versioned like code, tested against a regression set, and routed by budget. Ask your team which pattern moved your task most, and whether it is written down anywhere.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 30 minutes
    **Reads:** charter
    **Writes:** prompts
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    The helper below makes one chat call. `instructions` is the system prompt, `effort` is the reasoning budget for models that have one. Every call is recorded in `PROMPTS` so the last cell can save the whole session.
    """)
    return


@app.cell
def _():
    import json, time

    from openai import OpenAI
    from IPython.display import display, Markdown

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, require
    from helpers import workspace as ws
    from helpers.llm import client

    require("OPENAI_API_KEY")
    client = client()
    MODEL = LLM_MODEL
    PROMPTS: list[dict] = []

    def ask(user, instructions=None, effort=None, pattern="ad hoc", **kw) -> str:
        """One chat call. `user` is a string or a list of role-message dicts."""
        messages = [{"role": "system", "content": instructions}] if instructions else []
        messages += [{"role": "user", "content": user}] if isinstance(user, str) else user
        if effort:
            kw["reasoning_effort"] = effort
        resp = client.chat.completions.create(model=MODEL, messages=messages, **kw)
        text = resp.choices[0].message.content or ""
        PROMPTS.append({"pattern": pattern, "input": user if isinstance(user, str) else json.dumps(user),
                        "output": text, "model": MODEL, "instructions": instructions or ""})
        return text

    def show(text: str) -> None:
        display(Markdown(text))

    CHARTER = ws.load("charter")
    print(f"✅ model {MODEL} at {LLM_BASE or 'api.openai.com'}; charter is {len(CHARTER.split())} words")
    return CHARTER, MODEL, PROMPTS, ask, client, json, show, time, ws


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line naming the model and the charter length, and possibly an ℹ line saying the charter comes from the seed. Stop here if you get a missing-key error: copy `.env.template` to `.env` and fill it in.
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

    The system prompt does not change what the model knows. It changes how the model speaks. Ask one question from your charter three ways: no persona, a terse lead engineer, a patient onboarding buddy. Same facts, different voice.
    """)
    return


@app.cell
def _(ask, show):
    QUESTION = "A colleague says the VPN connects but they cannot reach the staging database. What should they do first?"

    print("weak: no persona")
    show(ask(QUESTION, pattern="persona: none"))
    return (QUESTION,)


@app.cell
def _(QUESTION, ask, show):
    TERSE = ("You are a terse lead engineer. Answer in three sentences or fewer. "
             "Give the exact step to take first. No pleasantries.")
    PATIENT = ("You are a patient onboarding buddy. Explain the reasoning step by step, "
               "anticipate the follow-up question, and end with one concrete next action.")

    print("strong: terse lead engineer")
    show(ask(QUESTION, instructions=TERSE, pattern="persona: terse"))
    print("strong: patient onboarding buddy")
    show(ask(QUESTION, instructions=PATIENT, pattern="persona: patient"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see three answers to the same question in three voices. The facts should match; the length and tone should not. Stop here if all three read the same: your model may be ignoring the system prompt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 7 — Few-shot

    The model knows what words mean. It does not know your conventions. Two labelled examples in the conversation teach it a convention it cannot guess. Here the convention is what counts as in scope for the product in your charter. Edit the examples to match your charter.
    """)
    return


@app.cell
def _(CHARTER, ask, json, show):
    SCOPE_INSTRUCTIONS = ("You triage incoming requests for the product described in the charter below. "
                          "Classify each request as IN_SCOPE or OUT_OF_SCOPE and give a one-sentence reason. "
                          'Reply with JSON: {"classification": "...", "reason": "..."}.\n\n' + CHARTER)

    print("weak: no examples")
    show(ask("Can you book me a meeting room for Thursday?", instructions=SCOPE_INSTRUCTIONS, pattern="few-shot: zero"))

    scope_examples = [
        {"role": "user", "content": "My VPN drops every twenty minutes on home wifi."},
        {"role": "assistant", "content": '{"classification": "IN_SCOPE", "reason": "Connectivity to company systems is a helpdesk question."}'},
        {"role": "user", "content": "Can you write my performance review for me?"},
        {"role": "assistant", "content": '{"classification": "OUT_OF_SCOPE", "reason": "Not an IT or access question."}'},
        {"role": "user", "content": "Can you book me a meeting room for Thursday?"},
    ]
    print("strong: two examples")
    raw = ask(scope_examples, instructions=SCOPE_INSTRUCTIONS, pattern="few-shot: two examples")
    print(json.dumps(json.loads(raw), indent=2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a JSON object with a classification and a reason. With examples, the reason should sound like the examples. Stop here if `json.loads` fails: the model wrapped the JSON in prose, which Task 4 fixes for good.
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
    ## Task 3 of 7 — Reasoning budget

    Some models can think before they answer, and you can set how much. More effort costs more tokens and more time. Compare no explicit reasoning against a high budget on a question with a trap in it, and read the token counts.
    """)
    return


@app.cell
def _(ask, show, time):
    TRAP = "I need my car cleaned. The car wash is fifty metres away. Should I walk or drive?"


    def timed(effort):
        t0 = time.perf_counter()
        try:
            text = ask(TRAP, effort=effort, pattern=f"reasoning: {effort or 'none'}")
        except Exception as e:  # noqa: BLE001
            return None, 0.0, f"this model has no reasoning budget ({type(e).__name__})"
        return text, time.perf_counter() - t0, ""


    for effort in (None, "high"):
        text, secs, note = timed(effort)
        print(f"effort={effort or 'none'}  latency={secs:0.1f}s  {note}")
        if text:
            show(text)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see two answers with latencies. The trap is that the car has to be at the car wash, so the answer is drive. A higher budget catches it more reliably. Stop here if both say walk and the note says the model has no reasoning budget; that is fine, keep going.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 7 — Structured output

    Asking politely for JSON works most of the time. Most of the time is not good enough for code that calls `json.loads`. A schema makes the shape a contract. Extract a product brief from your charter into a typed object.
    """)
    return


@app.cell
def _(CHARTER, MODEL, PROMPTS: list[dict], client):
    from typing import List, Literal
    from pydantic import BaseModel

    class ProductBrief(BaseModel):
        product_name: str
        problem: str
        users: List[str]
        must_do: List[str]
        must_not_do: List[str]
        risk_level: Literal['low', 'medium', 'high']
    _result = client.chat.completions.parse(model=MODEL, messages=[{'role': 'system', 'content': 'Extract a product brief from the charter.'}, {'role': 'user', 'content': CHARTER}], response_format=ProductBrief)
    brief: ProductBrief = _result.choices[0].message.parsed
    PROMPTS.append({'pattern': 'structured output', 'input': CHARTER, 'output': brief.model_dump_json(indent=2), 'model': MODEL, 'instructions': 'Extract a product brief from the charter.'})
    print(brief.model_dump_json(indent=2))
    return BaseModel, List, Literal


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see valid JSON with every field filled and `risk_level` one of three allowed values. Stop here if you get a validation error: your endpoint may not support structured outputs, and the fallback is the few-shot JSON from Task 2.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 7 — Pasted context

    The model knows nothing about your product. The simplest fix is to paste the document into the system prompt. This is retrieval by hand. Ask a question only your charter can answer, without and then with the charter.
    """)
    return


@app.cell
def _(CHARTER, ask, show):
    CONTEXT_Q = "Who are the two named users of this product, and what does the product refuse to do?"

    print("weak: no context")
    show(ask(CONTEXT_Q, pattern="context: none"))

    GROUNDED = ("Answer using only the charter below. If the charter does not say, say so.\n\n" + CHARTER)
    print("strong: charter pasted in")
    show(ask(CONTEXT_Q, instructions=GROUNDED, pattern="context: charter"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a first answer that guesses or declines, and a second that names the users and the refusals from your charter. Stop here if the second answer invents a user not in the charter.
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

    A first draft is rarely the best draft. Self-refine is two calls: draft, then critique against explicit criteria and revise. The criteria are the point. You can read them, change them, and hand them to a teammate as the definition of good.
    """)
    return


@app.cell
def _(CHARTER, ask, show):
    DRAFT_Q = "Write the one-paragraph pitch for this product that we will read aloud to the room."
    draft = ask(DRAFT_Q, instructions="Use only the charter below.\n\n" + CHARTER, pattern="self-refine: draft")
    print("pass 1: draft")
    show(draft)

    REFINE = ("You are a senior editor. Evaluate the draft against these criteria:\n"
              "1. Under 120 words.\n2. Names a real user from the charter.\n3. Ends with one specific ask.\n\n"
              "Write a two-sentence critique, then the revised pitch under the heading REVISED.\n\n" + CHARTER)
    print("pass 2: critique and revision")
    show(ask(f"DRAFT:\n{draft}\n\nCritique and revise.", instructions=REFINE, pattern="self-refine: revised"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a draft, a short critique naming which criteria failed, and a revised pitch under a REVISED heading. Stop here if the critique says everything passed on the first try: tighten the criteria and rerun.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 7 of 7 — Meta-prompting

    So far you wrote the prompts. Meta-prompting asks the model to write one for you, from a task description, examples of bad output, and your quality bar. Then you run the generated prompt to see if it works.
    """)
    return


@app.cell
def _(CHARTER, QUESTION, ask, show):
    import re

    META = ("You are a prompt engineer. Write a system prompt for the task below. It must be clear and short "
            "and produce consistent outputs. Wrap the final prompt in <PROMPT> and </PROMPT> tags.")
    TASK_DESCRIPTION = f"""
    TASK: answer user questions for the product described in this charter.

    {CHARTER}

    Good output: answers from the charter, names the exact step or entitlement, offers a next action.
    Bad output we have seen: guesses a policy, invents a menu path, answers a question outside the product's scope.
    """
    generated = ask(TASK_DESCRIPTION, instructions=META, pattern="meta-prompt: generate")
    m = re.search(r"<PROMPT>(.*?)</PROMPT>", generated, re.S)
    GENERATED_PROMPT = m.group(1).strip() if m else generated.strip()
    print("generated prompt:")
    show(GENERATED_PROMPT)

    print("the generated prompt in use:")
    show(ask(QUESTION, instructions=GENERATED_PROMPT, pattern="meta-prompt: applied"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a generated system prompt and then an answer to the Task 1 question written under it. Compare it with the Task 1 answers. Stop here if the generated prompt is longer than your charter: ask for a shorter one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Stack three patterns in one call: a persona, the charter as context, and a structured output with a decision (`proceed`, `redesign`, `pause`), a rationale, and up to three risks. Ask whether your group should build the product as described. Then explain to a teammate which pattern did the most work.
    """)
    return


@app.cell
def _(BaseModel, CHARTER, List, Literal, MODEL, PROMPTS: list[dict], client):
    class Decision(BaseModel):
        decision: Literal['proceed', 'redesign', 'pause']
        rationale: str
        risks: List[str]
    STACKED = 'You are a sceptical engineering lead. Give a direct, evidence-based recommendation. Use only the charter below.\n\n' + CHARTER
    _result = client.chat.completions.parse(model=MODEL, messages=[{'role': 'system', 'content': STACKED}, {'role': 'user', 'content': 'Should we build this product as described?'}], response_format=Decision)
    decision: Decision = _result.choices[0].message.parsed
    PROMPTS.append({'pattern': 'stacked', 'input': 'Should we build this product as described?', 'output': decision.model_dump_json(indent=2), 'model': MODEL, 'instructions': STACKED})  # edit the persona
    print(decision.model_dump_json(indent=2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Save your prompts

    Every call this session is in `PROMPTS`. Saving it makes those inputs and outputs part of your workspace, where the retrieval notebooks will index them.
    """)
    return


@app.cell
def _(PROMPTS: list[dict], ws):
    ws.save("prompts", PROMPTS)
    print(f"patterns recorded: {sorted({p['pattern'].split(':')[0] for p in PROMPTS})}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with the row count and a list of pattern names. Stop here if the count is under ten: a task above did not run.
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

    | What we built | Production equivalent |
    |---|---|
    | Two few-shot examples typed by hand | An example store with nearest-neighbour selection per input |
    | The charter pasted into the system prompt | A retrieval pipeline: chunking, vector search, reranking |
    | A two-call self-refine loop | Reflection agents and durable multi-step workflows |
    | A Pydantic model as the output contract | Schema registries and validation middleware shared across teams |
    | One persona string per call | Versioned prompt templates deployed like code, with A/B tests |
    | Reading quality by eye | Judges and regression sets, which the evals notebook builds |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Version every system prompt and record which version produced which output.
    - A regression set of inputs with known-good structured outputs, run on every prompt edit.
    - A reasoning-budget policy per task so cost does not drift with the model.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Build a prompt regression set: five inputs with known-correct structured outputs. Assert on them after every prompt edit.
    - Select few-shot examples dynamically by embedding a labelled library and retrieving the nearest ones per input.
    - Log reasoning tokens and latency for every prompt in your prototype, then set the budget per task rather than globally.
    """)
    return


if __name__ == "__main__":
    app.run()
