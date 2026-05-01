import re

BLOCKED_PATTERNS = [
    r"<.*?>",                     # HTML tags
    r"(?i)ignore",               # prompt injection
    r"(?i)system",
    r"(?i)override",
    r"(?i)drop table",           # SQL
    r"(?i)select .* from",
]

def sanitize_input(text):
    if not text:
        return None

    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, text):
            return None

    # Clean HTML
    text = re.sub(r"<.*?>", "", text)

    return text.strip()