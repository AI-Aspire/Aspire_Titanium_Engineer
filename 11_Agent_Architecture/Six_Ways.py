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
    # Six ways to give an agent a capability

    The same capability, looking up one of your eval cases or agent runs, built six ways: a tool, a skill, an MCP server, a sub-agent, a code-mode runtime, and an API described by a manifest. The point is not six demos. It is seeing where code runs, who owns the boundary, what enters model context, and how each choice fails.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    One capability six ways: a tool, a skill folder, an MCP server, a sub-agent, a code-mode runtime, a manifest-described API. What reaches the model in each, and what breaks first.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    A catalogue that says when to use each mechanism, written for the one lookup your prototype needs most and saved to your workspace.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Production picks a mechanism per capability by ownership, auth, and what enters context. Tell your team, for two mechanisms on one question, the call count and context size.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 45 minutes
    **Reads:** eval_cases, trajectories
    **Writes:** tools_catalog
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    One chat model that supports tool calling. Every mechanism answers from the same two artifacts, so only the architecture changes between tasks. The `chat` helper returns the reply and any tool calls in the OpenAI shape.
    """)
    return


@app.cell
def _():
    import ast, asyncio, json, os, re, shlex, subprocess, sys, textwrap, threading, time
    from pathlib import Path

    from openai import OpenAI

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, require
    from helpers import workspace as ws
    from helpers.llm import client

    require("OPENAI_API_KEY")
    client = client()
    CASES = ws.load("eval_cases")
    TRAJECTORIES = ws.load("trajectories")

    def chat(messages: list[dict], tools: list | None = None) -> dict:
        """One chat call. Returns {"content": str, "tool_calls": [openai-shaped dicts]}."""
        kw = dict(model=LLM_MODEL, messages=messages, temperature=0)
        if tools:
            kw["tools"], kw["tool_choice"] = tools, "auto"
        m = client.chat.completions.create(**kw).choices[0].message
        return {"content": m.content or "",
                "tool_calls": [{"id": tc.id, "type": "function",
                                "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
                               for tc in (m.tool_calls or [])]}

    print(f"✅ model {LLM_MODEL}; {len(CASES)} eval cases; {len(TRAJECTORIES)} trajectories")
    return (
        CASES,
        Path,
        TRAJECTORIES,
        ast,
        asyncio,
        chat,
        json,
        os,
        re,
        shlex,
        subprocess,
        sys,
        textwrap,
        threading,
        time,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with the model and two counts above zero. Stop here if either count is zero: run the eval cases and trajectory evals notebooks first, or let the seed carry them.
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
    ## Task 1 of 7 — A tool

    The default way to give an agent a capability. Write a function, describe it with a JSON schema, and hand the schema to the model. The model decides when to call it; your loop runs it and feeds the result back. It lives in your code and your process, so you own the wiring. The function below finds a case or a trajectory by id, or the closest cases to a question.
    """)
    return


