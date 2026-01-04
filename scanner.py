import requests, time
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from intelligence import is_ssrf_candidate
from payloads import generate_payloads
from verifier import timing_anomaly, error_indicator

HEADERS = {"User-Agent": "LΞX-SSRF"}

def scan(url, oob):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    findings = []

    # baseline
    start = time.time()
    requests.get(url, headers=HEADERS, timeout=10)
    baseline = time.time() - start

    for param in params:
        if not is_ssrf_candidate(param):
            continue

        original = params[param][0]

        for payload in generate_payloads(original, oob):
            test_params = params.copy()
            test_params[param] = payload

            test_url = urlunparse(
                parsed._replace(query=urlencode(test_params, doseq=True))
            )

            start = time.time()
            r = requests.get(test_url, headers=HEADERS, timeout=15)
            elapsed = time.time() - start

            score = 0
            signals = []

            if timing_anomaly(baseline, elapsed):
                score += 40
                signals.append("TIMING")

            if error_indicator(r.text):
                score += 30
                signals.append("ERROR")

            if score >= 40:
                findings.append({
                    "param": param,
                    "url": test_url,
                    "signals": signals,
                    "confidence": score
                })

    return findings
