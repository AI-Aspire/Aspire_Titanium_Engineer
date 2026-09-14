# Research report: Turn the request into a research brief about an internal support product and its agent. Make the success criteria concrete. The research reads the product's documentation, transcripts, and evaluation notes, so prefer framing that those sources can answer.

Question: The support agent fails the out_of_scope task task-out-of-scope in 1 of 1 runs. What are the likely causes, what does the product's documentation and transcript history say about this case, and what change to the agent, its tools, or its corpus would fix it?

# Research Report: Internal Support Agent Scope Classification & Evaluation Readiness
**Audience:** Product engineering, AI safety/evaluation team, documentation owners

## Executive Summary
This investigation was strictly limited to static prompt analysis and available knowledge base artifacts. The requested success criteria cannot be validated due to a complete absence of empirical evaluation data, misclassification logs, and regression test results in the reviewed sources [prompts/few-shot-two-examples.md][prompts/few-shot-zero.md][prompts/meta-prompt-generate.md]. While the agent’s architecture and prompt logic are documented, the research purpose (mapping root causes and validating fixes) is currently unfulfillable without missing artifacts.

## Findings Against Success Criteria
- **Accuracy (≥95%) & False Acceptance (≤2%):** Cannot be assessed. The reviewed sources contain only prompt specifications [prompts/few-shot-two-examples.md][prompts/few-shot-zero.md][prompts/meta-prompt-generate.md] and a single KB article [kb/vpn.md]. No evaluation metrics, labeled test sets, or ground-truth comparisons exist to calculate accuracy or false acceptance rates.
- **Traceability:** Prompt specifications are explicitly traceable to the prompt files, which enforce JSON output contracts (`classification`, `reason`) and structured reasoning for `IN_SCOPE`/`OUT_OF_SCOPE` classification [prompts/few-shot-two-examples.md][prompts/few-shot-zero.md]. However, root-cause findings cannot be mapped to product documentation or transcripts because failure evidence is entirely absent.
- **Regression Testing (<1% Degradation):** Cannot be verified. No regression test data, performance baselines, or methodology for the 1% threshold exists in the reviewed artifacts [prompts/few-shot-zero.md].

## Open gaps
Evidence required to satisfy the research brief constraints is incomplete across three critical areas:
- **Empirical Void:** Zero validation artifacts exist in the reviewed sources. Evaluation notes, labeled test sets, and error transcripts are missing, making it impossible to validate accuracy, false acceptance, or traceability requirements [prompts/meta-prompt-generate.md].
- **Scope Ambiguity:** Formal product scope documentation is absent. Scope boundaries (IT helpdesk vs. Admin/HR) and exclusion patterns were inferred solely from prompt examples [prompts/few-shot-two-examples.md]. Per brief constraints, any deviation requires documented justification, which cannot be provided without official scope docs [kb/vpn.md].
- **Regression Blocker:** Regression audit is impossible without test data or a defined threshold methodology. On-scope performance degradation cannot be measured against the >1% limit [prompts/few-shot-zero.md].

## Actionable Next Steps for Engineering & Eval Teams
1. **Artifact Collection:** Prioritize ingesting historical evaluation notes, labeled out-of-scope test sets, and misclassification transcripts to enable empirical validation.
2. **Scope Documentation:** Author and publish a formal product scope document to replace prompt-inferred boundaries, ensuring compliance with strict deviation constraints.
3. **Regression Pipeline:** Establish a baseline regression testing methodology and dataset to verify that prompt/architecture changes do not degrade on-scope performance by >1%.

## Sources

- prompts/few-shot-two-examples.md
- prompts/few-shot-zero.md
- prompts/meta-prompt-generate.md
- kb/vpn.md

## Open gaps

- Empirical Void: Zero validation artifacts (eval metrics, labeled sets, failure transcripts) in reviewed sources. Research cannot fulfill brief requirements without these.
- Scope Ambiguity: Deviations from scope cannot be justified per constraints due to missing formal scope documentation.
- Regression Blocker: Missing regression data prevents compliance verification for on-scope performance.

## Trace

| measure | value |
|---|---|
| research tasks | 2 |
| search calls | 2 |
| corpus hits | 6 |
| web hits | 0 |
| sources extracted | 4 |
| distinct sources | 4 |

Model: `unsloth/Qwen3.6-35B-A3B-MTP-GGUF`. Web search: off.