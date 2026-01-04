def timing_anomaly(baseline, test):
    return test > baseline * 1.8

def error_indicator(text):
    keywords = [
        "connection refused", "timeout",
        "could not resolve", "invalid url",
        "connection reset"
    ]
    return any(k in text.lower() for k in keywords)
