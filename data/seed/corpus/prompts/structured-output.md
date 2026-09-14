# Prompt pattern: structured output

## Example 1

**Input**

# Charter: Deskmate

## The problem

Every engineer in the building files a helpdesk ticket about once a month:
a VPN that drops, an access request that sits in a queue, a laptop that will
not install a package. The helpdesk answers the same forty questions on
repeat, first response takes a day, and the knowledge base that would answer
most of them is twelve pages nobody reads.

## The users

- **Priya, a backend engineer.** Asks "why can't I reach the staging database
  from the VPN" at 9 am and wants a fix, not a ticket number.
- **Marcus, the helpdesk lead.** Wants the repeat questions answered before
  they reach his queue, and a log he can audit.

## The product vision

Deskmate answers helpdesk questions from the knowledge base and the user's own
ticket history, opens a ticket when it cannot, and never resets anything
without confirmation.

It refuses to touch entitlements it cannot verify and never repeats another
user's ticket text.

## What a good answer looks like

1. "My VPN connects but I cannot reach staging." A good answer names the split
   tunnel setting and the exact menu path, and offers to open a ticket if that
   does not fix it.
2. "How do I get access to the analytics warehouse?" A good answer names the
   entitlement, who approves it, and the expected wait.
3. "`uv sync` removed a package I installed yesterday." A good answer explains
   that a plain sync drops optional groups and gives the `make setup` command.

## Where it will be wrong

- It will answer confidently from a stale page after a policy changes. We will
  notice when the judge's groundedness score drops on the eval cases.
- It will leak one user's ticket into another's answer if retrieval is not
  scoped by user. We will notice with a guardrail case that plants a name.


**Output**

{
  "product_name": "Deskmate",
  "problem": "Engineers submit ~1 repetitive IT helpdesk ticket monthly (VPN drops, access requests, package installation failures). Current first response time is ~24 hours, helpdesk staff burn out answering the same questions repeatedly, and the existing knowledge base is outdated and unused.",
  "users": [
    "End-Users/Engineers (e.g., Priya): Need immediate, actionable fixes without ticketing bureaucracy or wait times.",
    "Helpdesk Leads (e.g., Marcus): Want automated deflection of repeat queries, reduced queue volume, and a complete audit trail for monitoring."
  ],
  "must_do": [
    "Answer helpdesk questions using the knowledge base and the user's own ticket history.",
    "Provide specific, step-by-step solutions (exact menu paths, CLI commands, approval workflows).",
    "Open a helpdesk ticket automatically when the query cannot be resolved autonomously.",
    "Require explicit user confirmation before performing any system resets or changes.",
    "Verify entitlements before acting; refuse unverified access requests.",
    "Enforce strict user-scoped retrieval to prevent cross-user data leakage."
  ],
  "must_not_do": [
    "Reset or modify systems without explicit user confirmation.",
    "Share, reference, or repeat another user's private ticket data.",
    "Act on entitlements that cannot be verified by the system."
  ],
  "risk_level": "medium"
}

_Model: unsloth/Qwen3.6-35B-A3B-MTP-GGUF_
