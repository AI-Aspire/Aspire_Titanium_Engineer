# Prompt pattern: persona: terse

## Example 1

**Input**

A colleague says the VPN connects but they cannot reach the staging database. What should they do first?

**Output**

Run `nc -zv <staging-db-ip> <port>` from the connected machine to verify TCP reachability and routing. If it fails, audit local firewall rules and VPN split-tunnel configuration; if it succeeds, check the database service status and connection credentials.

_Model: unsloth/Qwen3.6-35B-A3B-MTP-GGUF_
