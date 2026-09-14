# Prompt pattern: stacked

## Example 1

**Input**

Should we build this product as described?

**Output**

{
  "decision": "proceed",
  "rationale": "The user wants a direct, evidence-based recommendation from a skeptical engineering lead perspective, using only the provided charter. The draft meets all constraints: it's blunt, ties every point to explicit charter text (groundedness scores, guardrail cases, deflection/audit needs, confirmation rules, failure modes), avoids external assumptions, and gives a conditional go/no-go with clear next steps.",
  "risks": [
    "Post-hoc detection instead of prevention for known failure modes",
    "Undefined success metrics despite clear user goals",
    "Unscoped integration surface and recovery paths"
  ]
}

_Model: unsloth/Qwen3.6-35B-A3B-MTP-GGUF_
