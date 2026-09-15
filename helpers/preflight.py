"""What your network allows, found out before the first morning.

Standard library only. It has to run before anything is installed, on a
machine that may not be able to install anything.

    from helpers import preflight
    report = preflight.check_egress()
    print(report)               # 5/6 reachable · TLS intercepted by Corp Root CA

Two things make it worth a module. **The deadline is the feature.** A serial
probe on a locked-down corporate network can hang for minutes, because
`socket.getaddrinfo` ignores socket timeouts and a blackholed DNS query blocks
until the resolver gives up. Every probe here runs in a daemon thread with a
wall-clock budget and is reported as blocked when it misses it. And naming the
interceptor is the point. "TLS succeeded" is not the interesting result on a
managed laptop. Who signed the certificate is. A corporate proxy re-signs
every certificate with an internal CA, which is why `pip` works in the
terminal and fails inside a container that does not trust that CA.
"""
from __future__ import annotations

import os
import queue
import socket
import ssl
import threading
import time
from dataclasses import dataclass, field
from urllib.parse import urlsplit

# The hosts every notebook in the course reaches for at some point.
DEFAULT_HOSTS: tuple[tuple[str, str], ...] = (
    ("pypi.org", "the package index"),
    ("files.pythonhosted.org", "the wheel downloads"),
    ("github.com", "this repository"),
    ("huggingface.co", "open weights and tokenizers"),
    ("cdn.jsdelivr.net", "the CDN the notebook widgets load"),
)

# Issuer organisations that are public certificate authorities. Anything else
# signing a public site means something is terminating your TLS.
PUBLIC_CAS = (
    "digicert", "let's encrypt", "isrg", "google trust services", "amazon",
    "sectigo", "comodo", "globalsign", "cloudflare", "microsoft", "baltimore",
    "usertrust", "godaddy", "entrust", "identrust", "starfield", "verisign",
    "thawte", "geotrust", "rapidssl", "buypass", "actalis", "certum",
)

# Environment variables that reveal a proxy or a swapped trust store.
PROXY_VARS = (
    "HTTP_PROXY", "HTTPS_PROXY", "NO_PROXY",
    "http_proxy", "https_proxy", "no_proxy",
    "REQUESTS_CA_BUNDLE", "SSL_CERT_FILE", "CURL_CA_BUNDLE",
    "NODE_EXTRA_CA_CERTS", "PIP_INDEX_URL", "PIP_TRUSTED_HOST",
    "UV_INDEX_URL", "UV_DEFAULT_INDEX",
)

OPEN, INTERCEPTED, BLOCKED = "open", "intercepted", "blocked"


@dataclass
class Probe:
    """One host: did the name resolve, did the connection open, who signed it."""

    host: str
    why: str = ""
    port: int = 443
    tls: bool = True
    ip: str | None = None
    dns_ok: bool = False
    connected: bool = False
    issuer: str = ""
    error: str = ""

    @property
    def intercepted(self) -> bool:
        """True when a public site was signed by something that is not a public CA."""
        return self.connected and self.tls and is_private_issuer(self.issuer)

    @property
    def verdict(self) -> str:
        if not self.dns_ok or not self.connected:
            return BLOCKED
        return INTERCEPTED if self.intercepted else OPEN


@dataclass
class Report:
    probes: list = field(default_factory=list)
    proxy_env: dict = field(default_factory=dict)

    @property
    def blocked(self) -> list:
        return [p for p in self.probes if p.verdict == BLOCKED]

    @property
    def intercepted(self) -> list:
        return [p for p in self.probes if p.verdict == INTERCEPTED]

    @property
    def all_failed(self) -> bool:
        return bool(self.probes) and len(self.blocked) == len(self.probes)

    def __str__(self) -> str:
        bits = [f"{len(self.probes) - len(self.blocked)}/{len(self.probes)} reachable"]
        if self.intercepted:
            names = sorted({p.issuer for p in self.intercepted})
            bits.append(f"TLS intercepted by {', '.join(names)}")
        if self.proxy_env:
            bits.append(f"{len(self.proxy_env)} proxy or trust-store variables set")
        return " · ".join(bits)

    def verdict(self) -> str:
        """One paragraph on what the result means for the week."""
        if self.blocked:
            hosts = ", ".join(p.host for p in self.blocked)
            return (f"Blocked: {hosts}. Someone has to allow these or mirror them "
                    f"internally before the first morning. Find out who now.")
        if self.intercepted:
            names = ", ".join(sorted({p.issuer for p in self.intercepted}))
            return (f"TLS is terminated by {names}. Your terminal works because the "
                    f"operating system trusts that CA. A container or a fresh "
                    f"virtual environment does not, so keep that CA file to hand.")
        return "Open network, public CAs, no proxy. Nothing here will slow you down."


# ── pure parts ───────────────────────────────────────────────────────────────

def is_private_issuer(issuer: str) -> bool:
    """True when the issuer is not one of the public certificate authorities."""
    if not issuer:
        return False
    low = issuer.lower()
    return not any(ca in low for ca in PUBLIC_CAS)


def issuer_of(cert: dict) -> str:
    """The organisation that signed a certificate, from `getpeercert()`'s shape.

    The issuer arrives as a tuple of relative distinguished names, each a tuple
    of `(key, value)` pairs. The organisation is what names a proxy; the common
    name is a fallback for a CA that set no organisation.
    """
    org, common = "", ""
    for rdn in (cert or {}).get("issuer", ()):
        for key, value in rdn:
            if key == "organizationName" and not org:
                org = value
            elif key == "commonName" and not common:
                common = value
    return org or common