@app.cell
def _(CASES, TRAJECTORIES, chat, json, re, textwrap):
    STOP = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'how', 'i', 'in', 'is', 'it', 'of', 'on', 'or', 'our', 'should', 'that', 'the', 'their', 'to', 'what', 'when', 'with', 'my', 'can', 'do', 'does', 'this', 'you', 'your', 'me', 'we', 'not', 'but', 'if', 'so', 'was', 'will', 'have', 'has'}
    CASE_BY_ID = {str(c['id']): c for c in CASES}
    TRAJ_BY_ID = {str(t['id']): t for t in TRAJECTORIES}

    def terms(text: str) -> set[str]:
        return {t for t in re.findall('[a-z0-9][a-z0-9-]+', text.lower()) if t not in STOP}

    def case_view(c: dict) -> dict:
        runs = [t for t in TRAJECTORIES if str(t['task_id']).endswith(str(c['id']))]
        return {'case': c['id'], 'question': c['question'], 'reference': c.get('reference', ''), 'runs': [{'trajectory': t['id'], 'passed': bool(t['passed'])} for t in runs]}

    def trajectory_view(t: dict) -> dict:
        return {'trajectory': t['id'], 'task_id': t['task_id'], 'passed': bool(t['passed']), 'tools': [s['name'] for s in t['steps'] if s['role'] == 'tool'], 'final': next((s['content'] for s in reversed(t['steps']) if s['role'] == 'assistant'), '')}

    def lookup(query: str) -> str:
        """Find an eval case or a trajectory by id, or the eval cases closest to a question."""
        q = query.strip()
        if q in CASE_BY_ID:
            return json.dumps(case_view(CASE_BY_ID[q]))
        if q in TRAJ_BY_ID:
            return json.dumps(trajectory_view(TRAJ_BY_ID[q]))
        words = terms(q)
        ranked = sorted(CASES, key=lambda c: len(words & terms(c['question'] + ' ' + c.get('reference', ''))), reverse=True)[:3]
        hits = [{'case': c['id'], 'question': c['question'], 'reference': textwrap.shorten(c.get('reference', ''), 200)} for c in ranked if words & terms(c['question'] + ' ' + c.get('reference', ''))]
        return json.dumps(hits) if hits else '(no case matched)'
    TOOLS = [{'type': 'function', 'function': {'name': 'lookup', 'description': 'Look up an eval case or an agent trajectory by id, or find the cases closest to a question.', 'parameters': {'type': 'object', 'properties': {'query': {'type': 'string'}}, 'required': ['query']}}}]
    FUNCS = {'lookup': lookup}
    SYSTEM = "You answer questions about the team's eval cases and agent runs. Use your tool and quote ids."

    def run_tool_agent(question: str, max_turns: int=5) -> tuple[str, list]:
        msgs = [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': question}]
        trace = []
        for _ in range(max_turns):
            r = chat(msgs, tools=TOOLS)
            if not r['tool_calls']:
                return (r['content'], trace)
            msgs.append({'role': 'assistant', 'content': r['content'], 'tool_calls': r['tool_calls']})
            for tc in r['tool_calls']:
                args = json.loads(tc['function']['arguments'] or '{}')
                out = str(FUNCS[tc['function']['name']](**args))
                trace.append((tc['function']['name'], args, len(out)))
                msgs.append({'role': 'tool', 'tool_call_id': tc['id'], 'content': out})
        return ('(max turns)', trace)
    QUESTION = f"What is eval case {CASES[0]['id']} about, and did the agent pass it?"
    _answer, _trace = run_tool_agent(QUESTION)
    print('tool calls:', _trace)
    print(textwrap.shorten(_answer, 400))
    return QUESTION, SYSTEM, lookup, run_tool_agent, trajectory_view


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one `lookup` call with the case id, the number of characters it returned, and an answer that quotes the question and says whether the runs passed. Stop here if the trace is empty: the model answered without the tool, so the description is too vague.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 7 — A skill

    A skill is not a function you wire in. It is a folder with a `SKILL.md`, plain-English instructions, and a script. The harness reads the instructions, decides to use the skill, and runs the script, feeding the output back. No JSON schema and no API plumbing. That the harness shells out is also the risk, so a real harness sandboxes it. Ours allows the one documented command.
    """)
    return


@app.cell
def _(Path):
    SKILL_DIR = Path("skills/case_lookup")
    print(SKILL_DIR.joinpath("SKILL.md").read_text(encoding="utf-8"))
    return (SKILL_DIR,)


@app.cell
def _(Path, QUESTION, SKILL_DIR, chat, shlex, subprocess, sys, textwrap):
    def run_skill_agent(question: str, skill_dir: Path=SKILL_DIR, max_steps: int=4) -> tuple[str, list]:
        skill_md = (skill_dir / 'SKILL.md').read_text(encoding='utf-8')
        sys_prompt = "You answer questions about the team's eval cases and agent runs. You have this SKILL available:\n\n" + skill_md + '\n\nWhen the skill says to run a command, reply with EXACTLY one line: RUN: <command>\nAfter you see its output, answer the user in plain English.'
        msgs = [{'role': 'system', 'content': sys_prompt}, {'role': 'user', 'content': question}]
        trace = []
        for _ in range(max_steps):
            out = chat(msgs)['content'].strip()
            if not out.startswith('RUN:'):
                return (out, trace)
            cmd = out[4:].strip()
            if not cmd.startswith('python run.py'):
                msgs += [{'role': 'assistant', 'content': out}, {'role': 'user', 'content': "Blocked: only the skill's `python run.py` may run."}]
                continue  # harness guard: only the documented command
            trace.append(cmd)
            argv = shlex.split(cmd)
            argv[0] = sys.executable
            res = subprocess.run(argv, cwd=skill_dir, capture_output=True, text=True)
            msgs += [{'role': 'assistant', 'content': out}, {'role': 'user', 'content': f'Command output:\n{res.stdout or res.stderr}'}]
        return (out, trace)  # the notebook's own interpreter
    _answer, _trace = run_skill_agent(QUESTION)
    print('harness ran:', _trace)
    print(textwrap.shorten(_answer, 400))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the SKILL.md text, then one `python run.py ...` command and an answer built from its JSON. Stop here if the harness ran nothing: the model did not reply with a `RUN:` line, so print its raw reply.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    The tool and the skill answered the same question. Which one could a teammate reuse in a different application without reading your notebook, and what would they have to copy?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 7 — An MCP server

    A tool lives in your process. An MCP server is a separate process that exposes tools over the Model Context Protocol, so any MCP-aware client can discover and call them behind a stable contract. The notebook launches `mcp_server.py` as a subprocess over stdio, discovers its tools, and runs the same loop against them. You never wrote a schema here; the agent discovered it.
    """)
    return


