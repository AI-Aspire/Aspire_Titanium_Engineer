# Prompt pattern: self-refine: revised

## Example 1

**Input**

DRAFT:
Every engineer in the building wastes time waiting a full day for helpdesk answers to the same forty recurring issues, while our twelve-page knowledge base goes unread. Deskmate changes that by instantly resolving these questions using your personal ticket history and our verified knowledge base—giving you exact menu paths, commands, and approval workflows instead of ticket numbers. For your helpdesk team, it automatically filters out repetitive requests before they hit the queue, provides a complete audit log, and strictly enforces security boundaries by refusing unverified entitlements and never leaking another user’s data. When Deskmate can’t help, it opens a ticket for you; when it needs to change something, it asks first. Built with continuous groundedness checks and strict user-scoped retrieval, Deskmate turns your helpdesk from a daily bottleneck into a seamless, secure, and instant engineering experience.

Critique and revise.

**Output**

Critique: The draft exceeds the word limit, omits the required named user from the charter, and concludes with a feature summary rather than a direct call to action. Trim it significantly, explicitly reference Priya or Marcus, and close with a single, concrete request.

REVISED
Priya, a backend engineer, wastes hours waiting a day for answers to the same forty recurring IT issues while your twelve-page knowledge base sits unread. Deskmate instantly resolves these questions using verified documentation and ticket history, providing exact menu paths and commands without opening a ticket. It filters repetitive requests before they reach Marcus’s queue, maintains an auditable log, and strictly enforces security by refusing unverified entitlements or leaking data. When unsure, it opens a ticket; when changing anything, it asks first. Please approve the Deskmate pilot next quarter.

_Model: unsloth/Qwen3.6-35B-A3B-MTP-GGUF_
