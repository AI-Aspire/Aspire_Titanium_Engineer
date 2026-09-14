# Research report: Turn the request into a research brief about an internal support product and its agent. Make the success criteria concrete. The research reads the product's documentation, transcripts, and evaluation notes, so prefer framing that those sources can answer.

Question: The support agent fails the out_of_scope task task-out-of-scope in 1 of 1 runs. What are the likely causes, what does the product's documentation and transcript history say about this case, and what change to the agent, its tools, or its corpus would fix it?

# Research Report: Support Agent `task-out-of-scope` Failure Analysis & Remediation
**Audience:** Internal AI/ML Engineering & Product Ops Teams
**Scope:** Product documentation, conversation transcripts, evaluation notes

## Executive Summary
Research was scoped per the initial brief to analyze `task-out-of-scope` failures and draft a remediation plan. Available materials contain only prompt artifacts; empirical failure logs, transcript data, and evaluation notes are absent. Consequently, the success criteria for identifying ≥3 distinct root causes and delivering validated before/after remediation specifications cannot be met without additional evidence. Current findings are strictly grounded in available prompt architecture and routing logic.

## Methodology & Source Mapping
Research questions were evaluated against three mandated source categories. Every provided source explicitly addresses at least one research question:
- **Product Documentation:** `[prompts/stacked.md]` answers RQ1 (Root Causes) by outlining high-level project risks but reveals zero scope-boundary definitions or constraint failure modes. `[prompts/meta-prompt-applied.md]`, `[prompts/persona-none.md]`, and `[prompts/persona-patient.md]` answer RQ2 (Routing/Tool Scope) by detailing the agent's diagnostic sequencing and conditional escalation triggers.
- **Conversation Transcripts:** Searched for empirical `task-out-of-scope` failure sequences. No transcript artifacts were located to answer either research question.
- **Evaluation Notes:** Reviewed for failure logs, pass/fail metrics, and traceability IDs (Doc Section #, Transcript Run ID, Eval Note Timestamp). No evaluation run logs or timestamps are present in the current dataset.

## Findings: Root Cause Analysis (`task-out-of-scope`)
The success criterion of identifying ≥3 distinct root causes is currently unmet due to the absence of empirical failure data.
- **Documentation Evidence:** `[prompts/stacked.md]` outlines a stacked prompt pattern and lists high-level risks (e.g., undefined success metrics, unscoped integrations) but contains zero references to scope-boundary violations or constraint failure modes.
- **Transcript/Eval Evidence:** No system traces or evaluation logs exist to capture how the agent handles out-of-scope requests in practice. Attributing root causes would violate the no-speculation constraint.

## Findings: Remediation Strategy & Agent Architecture
Based on available prompt artifacts, the agent follows a diagnostic sequencing workflow with conditional routing.
- **Prompt/Routing Logic:** The agent utilizes `meta-prompt` and `persona` patterns to sequence diagnostics (port reachability → DNS verification → VPN/firewall validation) before applying a decision gate `[prompts/meta-prompt-applied.md]`.
- **Escalation Mechanism:** Out-of-scope or permission-restricted tasks trigger a literal `"Open ticket"` phrase to route requests to network/security teams, rather than executing automated tool calls or API endpoints `[prompts/persona-none.md]`, `[prompts/persona-patient.md]`.
- **Base Model:** `unsloth/Qwen3.6-35B-A3B-MTP-GGUF`

While the routing logic is trigger-based, formalized escalation policies, SLAs, and technical definitions of "out-of-scope" are missing from the documentation. Consequently, before/after specifications and validation metrics (e.g., ≥90% pass rate across 3 consecutive runs) cannot be drafted without operational configuration data.

## Open Gaps
- **Empirical Failure Data:** Complete absence of transcripts, evaluation run logs, and system traces documenting `task-out-of-scope` events or constraint violations.
- **Configuration & Permission Schemas:** Tool permission boundaries, access controls, allowed action sets, and corpus retrieval filter configurations are entirely undocumented.
- **Traceability Framework:** Missing standardized IDs (Doc Section #, Transcript Run ID, Eval Note Timestamp) prevent reviewer verification and metric tracking.
- **Remediation Specifications:** Inability to produce required before/after prompt/tool specs or validation thresholds pending data acquisition.

## Path to Success Criteria Compliance
To satisfy the original success criteria, the following artifacts must be provisioned:
1. ≥50 conversation transcripts tagged with `task-out-of-scope` failure instances.
2. Evaluation run logs containing timestamped pass/fail metrics for scope-boundary tests.
3. Operational configuration schemas detailing tool permissions, corpus retrieval filters, and routing triggers.
Once acquired, analysis will yield ≥3 evidence-backed root causes and a prioritized remediation plan with validated before/after specifications. All findings will be mapped to standardized traceability IDs per the original brief constraints.

## Sources

- prompts/stacked.md
- prompts/meta-prompt-applied.md
- prompts/persona-none.md
- prompts/persona-patient.md

## Open gaps

- Complete absence of empirical data (transcripts, evaluation run logs, system traces) documenting `task-out-of-scope` events.
- No prompt or documentation artifacts explicitly analyze scope boundaries or constraint enforcement.
- Current evidence set is insufficient; any root cause attribution would violate the no-speculation constraint.
- No structural configuration schemas for prompts or tool definitions located.
- Tool permission boundaries, access controls, and allowed action sets are undocumented.
- Formalized escalation policies, SLAs, routing rules, and technical definitions of "out-of-scope" are missing.
- Cannot produce required before/after specifications or validation metrics (e.g., ≥90% pass rate) without operational config data.
- Missing standardized traceability IDs (Doc Section #, Transcript Run ID, Eval Note Timestamp) due to absence of empirical artifacts.
- Corpus retrieval filter configurations and tool permission scopes are entirely undocumented.
- Success criteria for root cause identification (≥3 causes) and remediation planning (before/after specs + validation metrics) remain unmet pending data acquisition.

## Trace

| measure | value |
|---|---|
| research tasks | 2 |
| search calls | 2 |
| corpus hits | 4 |
| web hits | 0 |
| sources extracted | 3 |
| distinct sources | 4 |

Model: `unsloth/Qwen3.6-35B-A3B-MTP-GGUF`. Web search: off.