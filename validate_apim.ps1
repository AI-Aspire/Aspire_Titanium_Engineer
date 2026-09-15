# =============================================================================
# Titanium Engineering Training — APIM Endpoint Validator (Windows / PowerShell)
# Usage:  .\validate_apim.ps1 <your-apim-subscription-key>
#
# If you see "cannot be loaded because running scripts is disabled" run once:
#   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# =============================================================================

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$ApimKey
)

$ErrorActionPreference = 'Stop'
$Base = 'https://lgts1tetamapi01.azure-api.net'

$Pass = 0
$Fail = 0
$Warn = 0

# ─── Helpers ────────────────────────────────────────────────────────────────
function Write-Ok   ($msg) { Write-Host "  [OK]  $msg"   -ForegroundColor Green }
function Write-Bad  ($msg) { Write-Host "  [FAIL] $msg"  -ForegroundColor Red   }
function Write-Warn ($msg) { Write-Host "  [WARN] $msg"  -ForegroundColor Yellow }
function Write-Head ($msg) { Write-Host ""; Write-Host ">> $msg" -ForegroundColor Cyan }

function Invoke-Check {
    param(
        [string]$Name,
        [string]$Method,
        [string]$Url,
        [object]$Body,
        [int]$ExpectHttp,
        [string]$SuccessField = ''
    )

    # Append subscription key with correct separator.
    $sep = if ($Url -like '*`?*') { '&' } else { '?' }
    $FullUrl = "$Url$sep`subscription-key=$ApimKey"

    $bodyJson = if ($Body -is [string]) { $Body } else { ($Body | ConvertTo-Json -Depth 10 -Compress) }

    try {
        if ($Method -eq 'GET') {
            $resp = Invoke-WebRequest -Uri $FullUrl -Method Get -UseBasicParsing -TimeoutSec 30
        } else {
            $resp = Invoke-WebRequest -Uri $FullUrl -Method Post -UseBasicParsing -TimeoutSec 30 `
                -ContentType 'application/json' -Body $bodyJson
        }
        $statusCode = [int]$resp.StatusCode
        $respBody   = $resp.Content
    }
    catch [System.Net.WebException] {
        $statusCode = if ($_.Exception.Response) { [int]$_.Exception.Response.StatusCode } else { 0 }
        $respBody   = try {
            $sr = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
            $sr.ReadToEnd()
        } catch { $_.Exception.Message }
    }
    catch {
        # PowerShell 7 uses Microsoft.PowerShell.Commands.HttpResponseException
        if ($_.Exception.Response) {
            $statusCode = [int]$_.Exception.Response.StatusCode
        } else {
            $statusCode = 0
        }
        $respBody = try {
            $_.ErrorDetails.Message
        } catch { $_.Exception.Message }
    }

    if ($statusCode -eq $ExpectHttp) {
        if ($SuccessField -ne '') {
            if ($respBody -match [regex]::Escape($SuccessField)) {
                Write-Ok "$Name  (HTTP $statusCode)"
                $script:Pass++
            } else {
                Write-Warn "$Name  (HTTP $statusCode but unexpected response body)"
                Write-Host "       Response: $($respBody.Substring(0, [Math]::Min(200, $respBody.Length)))"
                $script:Warn++
            }
        } else {
            Write-Ok "$Name  (HTTP $statusCode)"
            $script:Pass++
        }
    } else {
        Write-Bad "$Name  (expected HTTP $ExpectHttp, got $statusCode)"
        if ($respBody) {
            Write-Host "       Response: $($respBody.Substring(0, [Math]::Min(300, $respBody.Length)))"
        }
        $script:Fail++
    }
}

# ─── Banner ─────────────────────────────────────────────────────────────────
$keyMasked = if ($ApimKey.Length -ge 12) {
    "$($ApimKey.Substring(0,8))...$($ApimKey.Substring($ApimKey.Length-4))"
} else { '(short)' }

Write-Host ''
Write-Host '=================================================================='
Write-Host '  Titanium Training - APIM Endpoint Validator'
Write-Host '------------------------------------------------------------------'
Write-Host "  Gateway : $Base"
Write-Host "  Key     : $keyMasked"
Write-Host '=================================================================='

# ─── 1. Claude ──────────────────────────────────────────────────────────────
Write-Head '1. Claude - claude-sonnet-4-6  (/claude/anthropic/v1/messages)'
Invoke-Check -Name 'Claude chat' `
  -Method POST `
  -Url  "$Base/claude/anthropic/v1/messages" `
  -Body '{"model":"claude-sonnet-4-6","max_tokens":20,"messages":[{"role":"user","content":"Reply with the word VALID only"}]}' `
  -ExpectHttp 200 -SuccessField 'content'

# ─── 2. GPT-5.1 ─────────────────────────────────────────────────────────────
Write-Head '2. GPT-5.1  (/gpt51/openai/responses - Responses API)'
Invoke-Check -Name 'GPT-5.1' `
  -Method POST `
  -Url  "$Base/gpt51/openai/responses" `
  -Body '{"model":"gpt-5.1","input":"Reply with the word VALID only"}' `
  -ExpectHttp 200 -SuccessField 'output'

# ─── 3. GPT-5.5 ─────────────────────────────────────────────────────────────
Write-Head '3. GPT-5.5  (/gpt51/openai/responses - Responses API)'
Invoke-Check -Name 'GPT-5.5' `
  -Method POST `
  -Url  "$Base/gpt51/openai/responses" `
  -Body '{"model":"gpt-5.5","input":"Reply with the word VALID only"}' `
  -ExpectHttp 200 -SuccessField 'output'

# ─── 4. GPT-5.4-nano ────────────────────────────────────────────────────────
Write-Head '4. GPT-5.4-nano  (/gpt51/openai/responses - Responses API)'
Invoke-Check -Name 'GPT-5.4-nano' `
  -Method POST `
  -Url  "$Base/gpt51/openai/responses" `
  -Body '{"model":"gpt-5.4-nano","input":"Reply with the word VALID only"}' `
  -ExpectHttp 200 -SuccessField 'output'

# ─── 5. Embeddings ──────────────────────────────────────────────────────────
Write-Head '5. Embeddings - text-embedding-3-large  (/openai)'
Invoke-Check -Name 'Embeddings' `
  -Method POST `
  -Url  "$Base/openai" `
  -Body '{"model":"text-embedding-3-large","input":"Hello"}' `
  -ExpectHttp 200 -SuccessField 'data'

# ─── 6. GPT-5.1 Chat Completions ───────────────────────────────────────────
Write-Head '6. GPT-5.1 Chat Completions  (/gpt51/openai/deployments/gpt-5.1/chat/completions)'
Invoke-Check -Name 'GPT-5.1 Chat Completions' `
  -Method POST `
  -Url  "$Base/gpt51/openai/deployments/gpt-5.1/chat/completions" `
  -Body '{"model":"gpt-5.1","messages":[{"role":"user","content":"Reply with the word VALID only"}],"max_completion_tokens":10}' `
  -ExpectHttp 200 -SuccessField 'choices'

# ─── 7. Cohere Rerank ──────────────────────────────────────────────────────
Write-Head '7. Cohere Rerank 4.0  (/rerank)'
Invoke-Check -Name 'Cohere Rerank' `
  -Method POST `
  -Url  "$Base/rerank" `
  -Body '{"model":"Cohere-rerank-v4.0-pro","query":"What is AI?","documents":["AI is intelligence demonstrated by machines","The sky is blue"],"top_n":1}' `
  -ExpectHttp 200 -SuccessField 'results'

# ─── Summary ────────────────────────────────────────────────────────────────
$total = $Pass + $Fail + $Warn
Write-Host ''
Write-Host '========================================'
Write-Host -NoNewline "  Total: $total   "
Write-Host -NoNewline "$Pass passed   " -ForegroundColor Green
if ($Warn -gt 0) { Write-Host -NoNewline "$Warn warning   " -ForegroundColor Yellow }
if ($Fail -gt 0) { Write-Host -NoNewline "$Fail failed"      -ForegroundColor Red    }
Write-Host ''
Write-Host '========================================'
Write-Host ''

if ($Fail -gt 0) { exit 1 } else { exit 0 }
