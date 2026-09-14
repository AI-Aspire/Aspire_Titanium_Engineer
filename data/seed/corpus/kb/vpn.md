# VPN

## Connecting

Install the VPN client from the software centre. Sign in with your company
account. The client shows a green shield when connected.

## Split tunnelling

By default only company networks route through the VPN. Staging and the
analytics warehouse are on the private range, so they need the VPN connected.
If the shield is green and staging still times out, open the client, choose
Settings, then Routing, and confirm "Route private ranges" is on. Restart the
client after changing it.

## Known issues

- On hotel wifi the client sometimes connects but passes no traffic. Toggle
  wifi off and on, then reconnect.
- Two VPN clients installed at once will fight. Remove the old one.

## When to file a ticket

If you have restarted the client and the routing setting is on and staging is
still unreachable, file a ticket with the output of `ping staging-db.internal`.
