@echo off
setlocal EnableDelayedExpansion

REM ============================================================================
REM  Titanium Engineering Training - APIM Endpoint Validator (Windows / cmd.exe)
REM  Usage:  validate_apim.cmd <your-apim-subscription-key>
REM
REM  Requires:  curl.exe (ships with Windows 10 build 17063+ and Windows 11)
REM
REM  Note on JSON bodies: cmd.exe does not treat \" as an escaped quote, so a
REM  JSON payload cannot be passed as a `call` argument -- the quote closes
REM  early and every later argument shifts. Each body is therefore written to a
REM  temp file with literal quotes, and only the file path is passed along.
REM ============================================================================

if "%~1"=="" (
    echo Usage: %~nx0 ^<apim-subscription-key^>
    echo   Example: %~nx0 c21c6032fdc04d84b9cebeb21ec69967
    exit /b 1
)

where curl >nul 2>&1
if errorlevel 1 (
    echo ERROR: curl.exe not found on PATH.
    echo curl ships with Windows 10 1803+ and Windows 11. Update Windows or install curl manually.
    exit /b 1
)

set "APIM_KEY=%~1"
set "BASE=https://lgts1tetamapi01.azure-api.net"
set "BODY_FILE=%TEMP%\apim_body_%RANDOM%.json"
set /a PASS=0
set /a FAIL=0
set /a WARN=0

REM Banner - key masking (first 8 + last 4 chars)
set "KEY_HEAD=%APIM_KEY:~0,8%"
set "KEY_TAIL=%APIM_KEY:~-4%"

echo.
echo ==================================================================
echo   Titanium Training - APIM Endpoint Validator
echo ------------------------------------------------------------------
echo   Gateway : %BASE%
echo   Key     : %KEY_HEAD%...%KEY_TAIL%
echo ==================================================================

REM ---- 1. Claude -----------------------------------------------------------
echo.
echo ^>^> 1. Claude - claude-sonnet-4-6  (/claude/anthropic/v1/messages)
> "%BODY_FILE%" echo {"model":"claude-sonnet-4-6","max_tokens":20,"messages":[{"role":"user","content":"Reply with the word VALID only"}]}
call :check "Claude chat" "POST" "%BASE%/claude/anthropic/v1/messages" 200 "content"

REM ---- 2. GPT-5.1 ---------------------------------------------------------
echo.
echo ^>^> 2. GPT-5.1  (/gpt51/openai/responses - Responses API)
> "%BODY_FILE%" echo {"model":"gpt-5.1","input":"Reply with the word VALID only"}
call :check "GPT-5.1" "POST" "%BASE%/gpt51/openai/responses" 200 "output"

REM ---- 3. GPT-5.5 ---------------------------------------------------------
echo.
echo ^>^> 3. GPT-5.5  (/gpt51/openai/responses - Responses API)
> "%BODY_FILE%" echo {"model":"gpt-5.5","input":"Reply with the word VALID only"}
call :check "GPT-5.5" "POST" "%BASE%/gpt51/openai/responses" 200 "output"

REM ---- 4. GPT-5.4-nano ----------------------------------------------------
echo.
echo ^>^> 4. GPT-5.4-nano  (/gpt51/openai/responses - Responses API)
> "%BODY_FILE%" echo {"model":"gpt-5.4-nano","input":"Reply with the word VALID only"}
call :check "GPT-5.4-nano" "POST" "%BASE%/gpt51/openai/responses" 200 "output"

REM ---- 5. Embeddings ------------------------------------------------------
echo.
echo ^>^> 5. Embeddings - text-embedding-3-large  (/openai)
> "%BODY_FILE%" echo {"model":"text-embedding-3-large","input":"Hello"}
call :check "Embeddings" "POST" "%BASE%/openai" 200 "data"

