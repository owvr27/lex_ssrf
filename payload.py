def generate_payloads(original, oob):
    base = original.split("//")[-1].split("/")[0]

    return [
        f"http://{oob}",
        f"https://{base}.{oob}",
        f"https://{base}@{oob}",
        f"https://{oob}#{base}",
        f"ftp://{oob}"
    ]
