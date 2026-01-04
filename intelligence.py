SSRF_PARAMS = {
    "url": 3, "uri": 3, "link": 3, "target": 3,
    "dest": 3, "callback": 3,
    "redirect": 2, "next": 2, "return": 2,
    "image": 2, "feed": 2
}

def is_ssrf_candidate(param):
    return SSRF_PARAMS.get(param.lower(), 0) >= 2