REM ---- 6. GPT-5.1 Chat Completions ---------------------------------------
echo.
echo ^>^> 6. GPT-5.1 Chat Completions  (/gpt51/openai/deployments/gpt-5.1/chat/completions)
> "%BODY_FILE%" echo {"model":"gpt-5.1","messages":[{"role":"user","content":"Reply with the word VALID only"}],"max_completion_tokens":10}
call :check "GPT-5.1 Chat Completions" "POST" "%BASE%/gpt51/openai/deployments/gpt-5.1/chat/completions" 200 "choices"

REM ---- 7. Cohere Rerank ---------------------------------------------------
echo.
echo ^>^> 7. Cohere Rerank 4.0  (/rerank)
> "%BODY_FILE%" echo {"model":"Cohere-rerank-v4.0-pro","query":"What is AI?","documents":["AI is intelligence demonstrated by machines","The sky is blue"],"top_n":1}
call :check "Cohere Rerank" "POST" "%BASE%/rerank" 200 "results"

del "%BODY_FILE%" 2>nul

REM ---- Summary ------------------------------------------------------------
set /a TOTAL=%PASS%+%FAIL%+%WARN%
echo.
echo ========================================
echo   Total: %TOTAL%   %PASS% passed   %WARN% warning   %FAIL% failed
echo ========================================
echo.

if %FAIL% GTR 0 (exit /b 1) else (exit /b 0)


REM ============================================================================
REM  :check  NAME  METHOD  URL  EXPECT_HTTP  SUCCESS_FIELD
REM  Reads the request body from %BODY_FILE%, set by the caller.
REM ============================================================================
:check
setlocal EnableDelayedExpansion
set "NAME=%~1"
set "METHOD=%~2"
set "URL=%~3"
set "EXPECT_HTTP=%~4"
set "SUCCESS_FIELD=%~5"

REM Append subscription key with the correct separator. Compare the URL against
REM itself with '?' stripped -- findstr would read '?' as a regex wildcard and
REM match every line.
set "SEP=?"
if not "!URL!"=="!URL:?=!" set "SEP=&"
set "FULL_URL=!URL!!SEP!subscription-key=!APIM_KEY!"

set "RESP_FILE=%TEMP%\apim_resp_%RANDOM%.txt"

if /i "!METHOD!"=="GET" (
    for /f %%s in ('curl -s -o "!RESP_FILE!" -w "%%{http_code}" "!FULL_URL!"') do set "HTTP_CODE=%%s"
) else (
    for /f %%s in ('curl -s -o "!RESP_FILE!" -w "%%{http_code}" -X POST "!FULL_URL!" -H "Content-Type: application/json" --data-binary "@!BODY_FILE!"') do set "HTTP_CODE=%%s"
)

if "!HTTP_CODE!"=="!EXPECT_HTTP!" (
    if "!SUCCESS_FIELD!"=="" goto :check_pass
    findstr /l /c:"!SUCCESS_FIELD!" "!RESP_FILE!" >nul
    if not errorlevel 1 goto :check_pass
    echo   [WARN] !NAME!  ^(HTTP !HTTP_CODE! but unexpected response body^)
    echo          Response:
    powershell -NoProfile -Command "Get-Content -TotalCount 3 '!RESP_FILE!' | ForEach-Object { $_.Substring(0, [Math]::Min(200, $_.Length)) }" 2>nul
    del "!RESP_FILE!" 2>nul
    endlocal & set /a WARN+=1
    goto :eof
) else (
    echo   [FAIL] !NAME!  ^(expected HTTP !EXPECT_HTTP!, got !HTTP_CODE!^)
    echo          Response:
    powershell -NoProfile -Command "Get-Content -TotalCount 3 '!RESP_FILE!' | ForEach-Object { $_.Substring(0, [Math]::Min(300, $_.Length)) }" 2>nul
    del "!RESP_FILE!" 2>nul
    endlocal & set /a FAIL+=1
    goto :eof
)

:check_pass
echo   [OK]   !NAME!  ^(HTTP !HTTP_CODE!^)
del "!RESP_FILE!" 2>nul
endlocal & set /a PASS+=1
goto :eof
