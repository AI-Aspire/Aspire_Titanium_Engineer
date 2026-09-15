"""Eval lookup MCP server: the eval cases and trajectories as tools over the Model Context Protocol.

Run standalone from this folder:   uv run python mcp_server.py
Or let the notebook launch it as a subprocess over stdio, which is the usual MCP pattern.

Nothing here may print to stdout except the server itself: stdout is the protocol channel.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mcp.server.fastmcp import FastMCP  # noqa: E402

import eval_lookup  # noqa: E402

server = FastMCP("Eval lookup", log_level="WARNING")


@server.tool()
def get_case(case_id: str) -> str:
    """Return one eval case by id: its question, reference answer, and which agent runs passed it."""
    found = eval_lookup.get_case(case_id)
    return json.dumps(found) if found else f"(no eval case {case_id})"


@server.tool()
def get_trajectory(trajectory_id: str) -> str:
    """Return one agent trajectory by id: whether it passed, the tools it called, and its final answer."""
    found = eval_lookup.get_trajectory(trajectory_id)
    return json.dumps(found) if found else f"(no trajectory {trajectory_id})"


@server.tool()
def search_cases(query: str) -> str:
    """Find the eval cases whose question or reference shares the most words with the query."""
    hits = eval_lookup.search_cases(query)
    return json.dumps(hits) if hits else "(no case matched)"


if __name__ == "__main__":
    server.run()  # stdio transport by default
