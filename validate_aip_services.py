#!/usr/bin/env python3
"""Validate the AIP shared services that do NOT go through the APIM gateway.

    python3 validate_aip_services.py
    python3 validate_aip_services.py --only speech,postgres
    python3 validate_aip_services.py --verbose

These five services are reached directly, each with its own credential, and all
of them are network-restricted: connect the Accenture VPN (LLM COE HUB) first.

    Azure AI Speech          lgts1tetamsph01   shared Cognitive Services key
    Azure AI Content Safety  lgts1tetamacs01   shared Cognitive Services key
    Azure AI Search          lgts1tetamais01   service principal, or admin key
    Blob Storage             lgts1tetamstg01   connection string
    PostgreSQL + pgvector    lgts1tetamdb01    password, TCP only

Everything that goes through the gateway -- Claude, GPT, embeddings, Cohere
rerank -- is covered by validate_apim.sh instead. This script is its companion.

Credentials are read from the environment, or from a .env file beside this
script (or in the current directory). Nothing is hard-coded: get the values
from SharePoint "Env Files (Local & AIP)" or the AIP Provisioning Tracker.

Exit status is 0 when nothing failed (skips are fine), 1 when any check failed.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import re
import shutil
import socket
import ssl
import struct
import subprocess
import sys
import urllib.error
import urllib.request
from email.utils import formatdate
from pathlib import Path

TIMEOUT = 15

# ── console: make Unicode and colour safe on Windows ──────────────────────────


def _init_console() -> None:
    """A Windows console defaults to cp1252/cp437, which cannot encode the box
    drawing or tick glyphs, and legacy cmd.exe prints ANSI escapes literally."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError, ValueError):
            pass
    if os.name == "nt":
        try:  # ask the console for VT processing so colours render
            import ctypes

            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:  # noqa: BLE001  cosmetic only
            pass


def _encodable(text: str) -> bool:
    enc = getattr(sys.stdout, "encoding", None) or "ascii"
    try:
        text.encode(enc)
        return True
    except (LookupError, UnicodeEncodeError):
        return False


_init_console()

_TTY = sys.stdout.isatty()
_UNICODE = _encodable("✓─═║╔╗╚╝╠╣")


def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _TTY else text


OK, FAIL, SKIP = "ok", "fail", "skip"
MARK = ({OK: "✓", FAIL: "✗", SKIP: "–"} if _UNICODE
        else {OK: "PASS", FAIL: "FAIL", SKIP: "SKIP"})
COLOUR = {OK: "1;32", FAIL: "1;31", SKIP: "1;33"}
BOX = ("╔╗╚╝╠╣═║" if _UNICODE else "++++++-|")
HRULE = "─" if _UNICODE else "-"


def tool(name: str) -> str | None:
    """Resolve an external command to a full path.

    `shutil.which` honours PATHEXT, so this finds `az.cmd` on Windows. Passing
    the bare name to subprocess would raise FileNotFoundError there, because
    CreateProcess does not resolve batch-file extensions.
    """
    return shutil.which(name)


class Results:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []

    def add(self, status: str, name: str, detail: str = "") -> None:
        self.rows.append((status, name, detail))
        print(f"  {_c(COLOUR[status], MARK[status])} {name:<34} {detail}")

    def count(self, status: str) -> int:
        return sum(1 for s, _, _ in self.rows if s == status)


# ── env loading ───────────────────────────────────────────────────────────────


def load_env() -> None:
    """Merge a .env into os.environ without overriding real env vars.

    Handles the ${VAR} interpolation the AIP templates use, so SPEECH_KEY set
    once is picked up by STT_API_KEY=${SPEECH_KEY}.
    """
    for base in (Path(__file__).resolve().parent, Path.cwd()):
        path = base / ".env"
        if not path.is_file():
            continue
        raw: dict[str, str] = {}
        for line in path.read_text(errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key, val = key.strip(), val.strip().strip('"').strip("'")
            if key.isidentifier():
                raw[key] = val
        for key, val in raw.items():
            expanded = re.sub(
                r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}",
                lambda m: raw.get(m.group(1), os.environ.get(m.group(1), "")),
                val,
            )
            os.environ.setdefault(key, expanded)
        return


def env(*names: str) -> str:
    """First non-empty, non-placeholder value among `names`."""
    for n in names:
        v = (os.environ.get(n) or "").strip()
        if v and not (v.startswith("<") and v.endswith(">")):
            return v
    return ""


def host_of(url: str) -> str:
    return re.sub(r"^https?://", "", url).split("/")[0].split(":")[0]


