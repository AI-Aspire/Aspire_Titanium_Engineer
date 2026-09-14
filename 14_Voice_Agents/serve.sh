#!/usr/bin/env bash
# Launch the voice research panel over HTTPS via Tailscale Serve.
#
# Why HTTPS: browsers only allow microphone access (getUserMedia / hold-to-talk) in a
# "secure context": localhost OR https. Over plain http://<ip>:8000 from a phone or
# another device the mic is silently blocked. Tailscale Serve fronts the app with a
# valid cert on your tailnet, so the mic works from any device.
#
#   ./serve.sh            # then open the printed https URL on any tailnet device
set -euo pipefail
cd "$(dirname "$0")"
PORT="${PORT:-8000}"
UVICORN_PID=""

cleanup() {
  echo
  echo "shutting down (app + HTTPS proxy)"
  tailscale serve reset 2>/dev/null || true
  [[ -n "$UVICORN_PID" ]] && kill "$UVICORN_PID" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

echo "starting the app on :$PORT"
uv run uvicorn web.server:app --host 127.0.0.1 --port "$PORT" &
UVICORN_PID=$!

for _ in $(seq 1 90); do
  curl -sf "http://127.0.0.1:$PORT/api/status" >/dev/null 2>&1 && break
  sleep 1
done

echo "putting it behind HTTPS via Tailscale Serve"
tailscale serve --bg "$PORT" >/dev/null
URL=$(tailscale serve status 2>/dev/null | grep -oE 'https://[^ ]+' | head -1)

echo
echo "  Open on any device in your tailnet:  ${URL:-check: tailscale serve status}"
echo "  HTTPS means the microphone / hold-to-talk works. Ctrl-C to stop everything."
echo
wait "$UVICORN_PID"
