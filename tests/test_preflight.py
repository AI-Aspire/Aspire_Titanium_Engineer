"""The network preflight, without a network."""
from helpers import preflight as P


def test_a_public_ca_is_open():
    p = P.Probe(host="pypi.org", dns_ok=True, connected=True, issuer="Let's Encrypt")
    assert p.verdict == "open" and not p.intercepted


def test_a_private_ca_counts_as_intercepted():
    p = P.Probe(host="pypi.org", dns_ok=True, connected=True, issuer="Corp Root CA")
    assert p.verdict == "intercepted" and p.intercepted


def test_a_failed_lookup_or_connection_is_blocked():
    assert P.Probe(host="x", dns_ok=False).verdict == "blocked"
    assert P.Probe(host="x", dns_ok=True, connected=False, error="timed out").verdict == "blocked"


def test_a_plain_http_endpoint_is_open_without_a_certificate():
    p = P.Probe(host="10.0.0.5", port=8000, tls=False, dns_ok=True, connected=True)
    assert p.verdict == "open" and not p.intercepted


def test_issuer_parsing_reads_the_organisation_before_the_common_name():
    cert = {"issuer": ((("countryName", "US"),), (("organizationName", "DigiCert Inc"),),
                       (("commonName", "DigiCert Global G2"),))}
    assert P.issuer_of(cert) == "DigiCert Inc"
    assert P.issuer_of({"issuer": ((("commonName", "Corp Proxy CA"),),)}) == "Corp Proxy CA"
    assert P.issuer_of({}) == ""


def test_the_model_endpoint_joins_the_host_list_with_its_own_port():
    found = P.hosts("http://10.0.0.5:8000/v1")
    assert found[-1] == ("10.0.0.5", "the model endpoint in .env", 8000, False)
    found = P.hosts("https://api.example.com/v1")
    assert found[-1] == ("api.example.com", "the model endpoint in .env", 443, True)
    assert len(P.hosts("")) == len(P.DEFAULT_HOSTS)
    assert len(P.hosts("https://github.com/x")) == len(P.DEFAULT_HOSTS)   # no duplicate row


def test_proxy_variables_are_counted_once_per_value():
    env = {"HTTPS_PROXY": "http://proxy:3128", "https_proxy": "http://proxy:3128",
           "SSL_CERT_FILE": "/etc/corp.pem", "NO_PROXY": ""}
    assert P._proxy_env(env) == {"HTTPS_PROXY": "http://proxy:3128", "SSL_CERT_FILE": "/etc/corp.pem"}
    env["https_proxy"] = "http://other:3128"
    assert set(P._proxy_env(env)) == {"HTTPS_PROXY", "https_proxy", "SSL_CERT_FILE"}


def test_report_summarises_and_only_fails_when_every_host_did():
    ok = P.Probe(host="a", dns_ok=True, connected=True, issuer="Amazon")
    mitm = P.Probe(host="b", dns_ok=True, connected=True, issuer="Corp Root CA")
    dead = P.Probe(host="c")
    r = P.Report(probes=[ok, mitm, dead], proxy_env={"HTTPS_PROXY": "x"})
    assert str(r) == "2/3 reachable · TLS intercepted by Corp Root CA · 1 proxy or trust-store variables set"
    assert not r.all_failed and "Blocked: c" in r.verdict()
    assert P.Report(probes=[dead, dead]).all_failed
    assert not P.Report().all_failed
    assert "Open network" in P.Report(probes=[ok]).verdict()


def test_check_egress_with_no_hosts_does_not_touch_the_network():
    r = P.check_egress([])
    assert r.probes == [] and not r.all_failed