# ── shared HTTP helper ────────────────────────────────────────────────────────


def request(
    url: str,
    *,
    method: str = "GET",
    headers: dict[str, str] | None = None,
    body: bytes | None = None,
) -> tuple[int, bytes, str]:
    """Return (status, body, error). status 0 means the call never completed."""
    req = urllib.request.Request(url, data=body, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read(), ""
    except urllib.error.HTTPError as e:
        return e.code, e.read(), ""
    except urllib.error.URLError as e:
        # URLError wraps the real cause; a TLS trust failure needs a different
        # fix from an unreachable host, so separate the two.
        reason = e.reason
        if isinstance(reason, ssl.SSLCertVerificationError):
            return 0, b"", "TLS_VERIFY"
        if isinstance(reason, ssl.SSLError):
            return 0, b"", f"TLS error: {reason}"
        if isinstance(reason, socket.gaierror):
            return 0, b"", f"{host_of(url)} did not resolve"
        if isinstance(reason, (TimeoutError, socket.timeout)):
            return 0, b"", "timed out — VPN connected?"
        return 0, b"", str(reason)
    except (TimeoutError, socket.timeout):
        return 0, b"", "timed out — VPN connected?"
    except ssl.SSLError as e:
        return 0, b"", f"TLS error: {e}"
    except OSError as e:
        return 0, b"", str(e.strerror or e)


def trust_store_empty() -> bool:
    """True when this Python has no CA certificates at all.

    A python.org build on macOS ships without a usable trust store until
    "Install Certificates.command" is run, so every HTTPS call fails
    verification while curl in the same shell succeeds. That is a different
    problem from a proxy re-signing traffic, and has a different fix.
    """
    try:
        return not ssl.create_default_context().get_ca_certs()
    except Exception:  # noqa: BLE001  never let diagnostics break the run
        return False


def unreachable(err: str) -> str:
    if err != "TLS_VERIFY":
        return f"unreachable — {err}"
    if trust_store_empty():
        return "TLS failed — this Python has no CA certificates (see note below)"
    return ("TLS certificate not trusted — a proxy is re-signing traffic. "
            "Point SSL_CERT_FILE at your corporate CA bundle.")


def trust_store_advice() -> str:
    return "\n".join([
        "  This Python has an empty certificate store, so every HTTPS check above",
        "  failed verification even though the network is fine. Fix it once:",
        "",
        "    macOS, python.org build:",
        '      open "/Applications/Python 3.12/Install Certificates.command"',
        "",
        "    any platform:",
        "      python3 -m pip install --upgrade certifi",
        '      export SSL_CERT_FILE="$(python3 -m certifi)"',
        "",
        "  Or just run this with the repo's uv-managed Python, which ships certs:",
        "      uv run --no-sync python validate_aip_services.py",
    ])


def azure_error(payload: bytes) -> str:
    """Pull a useful message out of an Azure error body."""
    text = payload.decode(errors="replace").strip()
    try:
        data = json.loads(text)
        err = data.get("error", data)
        if isinstance(err, dict):
            return str(err.get("code") or err.get("message") or err)[:140]
    except (ValueError, AttributeError):
        pass
    m = re.search(r"<Code>(.*?)</Code>", text)
    if m:
        return m.group(1)
    return text[:140].replace("\n", " ") or "no detail"


# ── 1. Azure AI Speech ────────────────────────────────────────────────────────


def check_speech(r: Results, verbose: bool) -> None:
    name = "Azure AI Speech"
    endpoint = env("STT_BASE_URL", "TTS_BASE_URL", "SPEECH_ENDPOINT").rstrip("/")
    key = env("SPEECH_KEY", "STT_API_KEY", "TTS_API_KEY", "SPEECH_API_KEY")
    if not endpoint:
        endpoint = "https://lgts1tetamsph01.cognitiveservices.azure.com"
    if not key:
        r.add(SKIP, name, "SPEECH_KEY not set")
        return

    # Listing the base models proves the key works and the resource is reachable.
    # Note: /sts/v1.0/issueToken is NOT usable here -- Azure disables the Token
    # API on a resource with a virtual-network or firewall rule, which every AIP
    # Speech resource has, so it returns 400 regardless of the key.
    url = f"{endpoint}/speechtotext/v3.2/models/base"
    status, payload, err = request(url, headers={"Ocp-Apim-Subscription-Key": key})
    if status == 200:
        try:
            n = len(json.loads(payload).get("values", []))
            detail = f"{n} base model(s) listed"
        except ValueError:
            detail = "reachable, key accepted"
        r.add(OK, name, detail)
    elif status in (401, 403):
        r.add(FAIL, name, f"HTTP {status} — key rejected, or VPN not connected")
    elif status:
        r.add(FAIL, name, f"HTTP {status} — {azure_error(payload)}")
    else:
        r.add(FAIL, name, unreachable(err))
    if verbose and status:
        print(f"      {url} -> {status}")


# ── 2. Azure AI Content Safety ────────────────────────────────────────────────


def check_content_safety(r: Results, verbose: bool) -> None:
    name = "Azure AI Content Safety"
    endpoint = env("CONTENT_SAFETY_BASE_URL", "CONTENT_SAFETY_ENDPOINT").rstrip("/")
    key = env("CONTENT_SAFETY_API_KEY", "CONTENT_SAFETY_KEY", "CS_KEY")
    if not endpoint:
        endpoint = "https://lgts1tetamacs01.cognitiveservices.azure.com"
    if not key:
        r.add(SKIP, name, "CONTENT_SAFETY_API_KEY not set")
        return

    api_version = env("CONTENT_SAFETY_API_VERSION") or "2023-10-01"
    url = f"{endpoint}/contentsafety/text:analyze?api-version={api_version}"
    status, payload, err = request(
        url,
        method="POST",
        headers={"Ocp-Apim-Subscription-Key": key, "Content-Type": "application/json"},
        body=json.dumps({"text": "Hello world"}).encode(),
    )
    if status == 200:
        try:
            cats = json.loads(payload).get("categoriesAnalysis", [])
            detail = f"{len(cats)} categories analysed"
        except ValueError:
            detail = "analysed"
        r.add(OK, name, detail)
    elif status in (401, 403):
        r.add(FAIL, name, f"HTTP {status} — key rejected, or VPN not connected")
    elif status:
        r.add(FAIL, name, f"HTTP {status} — {azure_error(payload)}")
    else:
        r.add(FAIL, name, unreachable(err))
    if verbose and status:
        print(f"      {url} -> {status}")


# ── 3. Azure AI Search ────────────────────────────────────────────────────────


def az_token(scope: str) -> str:
    """Bearer token via the Azure CLI, when it is installed and signed in."""
    az = tool("az")
    if not az:
        return ""
    try:
        out = subprocess.run(
            [az, "account", "get-access-token", "--scope", scope,
             "--query", "accessToken", "-o", "tsv"],
            capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired):
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


def check_search(r: Results, verbose: bool) -> None:
    name = "Azure AI Search"
    endpoint = env("AZURE_SEARCH_ENDPOINT", "SEARCH_URL").rstrip("/")
    if not endpoint:
        endpoint = "https://lgts1tetamais01.search.windows.net"
    api_version = env("AZURE_SEARCH_API_VERSION") or "2024-07-01"
    url = f"{endpoint}/indexes?api-version={api_version}&$select=name"

    # Azure AD first: the AIP search service sets disableLocalAuth=true, so its
    # admin keys can be fetched but are always rejected. Fall back to an api-key
    # anyway, in case a future service has local auth enabled.
    key = env("AZURE_SEARCH_API_KEY", "SEARCH_API_KEY", "AZURE_SEARCH_ADMIN_KEY")
    attempts: list[tuple[str, dict[str, str]]] = []
    token = az_token("https://search.azure.com/.default")
    if token:
        attempts.append(("Entra ID token", {"Authorization": f"Bearer {token}"}))
    if key:
        attempts.append(("admin key", {"api-key": key}))

    if not attempts:
        r.add(SKIP, name, "az CLI not signed in, and no AZURE_SEARCH_API_KEY")
        return

    status = 0
    for how, headers in attempts:
        status, payload, err = request(url, headers=headers)
        if verbose and status:
            print(f"      {url} -> {status} ({how})")
        if status == 200:
            try:
                n = len(json.loads(payload).get("value", []))
                detail = f"{n} index(es) listed via {how}"
            except ValueError:
                detail = f"reachable via {how}"
            r.add(OK, name, detail)
            return
        if status in (401, 403) and how == "admin key":
            r.add(FAIL, name,
                  "401/403 on the admin key — this service has local auth "
                  "disabled; use a service principal")
            return
        if status not in (401, 403):
            break

    if status in (401, 403):
        r.add(FAIL, name, f"HTTP {status} — sign in with `az login`, or grant "
                          "your principal the Search Index Data Reader role")
    elif status:
        r.add(FAIL, name, f"HTTP {status} — {azure_error(payload)}")
    else:
        r.add(FAIL, name, unreachable(err))


# ── 4. Blob Storage ───────────────────────────────────────────────────────────


def parse_conn_str(conn: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for part in conn.split(";"):
        k, _, v = part.partition("=")
        if k.strip():
            out[k.strip()] = v.strip()
    return out


def check_blob(r: Results, verbose: bool) -> None:
    name = "Blob Storage"
    conn = env("AZURE_STORAGE_CONNECTION_STRING", "BLOB_CONNECTION_STRING")
    account = env("AZURE_STORAGE_ACCOUNT")
    key_b64 = env("AZURE_STORAGE_KEY")

    if conn:
        parts = parse_conn_str(conn)
        account = parts.get("AccountName", account)
        # AccountKey is base64 and contains '=' padding, so recover it verbatim.
        m = re.search(r"AccountKey=([^;]+)", conn)
        key_b64 = m.group(1) if m else key_b64
    if not (account and key_b64):
        r.add(SKIP, name, "AZURE_STORAGE_CONNECTION_STRING not set")
        return

    try:
        secret = base64.b64decode(key_b64)
    except Exception:
        r.add(FAIL, name, "AccountKey is not valid base64")
        return

    # Shared Key (blob) signing -- avoids needing the azure-storage-blob package.
    version = "2021-08-06"
    date = formatdate(timeval=None, localtime=False, usegmt=True)
    canon_headers = f"x-ms-date:{date}\nx-ms-version:{version}\n"
    canon_resource = f"/{account}/\ncomp:list"
    fields = ["GET"] + [""] * 11          # VERB then 11 conditional/content headers
    string_to_sign = "\n".join(fields) + "\n" + canon_headers + canon_resource
    signature = base64.b64encode(
        hmac.new(secret, string_to_sign.encode("utf-8"), hashlib.sha256).digest()
    ).decode()

    url = f"https://{account}.blob.core.windows.net/?comp=list"
    status, payload, err = request(
        url,
        headers={
            "x-ms-date": date,
            "x-ms-version": version,
            "Authorization": f"SharedKey {account}:{signature}",
        },
    )
    if status == 200:
        n = len(re.findall(r"<Container>", payload.decode(errors="replace")))
        r.add(OK, name, f"{n} container(s) listed on {account}")
    elif status == 403 and "AuthenticationFailed" in payload.decode(errors="replace"):
        # The request was well-formed and signed; Azure simply computed a
        # different signature, which means the AccountKey is wrong or rotated.
        r.add(FAIL, name, "403 AuthenticationFailed — AccountKey wrong or rotated")
        print("      cross-check with the Azure CLI, which signs independently:")
        print(f"      az storage container list --account-name {account} "
              "--account-key <key> -o tsv")
    elif status == 403:
        r.add(FAIL, name, f"HTTP 403 — {azure_error(payload)}")
    elif status:
        r.add(FAIL, name, f"HTTP {status} — {azure_error(payload)}")
    else:
        r.add(FAIL, name, unreachable(err))
    if verbose and status:
        print(f"      {url} -> {status}")


# ── 5. PostgreSQL + pgvector ──────────────────────────────────────────────────


def check_postgres(r: Results, verbose: bool) -> None:
    name = "PostgreSQL (reachable)"
    host = env("POSTGRES_HOST", "PGHOST")
    if not host:
        conn = env("POSTGRES_CONNECTION_STRING")
        m = re.search(r"host=([^\s;]+)", conn)
        host = m.group(1) if m else "c-lgts1tetamdb01.qj62zfkoqkr3nu.postgres.cosmos.azure.com"
    port = int(env("POSTGRES_PORT", "PGPORT") or 5432)

    # A TCP connect plus the Postgres SSLRequest handshake proves the host is
    # reachable, is really Postgres, and accepts TLS -- no credentials needed.
    # This is the check that fails when the VPN is down, which is the common case.
    try:
        with socket.create_connection((host, port), timeout=TIMEOUT) as s:
            s.sendall(struct.pack("!ii", 8, 80877103))
            reply = s.recv(1)
        if reply == b"S":
            r.add(OK, name, f"{host}:{port} — TLS accepted")
        elif reply == b"N":
            r.add(OK, name, f"{host}:{port} — reachable, TLS refused")
        else:
            r.add(FAIL, name, f"{host}:{port} — unexpected reply {reply!r}")
            return
    except socket.gaierror as e:
        r.add(FAIL, name, f"{host} did not resolve — {e.strerror or e}")
        return
    except (TimeoutError, socket.timeout):
        r.add(FAIL, name, f"{host}:{port} timed out — VPN connected?")
        return
    except OSError as e:
        r.add(FAIL, name, f"{host}:{port} — {e.strerror or e}")
        return

    # Full auth and the pgvector check need a real client.
    password = env("POSTGRES_PASSWORD", "PGPASSWORD")
    user = env("POSTGRES_USER", "PGUSER") or "citus"
    db = env("POSTGRES_DB", "PGDATABASE") or "titaniumdb"
    if not password:
        r.add(SKIP, "PostgreSQL (pgvector)", "POSTGRES_PASSWORD not set")
        return

    psql = tool("psql")
    if not psql:
        r.add(SKIP, "PostgreSQL (pgvector)",
              "psql not installed — reachability confirmed above")
        return

    sql = "SELECT extname FROM pg_extension WHERE extname = 'vector';"
    try:
        out = subprocess.run(
            [psql, "--no-psqlrc", "-tAX", "-h", host, "-p", str(port),
             "-U", user, "-d", db, "-c", sql],
            capture_output=True, text=True, timeout=45,
            env={**os.environ, "PGPASSWORD": password, "PGSSLMODE": "require"},
        )
    except OSError:
        r.add(SKIP, "PostgreSQL (pgvector)",
              "psql could not be run — reachability confirmed above")
        return
    except subprocess.TimeoutExpired:
        r.add(FAIL, "PostgreSQL (pgvector)", "psql timed out")
        return

    if out.returncode != 0:
        r.add(FAIL, "PostgreSQL (pgvector)",
              (out.stderr.strip().splitlines() or ["psql failed"])[-1][:120])
    elif "vector" in out.stdout:
        r.add(OK, "PostgreSQL (pgvector)", f"connected to {db}, pgvector present")
    else:
        r.add(FAIL, "PostgreSQL (pgvector)",
              f"connected to {db}, but the vector extension is missing")


# ── main ──────────────────────────────────────────────────────────────────────

CHECKS = {
    "speech": check_speech,
    "contentsafety": check_content_safety,
    "search": check_search,
    "blob": check_blob,
    "postgres": check_postgres,
}


def main(argv: list[str]) -> int:
    global TIMEOUT

    ap = argparse.ArgumentParser(
        description="Validate the AIP services that bypass the APIM gateway.")
    ap.add_argument("--only", default="",
                    help="comma-separated subset: " + ", ".join(CHECKS))
    ap.add_argument("--verbose", action="store_true", help="show URLs and status codes")
    ap.add_argument("--timeout", type=float, default=None,
                    help=f"seconds per call (default {TIMEOUT})")
    args = ap.parse_args(argv)

    if args.timeout:
        TIMEOUT = args.timeout

    load_env()

    wanted = list(CHECKS)
    if args.only:
        wanted = [w.strip().lower().replace("_", "").replace("-", "")
                  for w in args.only.split(",")]
        unknown = [w for w in wanted if w not in CHECKS]
        if unknown:
            print(f"unknown check(s): {', '.join(unknown)}", file=sys.stderr)
            print(f"available: {', '.join(CHECKS)}", file=sys.stderr)
            return 2

    tl, tr, bl, br, ml, mr, h, v = BOX
    width = 66
    rule = h * width
    dash = "-" if not _UNICODE else "—"

    def boxed(text: str = "") -> None:
        print(v + f"   {text}".ljust(width) + v)

    print(f"\n{tl}{rule}{tr}")
    boxed("Titanium Training - AIP Direct Service Validator")
    print(f"{ml}{rule}{mr}")
    boxed("These services bypass APIM. Connect the VPN first.")
    boxed(f"For the gateway models {dash} Claude, GPT, embeddings, rerank {dash}")
    boxed("use validate_apim.sh instead.")
    print(f"{bl}{rule}{br}\n")

    r = Results()
    for w in wanted:
        CHECKS[w](r, args.verbose)

    failed, skipped, passed = r.count(FAIL), r.count(SKIP), r.count(OK)
    print("\n" + HRULE * 40)
    print(f"  Total: {len(r.rows)}   "
          f"{_c('1;32', f'{passed} passed')}   "
          f"{_c('1;31', f'{failed} failed')}   "
          f"{_c('1;33', f'{skipped} skipped')}")
    print(HRULE * 40)

    if skipped and not failed:
        print("\n  Skipped checks just mean the credential is not in your .env.")
        print("  Fill in only the services your team application uses.")
    if failed:
        if trust_store_empty():
            print()
            print(trust_store_advice())
        else:
            print("\n  If several failed at once, check the VPN first —")
            print("  every service here is network-restricted.")
    print()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
