import re


def extract_urls(email):

    urls = re.findall(
        r'https?://[^\s]+',
        email
    )

    return urls


def extract_sender(email):

    match = re.search(
        r'From:\s*(.*)',
        email
    )

    if match:
        return match.group(1)

    return "Unknown"


dangerous_extensions = [

    ".exe",
    ".js",
    ".vbs",
    ".scr",
    ".zip",
    ".docm",
    ".xlsm"
]


def detect_attachment(email):

    found = []

    for ext in dangerous_extensions:

        if ext in email.lower():
            found.append(ext)

    return found