  LΞX-SSRF

Advanced Server-Side Request Forgery Detector
Made by Omar Abdelsalam


# LΞX-SSRF

**LΞX-SSRF** is an advanced **Server-Side Request Forgery (SSRF) detection tool** designed for **real bug bounty hunters** and **penetration testers**.

It is **not a payload-spraying scanner**.  
It is a **detection system** built around **how SSRF is actually found and accepted** in real-world programs.

---

## 🎯 Design Goals

- Detect **all known SSRF entry points**
- Minimize false positives
- Preserve application logic
- Rely on **proof, not guessing**
- Stay **ethical and authorization-safe**
- Produce **actionable, report-ready results**

---

## 🧠 What Makes LΞX-SSRF Different

Most SSRF tools fail because they:
- Blindly replace parameters
- Ignore validation logic
- Produce “possible SSRF” noise
- Rely on metadata exploitation

**LΞX-SSRF instead focuses on:**

- **Parameter intelligence**
- **Context-preserving payloads**
- **Multi-signal verification**
- **Confidence-based reporting**

This is how **experienced bug hunters** work.

---

## 🔥 SSRF Types Covered

LΞX-SSRF is designed to detect **all practical SSRF classes**:

- ✅ Basic SSRF
- ✅ Blind SSRF
- ✅ Filtered / allowlist SSRF
- ✅ Redirect-based SSRF
- ✅ POST / JSON SSRF
- ✅ Header-based SSRF
- ✅ Stored / delayed SSRF (via OOB)
- ✅ Internal service SSRF
- ✅ Protocol-based SSRF (safe protocols)

> Cloud metadata targeting is **disabled by default** and must be explicitly enabled.

---

## 🧩 Architecture Overview

lex-ssrf/
├── lex_ssrf.py # Main CLI entry
├── intelligence.py # SSRF parameter detection
├── payloads.py # Context-aware payload engine
├── scanner.py # Request execution logic
├── verifier.py # Timing & error analysis
└── reporter.py # Confidence-based output


---

## 🧠 Detection Methodology

LΞX-SSRF does **not rely on a single signal**.

It correlates multiple indicators:

| Signal | Meaning |
|-----|--------|
| OOB callback | Confirmed SSRF |
| Timing anomaly | Blind/internal SSRF |
| Error behavior change | Backend fetch attempt |
| Redirect behavior | Redirect-based SSRF |

Each finding is assigned a **confidence score**, making triage and reporting easy.

---

## 🖥 Usage

```bash
python3 lex_ssrf.py \
  -u "https://target.com/api?url=https://example.com" \
  --oob abc123.interact.sh

Example Output

[SSRF:STRONG] url → https://target.com/api?url=https://example.com@abc123.interact.sh
Signals: TIMING, ERROR

📁 Output Philosophy

LΞX-SSRF intentionally:

    Avoids auto-exploitation

    Avoids unsafe defaults

    Produces human-reviewable results

Every finding is meant to be:

    Re-tested manually

    Clearly explained

    Easily accepted by programs

🛠 Requirements

    Python 3.8+

    requests

    An OOB interaction service (e.g. Burp Collaborator, Interactsh)

⚠️ Legal & Ethical Notice

This tool is intended only for authorized security testing.

    Do not test systems you do not own

    Do not test without permission

    The author is not responsible for misuse

LΞX-SSRF prioritizes responsible disclosure and ethical research.
👤 Author

Omar Abdelsalam

Security Researcher & Tool Developer
📈 Why This Tool Finds Valid Bugs

LΞX-SSRF mirrors real bug bounty workflows:

    Identify SSRF entry points intelligently

    Test with context-preserving payloads

    Verify via OOB / timing / behavior

    Manually confirm one payload

    Submit clean, evidence-based reports

This leads to accepted reports, not noise.
🚀 Roadmap

    POST / JSON body auto-extraction

    GraphQL SSRF detection

    Redirect-chain automation

    OOB auto-correlation

    Docker support

    Integration with LΞX Recon framework

⭐ Final Note

LΞX-SSRF is not built to replace thinking.
It is built to amplify it.

If you use it correctly, it will help you find real SSRF vulnerabilities.




