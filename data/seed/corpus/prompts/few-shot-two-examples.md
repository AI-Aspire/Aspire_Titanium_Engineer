# Prompt pattern: few-shot: two examples

## Example 1

**Input**

[{"role": "user", "content": "My VPN drops every twenty minutes on home wifi."}, {"role": "assistant", "content": "{\"classification\": \"IN_SCOPE\", \"reason\": \"Connectivity to company systems is a helpdesk question.\"}"}, {"role": "user", "content": "Can you write my performance review for me?"}, {"role": "assistant", "content": "{\"classification\": \"OUT_OF_SCOPE\", \"reason\": \"Not an IT or access question.\"}"}, {"role": "user", "content": "Can you book me a meeting room for Thursday?"}]

**Output**

{"classification": "OUT_OF_SCOPE", "reason": "Booking a meeting room is an administrative task, not an IT helpdesk issue."}

_Model: unsloth/Qwen3.6-35B-A3B-MTP-GGUF_