@app.cell
def _(
    Path,
    QUESTION,
    SYSTEM,
    asyncio,
    chat,
    json,
    os,
    sys,
    textwrap,
    threading,
):
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    SERVER = str(Path('mcp_server.py').resolve())

    async def run_mcp_agent(question: str, max_turns: int=6):
        params = StdioServerParameters(command=sys.executable, args=[SERVER], env=dict(os.environ))
        async with stdio_client(params) as (read, write_):
            async with ClientSession(read, write_) as session:  # pass .env and TE_WORKSPACE through
                await session.initialize()
                discovered = (await session.list_tools()).tools
                oai = [{'type': 'function', 'function': {'name': t.name, 'description': t.description, 'parameters': t.input_schema}} for t in discovered]
                msgs = [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': question}]  # the agent learns the tools at runtime
                calls = []
                for _ in range(max_turns):
                    r = chat(msgs, tools=oai)
                    if not r['tool_calls']:
                        return (r['content'], [t.name for t in discovered], calls)
                    msgs.append({'role': 'assistant', 'content': r['content'], 'tool_calls': r['tool_calls']})
                    for tc in r['tool_calls']:
                        args = json.loads(tc['function']['arguments'] or '{}')
                        res = await session.call_tool(tc['function']['name'], args)
                        calls.append(tc['function']['name'])
                        out = '\n'.join((b.text for b in res.content if hasattr(b, 'text'))) or '(tool returned no text)'
                        if getattr(res, 'is_error', False):
                            out = 'MCP tool error: ' + out
                        msgs.append({'role': 'tool', 'tool_call_id': tc['id'], 'content': out})
                return ('(max turns)', [t.name for t in discovered], calls)

    def run_sync(coro):
        """Run a coroutine on its own thread, so it works whether or not the notebook already has an event loop."""
        out = {}

        def _run():
            try:
                out['value'] = asyncio.run(coro)
            except BaseException as e:
                out['error'] = e
        th = threading.Thread(target=_run)
        th.start()
        th.join()  # noqa: BLE001 - re-raised below
        if 'error' in out:
            raise out['error']
        return out['value']
    _answer, discovered, calls = run_sync(run_mcp_agent(QUESTION))
    print('server exposed:', discovered)
    print('agent called:  ', calls)
    print(textwrap.shorten(_answer, 400))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see three discovered tool names, at least one call, and an answer. Stop here if the session never initialises: run `uv run python mcp_server.py` from this folder in a terminal and read the error; a stray print in the server breaks the protocol.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 7 — A sub-agent

    The first three are capabilities. A sub-agent is a colleague: a separate agent with its own prompt, its own context, and its own loop, that the main agent delegates to. From the coordinator's side, delegating looks like calling a tool. Behind that one tool sits a whole agent that reads the trajectories and answers.
    """)
    return


@app.cell
def _(TRAJECTORIES, chat, json, textwrap, trajectory_view):
    def trajectory_analyst(question: str) -> str:
        """A separate agent: its own prompt, its own reference material, a finished answer."""
        views = [trajectory_view(t) for t in TRAJECTORIES[:12]]
        msgs = [{'role': 'system', 'content': "You are the analyst for the team's agent runs. Answer only from the runs given, name trajectory ids, and say plainly when a run failed and why."}, {'role': 'user', 'content': f'{question}\n\nRUNS:\n{json.dumps(views, indent=1)}'}]
        return chat(msgs)['content'].strip()
    DELEGATE = [{'type': 'function', 'function': {'name': 'ask_trajectory_analyst', 'description': 'Delegate any question about agent runs, passes, failures, or trajectories to the analyst sub-agent.', 'parameters': {'type': 'object', 'properties': {'question': {'type': 'string'}}, 'required': ['question']}}}]

    def run_coordinator(question: str) -> tuple[str, str | None]:
        msgs = [{'role': 'system', 'content': 'You are a routing coordinator with NO knowledge of the agent runs yourself. For ANY question about whether the agent passed, what it did, or its trajectories you MUST call ask_trajectory_analyst. Answer only unrelated questions directly.'}, {'role': 'user', 'content': question}]
        r = chat(msgs, tools=DELEGATE)
        if not r['tool_calls']:
            return (r['content'].strip(), None)
        tc = r['tool_calls'][0]
        sub_answer = trajectory_analyst(json.loads(tc['function']['arguments'] or '{}')['question'])
        msgs.append({'role': 'assistant', 'content': '', 'tool_calls': [tc]})
        msgs.append({'role': 'tool', 'tool_call_id': tc['id'], 'content': sub_answer})
        return (chat(msgs)['content'].strip(), sub_answer)
    _answer, sub = run_coordinator('Which agent run failed, and what did it do wrong?')
    print('delegated:', 'yes' if sub else 'no')
    print(textwrap.shorten(_answer, 500))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see `delegated: yes` and an answer that names a trajectory id and a reason. Stop here if it says no: the coordinator answered from nothing, so its system prompt is not forcing the delegation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    What did the coordinator never see that the analyst did? When is that hiding a feature, and when is it a debugging problem?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 7 — Code mode

    Normal tool calling sends every intermediate result back through the model. In code mode the model writes a small program and a runtime executes it. Calls and intermediate values can stay inside the runtime; only the program's final `answer` returns. The validator below keeps the lesson deterministic. It is not a sandbox: production needs a subprocess, container, or WASM runtime with limits.
    """)
    return


