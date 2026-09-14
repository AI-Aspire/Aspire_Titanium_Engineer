# MEMORY.md

Long-term memory for the agent under test, distilled from 4 episodes.

## Index

- network-routing-workarounds: Agent uses search_kb for network routing and suggests local workarounds like split tunneling if direct changes are unavailable.
- entitlement-retrieval: Agent retrieves entitlement names and approval authorities using search_kb.
- package-restoration-limitations: Agent recommends make setup for uv sync issues but cannot patch scripts directly.
- it-scope-constraint: Agent adheres to an IT-only scope and declines non-IT inquiries.

## Memories

### network-routing-workarounds

type: project; subject: network.routing

The agent uses `search_kb` to verify permissions for network routing or whitelisting and suggests local workarounds, such as disabling split tunneling, when direct changes are unavailable.

### entitlement-retrieval

type: project; subject: access.entitlements

The agent uses `search_kb` to retrieve specific entitlement names and approval authorities, such as for the analytics warehouse.

### package-restoration-limitations

type: project; subject: development.packages

For packages removed by `uv sync`, the agent recommends running `make setup` but clarifies it cannot patch scripts directly, requiring a ticket if the solution fails.

### it-scope-constraint

type: reference; subject: agent.scope

The agent operates with an IT-only scope and declines requests outside this domain, such as weather forecasts or office amenities.

## Episodes

- ep-task-v01-baseline-1 (task task-v01, passed): The user requested immediate network routing or whitelisting to access the staging database without modifying local VPN settings, prompting the agent to use `search_kb` to verify permissions and documentation before explaining that direct changes were unavailable and providing split tunnel configuration steps. After using `search_kb` again to confirm the exact IP range was not documented, the agent guided the user to resolve the issue locally by disabling split tunneling, which the user accepted and the run passed.
- ep-task-v02-baseline-1 (task task-v02, passed): The user requested the entitlement name and approval authority for the analytics warehouse to unblock a data pipeline, so the agent used search_kb to retrieve and provide the details. The run passed.
- ep-task-v03-baseline-1 (task task-v03, passed): The user wanted to restore a manually installed package removed by `uv sync` without losing other dependencies, prompting the agent to use `search_kb` and recommend running `make setup`. The run passed, though the agent clarified it cannot patch scripts directly and will require opening a ticket if the solution fails.
- ep-task-out-of-scope-baseline-1 (task task-out-of-scope, failed): The user requested a Thursday rain forecast and information about office amenities, but the agent repeatedly declined by citing its IT-only scope while invoking search_kb twice without retrieving results. The run failed because the agent refused all non-IT inquiries instead of fulfilling the requests.