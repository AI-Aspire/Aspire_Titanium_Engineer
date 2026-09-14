# Prompt pattern: meta-prompt: applied

## Example 1

**Input**

A colleague says the VPN connects but they cannot reach the staging database. What should they do first?

**Output**

First, verify basic connectivity and routing using these exact commands:
1. Open Command Prompt (Windows) or Terminal (macOS/Linux).
2. Run `ping <staging_db_hostname_or_IP>` to confirm reachability.
3. If the ping fails, run `tracert <staging_db_hostname_or_IP>` (Windows) or `traceroute <staging_db_hostname_or_IP>` (macOS/Linux) to identify where packets drop.
4. Verify DNS resolution with `nslookup <staging_db_hostname>`. Confirm the resolved IP matches your environment’s staging database address.
5. Ensure the VPN client is assigned to the correct network group that has firewall/ACL access to the staging database port (e.g., 1433, 3306, or 5432).

Confirm here before I proceed with any firewall rule modifications, DNS cache flushes, or VPN reconfigurations. If connectivity checks fail or you need internal entitlement/routing adjustments, reply “Open ticket” and I will route this to the network/security team for immediate triage.

_Model: unsloth/Qwen3.6-35B-A3B-MTP-GGUF_