@app.cell
def _(CASES, ast, chat, json, lookup, re, textwrap):
    def lookup_data(query: str):
        """The same capability, handing the program data rather than JSON text.

        A program that indexes the result as a dict is the natural thing for the
        model to write, and it is only wrong when the value is a string."""
        out = lookup(query)
        try:
            return json.loads(out)
        except ValueError:
            return out
    CODE_CAPABILITIES = {'lookup': lookup_data}
    ALLOWED_NODES = {ast.Module, ast.Assign, ast.Expr, ast.Name, ast.Load, ast.Store, ast.Constant, ast.Call, ast.keyword, ast.List, ast.Tuple, ast.Dict, ast.JoinedStr, ast.FormattedValue, ast.Subscript, ast.Slice, ast.BinOp, ast.Add, ast.IfExp, ast.Compare, ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.In, ast.NotIn, ast.Is, ast.IsNot, ast.BoolOp, ast.And, ast.Or, ast.UnaryOp, ast.Not}

    # Literal programs only: no imports, loops, attributes, or definitions. Comparisons,
    # and/or/not, and a conditional expression are in because models reach for them.
    def validate_program(source: str) -> ast.Module:
        """Only direct calls to the bound capabilities, only simple syntax, and a result named `answer`."""
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if type(node) not in ALLOWED_NODES:
                raise ValueError(f'unsupported syntax in the lesson runtime: {type(node).__name__}')
            if isinstance(node, ast.Call) and (not (isinstance(node.func, ast.Name) and node.func.id in CODE_CAPABILITIES)):
                raise ValueError('only direct capability calls are allowed')
        assigned = {t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
        if 'answer' not in assigned:
            raise ValueError('the program must assign its result to `answer`')
        return tree

    def run_code_mode(question: str) -> tuple[str, str]:
        prompt = f'Write Python for this question: {question}\nAvailable function: lookup(query: str), which returns a dict for an id (keys: case, question, reference, runs) or a list of such dicts for a question.\nAssign the final response, quoting ids, to a variable named answer.\nUse only direct calls, variables, lists, dicts, indexing, +, comparisons, and/or/not, a conditional expression, and f-strings. No imports, no loops, no attribute access.\nReturn Python only, without Markdown fences.'
        source = chat([{'role': 'system', 'content': 'You write small, literal Python programs.'}, {'role': 'user', 'content': prompt}])['content'].strip()
        source = re.sub('^```(?:python)?\\s*|\\s*```$', '', source, flags=re.I | re.S).strip()
        try:
            tree = validate_program(source)
        except (ValueError, SyntaxError) as e:
            return (f'the validator rejected the program: {e}', source)
        namespace = dict(CODE_CAPABILITIES)
        try:
            exec(compile(tree, '<code-mode-lesson>', 'exec'), {'__builtins__': {}}, namespace)
        except Exception as e:
            return (f'the program raised {type(e).__name__}: {e}', source)
        return (str(namespace['answer']), source)
    ids = [str(c['id']) for c in CASES[:2]]
    _answer, program = run_code_mode(f'Look up eval cases {ids[0]} and {ids[1]} and report both questions in one line.')
    print('generated program:\n' + program + '\n')
    print('runtime returned:', textwrap.shorten(_answer, 400))  # what the model wrote is the finding, not a crash  # noqa: BLE001  the program is the model's; its failure is the result
    return ids, run_code_mode


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a short program with two `lookup(...)` calls and an `answer = ...` line, then the runtime's result. Stop here if the runtime reports an error instead: read the program against the error, and decide whether the runtime or the prompt should change.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 7 — An API described by a manifest

    The UTCP pattern describes an API the organisation already runs instead of wrapping it in a new server. A client reads the manifest, turns each entry into a model-facing schema, and calls the original endpoint directly. The manifest and dispatcher below are a teaching subset, not a full implementation: discovery is separate from invocation, transport lives in the manifest, and credentials stay with the client.
    """)
    return


@app.cell
def _(QUESTION, SYSTEM, chat, json, lookup, textwrap):
    UTCP_MANIFEST = {'version': '1.0', 'name': 'eval-lookup-api', 'tools': [{'name': 'lookup', 'description': 'Fetch one eval case or trajectory by id, or the closest cases to a question, from the evals API.', 'inputs': {'type': 'object', 'properties': {'query': {'type': 'string'}}, 'required': ['query'], 'additionalProperties': False}, 'call': {'method': 'GET', 'url': 'https://evals.example/lookup?q={query}'}}]}

    def utcp_model_tools(manifest: dict) -> list[dict]:
        return [{'type': 'function', 'function': {'name': t['name'], 'description': t['description'], 'parameters': t['inputs']}} for t in manifest['tools']]

    def utcp_invoke(manifest: dict, name: str, arguments: dict) -> tuple[str, str]:
        item = next((t for t in manifest['tools'] if t['name'] == name), None)
        if item is None:
            raise ValueError(f'manifest has no tool named {name!r}')
        query = arguments.get('query')
        if not isinstance(query, str) or not query.strip():
            raise ValueError('query must be a non-empty string')
        resolved_url = item['call']['url'].format(query=query.replace(' ', '+'))
        return (lookup(query), resolved_url)

    def run_utcp_agent(question: str, max_turns: int=5) -> tuple[str, list]:
        tools = utcp_model_tools(UTCP_MANIFEST)
        msgs = [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': question}]
        trace = []
        for _ in range(max_turns):
            r = chat(msgs, tools=tools)
            if not r['tool_calls']:
                return (r['content'], trace)
            msgs.append({'role': 'assistant', 'content': r['content'], 'tool_calls': r['tool_calls']})
            for tc in r['tool_calls']:
                out, url = utcp_invoke(UTCP_MANIFEST, tc['function']['name'], json.loads(tc['function']['arguments'] or '{}'))
                trace.append(url)  # Lesson adapter: the existing endpoint is emulated by the same local function.
                msgs.append({'role': 'tool', 'tool_call_id': tc['id'], 'content': out})  # A real client would send an authenticated GET to resolved_url.
        return ('(max turns)', trace)
    _answer, _trace = run_utcp_agent(QUESTION)
    print('resolved from the manifest:', _trace)
    print(textwrap.shorten(_answer, 400))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one resolved URL containing the case id and the same kind of answer as the tool gave. Stop here if the URL has spaces or is empty: the argument validation in `utcp_invoke` is not running.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    The manifest points at an endpoint that does not exist. What in your organisation already has an API that a manifest could describe today, and who owns its schema?

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
    ## Task 7 of 7 — Six mechanisms, one catalogue

    | Mechanism | Boundary | Reaches context | Main risk |
    |---|---|---|---|
    | Tool | in-process function | each result | tight coupling |
    | Skill | a folder with a script | SOP and command output | unsafe execution |
    | MCP | protocol server | selected results | auth, uptime, versions |
    | Sub-agent | separate context | the specialist's answer | opaque handoffs |
    | Code mode | execution runtime | program, final result | arbitrary code |
    | UTCP | existing API, a manifest | selected responses | schema drift |

    Write the catalogue: name, kind, and one line on when to use each.
    """)
    return


