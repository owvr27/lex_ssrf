def report(findings):
    for f in findings:
        level = (
            "CONFIRMED" if f["confidence"] >= 80 else
            "STRONG" if f["confidence"] >= 60 else
            "POSSIBLE"
        )

        print(f"[SSRF:{level}] {f['param']} → {f['url']} | {f['signals']}")