def host_of(url: str) -> tuple[str, int, bool] | None:
    """`(host, port, tls)` for a base URL, or None when there is no host in it."""
    if not url:
        return None
    parts = urlsplit(url if "://" in url else "https://" + url)
    if not parts.hostname:
        return None
    tls = parts.scheme != "http"
    port = parts.port or (443 if tls else 80)
    return parts.hostname, port, tls


def hosts(base_url: str | None = None) -> tuple[tuple[str, str, int, bool], ...]:
    """The default hosts plus the model endpoint, when one is configured.

    The endpoint comes from `helpers.config` when it imports, and from
    `OPENAI_BASE_URL` in the environment when it does not: a machine that
    cannot install `python-dotenv` yet still needs the probe to run.
    """
    if base_url is None:
        try:
            from helpers import config as C

            base_url = C.LLM_BASE
        except Exception:  # noqa: BLE001  nothing installed yet
            base_url = os.environ.get("OPENAI_BASE_URL")
    out = [(h, why, 443, True) for h, why in DEFAULT_HOSTS]
    parsed = host_of(base_url or "")
    if parsed and parsed[0] not in {h for h, *_ in out}:
        host, port, tls = parsed
        out.append((host, "the model endpoint in .env", port, tls))
    return tuple(out)


def _proxy_env(environ=None) -> dict[str, str]:
    """The proxy and trust-store variables actually set, counted once each.

    `HTTPS_PROXY` and `https_proxy` are two variables on Unix and one on
    Windows, where lookup is case-insensitive. A repeat is collapsed only
    when the value matches, so divergent casings on Unix still show.
    """
    environ = os.environ if environ is None else environ
    seen: dict[str, str] = {}
    env: dict[str, str] = {}
    for name in PROXY_VARS:
        value = environ.get(name)
        if not value or seen.get(name.upper()) == value:
            continue
        seen[name.upper()] = value
        env[name] = value
    return env


# ── the network part ─────────────────────────────────────────────────────────

def _one(host: str, why: str, port: int, tls: bool, timeout: float) -> Probe:
    probe = Probe(host=host, why=why, port=port, tls=tls)
    try:
        # getaddrinfo rather than gethostbyname: it returns IPv6 too and fails
        # with a clean exception.
        info = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
        probe.ip = info[0][4][0]
        probe.dns_ok = True
    except Exception as exc:  # noqa: BLE001
        probe.error = type(exc).__name__
        return probe

    try:
        with socket.create_connection((host, port), timeout=timeout) as raw:
            if not tls:
                probe.connected = True
                return probe
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(raw, server_hostname=host) as sock:
                probe.connected = True
                probe.issuer = issuer_of(sock.getpeercert() or {})
    except Exception as exc:  # noqa: BLE001
        probe.error = f"{type(exc).__name__}: {exc}"[:80]
    return probe


def check_egress(targets=None, *, timeout: float = 6.0, workers: int = 8) -> Report:
    """Probe every host concurrently, with a wall-clock deadline for the batch.

    `targets` is a sequence of `(host, why)` or `(host, why, port, tls)`;
    the default is `hosts()`. The deadline lives here rather than on the
    socket because DNS resolution ignores socket timeouts. A probe that
    misses it is abandoned and reported as blocked.

    The workers are daemon threads rather than a `ThreadPoolExecutor`. A
    pool's workers are joined at interpreter exit, which would move the hang
    this module exists to prevent from the middle of the run to the end of
    it. Nothing joins these, so a stuck `getaddrinfo` cannot delay exit.
    """
    targets = tuple(hosts() if targets is None else targets)
    spec = [(t[0], t[1], t[2] if len(t) > 2 else 443, t[3] if len(t) > 3 else True) for t in targets]
    report = Report(proxy_env=_proxy_env())
    if not spec:
        return report

    todo: queue.Queue = queue.Queue()
    for i, item in enumerate(spec):
        todo.put((i, item))
    done: queue.Queue = queue.Queue()

    def _worker() -> None:
        while True:
            try:
                index, (host, why, port, tls) = todo.get_nowait()
            except queue.Empty:
                return
            try:
                done.put((index, _one(host, why, port, tls, timeout)))
            except BaseException as exc:  # noqa: BLE001  a worker must never die silently
                done.put((index, Probe(host=host, why=why, port=port, tls=tls,
                                       error=f"{type(exc).__name__}: {exc}"[:80])))

    for n in range(max(1, min(workers, len(spec)))):
        threading.Thread(target=_worker, name=f"preflight-{n}", daemon=True).start()

    budget = timeout * 2 + 2
    deadline = time.monotonic() + budget
    collected: dict[int, Probe] = {}
    while len(collected) < len(spec):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        try:
            index, probe = done.get(timeout=remaining)
        except queue.Empty:
            break
        collected[index] = probe

    # A host that did not answer is still a finding: name it, do not drop it.
    for index, (host, why, port, tls) in enumerate(spec):
        if index not in collected:
            collected[index] = Probe(host=host, why=why, port=port, tls=tls,
                                     error=f"no answer within {budget:.0f}s, treated as blocked")
    report.probes = [collected[i] for i in range(len(spec))]
    return report
