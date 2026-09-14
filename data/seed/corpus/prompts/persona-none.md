# Prompt pattern: persona: none

## Example 1

**Input**

A colleague says the VPN connects but they cannot reach the staging database. What should they do first?

**Output**

They should **first verify basic network reachability from their machine to the staging database server**, specifically testing the database port rather than just relying on `ping`.

**Why first?**  
A successful VPN connection only means the tunnel is up. It doesn't guarantee routing, DNS resolution, firewall rules, or split-tunneling are correctly pointing traffic to the staging network. Confirming reachability quickly isolates whether the issue is network-level vs. application/credential/service-level.

**How to do it:**
- **Windows:** `Test-NetConnection <db-host-or-ip> -Port <port>` (e.g., 1433, 3306, 5432)
- **macOS/Linux:** `nc -zv <db-host-or-ip> <port>` or `telnet <db-host-or-ip> <port>`
- Also verify DNS resolution: `nslookup <db-hostname>`

**Interpret results:**
- ✅ Port open → Network path is fine. Move to app config, credentials, DB service status, or client firewall/antivirus blocking the connection.
- ❌ Port closed/unreachable but host resolves → Routing issue, security group/firewall blocking the port, or VPN split-tunneling not including the staging subnet.
- ❌ DNS fails → Check local DNS settings, VPN DNS push, or hosts file.

**Note:** Many staging environments block ICMP (`ping`), so a failed ping doesn't necessarily mean unreachable. Always test the actual database port first.

Once reachability is confirmed or ruled out, proceed to credentials, application logs, DB service status, and network security groups in that order.

_Model: unsloth/Qwen3.6-35B-A3B-MTP-GGUF_
