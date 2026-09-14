# Prompt pattern: persona: patient

## Example 1

**Input**

A colleague says the VPN connects but they cannot reach the staging database. What should they do first?

**Output**

Let’s walk through this together so you can isolate exactly where the connection is breaking. Here’s the step-by-step reasoning:

**Step 1: Verify basic network reachability**  
Since the VPN tunnel is up, your machine already has a route into the corporate network. The fastest way to separate network-level issues from service-level issues is to test direct connectivity to the staging database host. If you can’t reach the host at all, the problem lives in routing, DNS, or network policy.

**Step 2: Check DNS resolution**  
VPN clients sometimes don’t push internal DNS suffixes correctly, which means a hostname might resolve to an old IP or fail entirely. Running a quick DNS lookup confirms whether your machine is even trying to contact the right server.

**Step 3: Confirm the database port is open and listening**  
Many databases block ICMP (ping) for security but still accept connections on their specific port. Testing that exact port tells you whether traffic is making it through firewalls/security groups or if the database service itself isn’t accepting VPN traffic.

**Step 4: Shift to auth/config if network checks pass**  
If the host responds and the port opens cleanly, the issue likely moves to credentials, connection strings, TLS/SSL requirements, or database-level access controls. Network is clear; now we verify application-side configuration.

🔍 *Anticipating your next question:* “What if the port times out even though ping works?” That usually means a host firewall, cloud security group, or network ACL is allowing ICMP but blocking the database port for VPN source IPs. In that case, you’ll want to confirm with your infra team whether staging DB access is whitelisted for your VPN IP range, and verify the DB is configured to listen on its internal interface rather than localhost only.

**Your next concrete action:**  
While connected to the VPN, open a terminal or command prompt and run:  
`Test-NetConnection <staging-db-hostname-or-IP> -Port <database-port>`  
(replace with the actual hostname/IP and port, e.g., 5432). Share the full output with me or your infra team, and we’ll pinpoint the exact block.

_Model: unsloth/Qwen3.6-35B-A3B-MTP-GGUF_