@app.cell
def _(ws):
    CATALOG = {"capability": "Look up an eval case or a trajectory by id or by question", "tools": [
        {"name": "lookup", "kind": "tool",
         "when_to_use": "A small capability owned by one application; you own the wiring and the schema."},
        {"name": "case_lookup", "kind": "skill",
         "when_to_use": "The reusable asset is mostly a procedure; drop in a folder and let the harness run the script."},
        {"name": "mcp_server.py", "kind": "mcp",
         "when_to_use": "Several clients need runtime discovery of a capability someone else operates."},
        {"name": "ask_trajectory_analyst", "kind": "sub-agent",
         "when_to_use": "The valuable boundary is separate reasoning, context, or policy, not just a function."},
        {"name": "run_code_mode", "kind": "code-mode",
         "when_to_use": "Many calls or bulky intermediates justify a hardened execution runtime."},
        {"name": "eval-lookup-api", "kind": "utcp",
         "when_to_use": "An API already exists and a manifest can describe it without adding a proxy server."},
    ]}
    ws.save("tools_catalog", CATALOG)
    for t in CATALOG["tools"]:
        print(f"{t['kind']:<10} {t['name']:<24} {t['when_to_use']}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line and six rows, one per kind. Edit the `when_to_use` lines to match your product before you move on; the seed lines are generic.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Make the trade-off measurable. Run the same question through the tool and through code mode. Count model calls and capability calls, the characters of evidence that entered model context, and the elapsed time. Then say which mechanism you would pick for a single internal prototype and which for a capability shared by several teams.
    """)
    return


@app.cell
def _(ids, run_code_mode, run_tool_agent, time):
    def measure(label: str, fn, question: str) -> dict:
        start = time.perf_counter()
        result = fn(question)
        return {"mechanism": label, "seconds": round(time.perf_counter() - start, 1),
                "chars_returned": len(str(result[0])), "trace": result[1]}


    q = f"Compare eval cases {ids[0]} and {ids[1]}: which one did the agent pass?"
    for row in (measure("tool", run_tool_agent, q), measure("code-mode", run_code_mode, q)):
        print(row)
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
    | An in-process Python tool | Validation, least privilege, retries, audit logs |
    | One allow-listed skill command | Signed, versioned assets in an isolated runtime |
    | A stdio MCP server | Authenticated deployment, health checks, protocol version tests |
    | One coordinator and one specialist | Routing evals, trace propagation, budgets, failure recovery |
    | AST checks plus `exec` | A real subprocess, container, or WASM sandbox with resource and I/O policy |
    | A local manifest dispatcher | A conforming client with authenticated HTTP and schema versioning |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - An owner named for every entry in the tool catalogue.
    - Code mode runs in a sandbox, never in the notebook process.
    - MCP servers authenticated and their schemas versioned.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Put code mode in a locked-down subprocess with a two-second timeout. Test an infinite loop, a file read, an import, and oversized output.
    - Serve the lookup behind a small authenticated HTTP API, publish its manifest, and replace the lesson dispatcher with a real client call.
    - Introduce one controlled failure per mechanism (bad arguments, a stale skill, a server that is down, a bad delegation, unsafe code, a stale manifest) and check that each fails visibly.
    """)
    return


if __name__ == "__main__":
    app.run()
