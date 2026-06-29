from rapidfuzz import fuzz

phishing_keywords = [

    "urgent",
    "verify",
    "account suspended",
    "click here",
    "login immediately",
    "password",
    "bank account",
    "payment failed",
    "security alert"
]


def keyword_analysis(email):

    found = []

    for keyword in phishing_keywords:

        if keyword in email.lower():
            found.append(keyword)

    return found


def suspicious_urls(urls):

    suspicious = []

    indicators = [
        "login",
        "verify",
        "paypal",
        "secure",
        "bank",
        "account"
    ]

    for url in urls:

        for indicator in indicators:

            if indicator in url.lower():
                suspicious.append(url)
                break

    return suspicious


def detect_spoof(sender):

    trusted_domains = [
        "paypal.com",
        "amazon.com",
        "google.com",
        "microsoft.com"
    ]

    try:

        sender_domain = sender.split("@")[1]

        for domain in trusted_domains:

            similarity = fuzz.ratio(
                sender_domain.lower(),
                domain.lower()
            )

            if similarity > 80 and sender_domain != domain:
                return True

    except:
        pass

    return False