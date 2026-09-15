#!/bin/bash
# =============================================================================
# Titanium Engineering Training — APIM Endpoint Validator
# Usage: ./validate_apim.sh <your-apim-subscription-key>
# =============================================================================

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <apim-subscription-key>"
  echo "  Example: $0 c21c6032fdc04d84b9cebeb21ec69967"
  exit 1
fi

APIM_KEY="$1"
BASE="https://lgts1tetamapi01.azure-api.net"

PASS=0
FAIL=0
WARN=0

# ─── HELPERS ─────────────────────────────────────────────────────────────────
green()  { echo -e "\033[1;32m  ✓ $*\033[0m"; }
red()    { echo -e "\033[1;31m  ✗ $*\033[0m"; }
yellow() { echo -e "\033[1;33m  ⚠ $*\033[0m"; }
header() { echo -e "\n\033[1;36m▶  $*\033[0m"; }

check() {
  local NAME="$1"
  local METHOD="$2"
  local URL="$3"
  local BODY="$4"
  local EXPECT_HTTP="$5"
  local SUCCESS_FIELD="${6:-}"

  local RESPONSE HTTP_CODE

  # Append key with ? or & depending on whether URL already has query params
  local SEP="?"
  [[ "$URL" == *"?"* ]] && SEP="&"

  if [[ "$METHOD" == "GET" ]]; then
    RESPONSE=$(curl -s -w "\n__HTTP__%{http_code}" "${URL}${SEP}subscription-key=${APIM_KEY}")
  else
    RESPONSE=$(curl -s -w "\n__HTTP__%{http_code}" -X POST "${URL}${SEP}subscription-key=${APIM_KEY}" \
      -H "Content-Type: application/json" \
      -d "$BODY")
  fi

  HTTP_CODE=$(echo "$RESPONSE" | grep "__HTTP__" | sed 's/__HTTP__//')
  BODY_RESP=$(echo "$RESPONSE" | grep -v "__HTTP__")

  if [[ "$HTTP_CODE" == "$EXPECT_HTTP" ]]; then
    if [[ -n "$SUCCESS_FIELD" ]]; then
      if echo "$BODY_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); exit(0 if '${SUCCESS_FIELD}' in str(d) else 1)" 2>/dev/null; then
        green "$NAME  (HTTP $HTTP_CODE)"
        PASS=$((PASS+1))
      else
        yellow "$NAME  (HTTP $HTTP_CODE but unexpected response body)"
        echo "     Response: $(echo "$BODY_RESP" | head -c 200)"
        WARN=$((WARN+1))
      fi
    else
      green "$NAME  (HTTP $HTTP_CODE)"
      PASS=$((PASS+1))
    fi
  else
    red "$NAME  (expected HTTP $EXPECT_HTTP, got $HTTP_CODE)"
    echo "     Response: $(echo "$BODY_RESP" | head -c 300)"
    FAIL=$((FAIL+1))
  fi
}

# ─── BANNER ──────────────────────────────────────────────────────────────────
echo ""
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║   Titanium Training — APIM Endpoint Validator                    ║"
echo "╠══════════════════════════════════════════════════════════════════╣"
printf "║   Gateway : %-52s║\n" "$BASE"
printf "║   Key     : %-52s║\n" "${APIM_KEY:0:8}…${APIM_KEY: -4}"
echo "╚══════════════════════════════════════════════════════════════════╝"

# ─── 1. CLAUDE ───────────────────────────────────────────────────────────────
header "1. Claude — claude-sonnet-4-6  (/claude/anthropic/v1/messages)"
check "Claude chat" \
  "POST" \
  "${BASE}/claude/anthropic/v1/messages" \
  '{"model":"claude-sonnet-4-6","max_tokens":20,"messages":[{"role":"user","content":"Reply with the word VALID only"}]}' \
  "200" \
  "content"

# ─── 2. GPT-5.1 ──────────────────────────────────────────────────────────────
header "2. GPT-5.1  (/gpt51/openai/responses — Responses API)"
check "GPT-5.1" \
  "POST" \
  "${BASE}/gpt51/openai/responses" \
  '{"model":"gpt-5.1","input":"Reply with the word VALID only"}' \
  "200" \
  "output"

# ─── 3. GPT-5.5 ──────────────────────────────────────────────────────────────
header "3. GPT-5.5  (/gpt51/openai/responses — Responses API)"
check "GPT-5.5" \
  "POST" \
  "${BASE}/gpt51/openai/responses" \
  '{"model":"gpt-5.5","input":"Reply with the word VALID only"}' \
  "200" \
  "output"

# ─── 4. GPT-5.4-nano ─────────────────────────────────────────────────────────
header "4. GPT-5.4-nano  (/gpt51/openai/responses — Responses API)"
check "GPT-5.4-nano" \
  "POST" \
  "${BASE}/gpt51/openai/responses" \
  '{"model":"gpt-5.4-nano","input":"Reply with the word VALID only"}' \
  "200" \
  "output"

# ─── 5. EMBEDDINGS ───────────────────────────────────────────────────────────
header "5. Embeddings — text-embedding-3-large  (/openai)"
check "Embeddings" \
  "POST" \
  "${BASE}/openai" \
  '{"model":"text-embedding-3-large","input":"Hello"}' \
  "200" \
  "data"

# ─── 6. GPT-5.1 CHAT COMPLETIONS ────────────────────────────────────────────
header "6. GPT-5.1 Chat Completions  (/gpt51/openai/deployments/gpt-5.1/chat/completions)"
check "GPT-5.1 Chat Completions" \
  "POST" \
  "${BASE}/gpt51/openai/deployments/gpt-5.1/chat/completions" \
  '{"model":"gpt-5.1","messages":[{"role":"user","content":"Reply with the word VALID only"}],"max_completion_tokens":10}' \
  "200" \
  "choices"

# ─── 7. COHERE RERANK ────────────────────────────────────────────────────────
header "7. Cohere Rerank 4.0  (/rerank)"
check "Cohere Rerank" \
  "POST" \
  "${BASE}/rerank" \
  '{"model":"Cohere-rerank-v4.0-pro","query":"What is AI?","documents":["AI is intelligence demonstrated by machines","The sky is blue"],"top_n":1}' \
  "200" \
  "results"

# ─── SUMMARY ─────────────────────────────────────────────────────────────────
echo ""
echo "════════════════════════════════════════"
TOTAL=$((PASS+FAIL+WARN))
printf "  Total: %d   " "$TOTAL"
printf "\033[1;32m✓ %d passed\033[0m   " "$PASS"
[[ $WARN -gt 0 ]] && printf "\033[1;33m⚠ %d warning\033[0m   " "$WARN"
[[ $FAIL -gt 0 ]] && printf "\033[1;31m✗ %d failed\033[0m" "$FAIL"
echo ""
echo "════════════════════════════════════════"
echo ""

[[ $FAIL -gt 0 ]] && exit 1 || exit 0
