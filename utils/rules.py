def detect_attack_type(url):
    u = url.lower()

    if "union select" in u or "or 1=1" in u:
        return "SQL Injection"

    if "<script>" in u:
        return "Cross-Site Scripting (XSS)"

    if "../" in u:
        return "Directory Traversal"

    if "@" in url and "http" in url:
        return "Phishing / URL Spoofing"

    if "=" in url and "&" in url:
        return "HTTP Parameter Pollution"

    return None