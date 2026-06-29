def calculate_score(data):

    score = 0

    # Suspicious URLs
    if data["suspicious_urls"]:
        score += 30

    # Keywords
    if data["keywords"]:
        score += 15

    # Sender Spoofing
    if data["spoof"]:
        score += 20

    # Attachment
    if data["attachments"]:
        score += 10

    # Newly Registered Domain
    if data["new_domain"]:
        score += 25

    # VirusTotal
    if data["malicious"]:
        score += 30

    # Business Email Compromise
    if data["bec"]:
        score += 40

    return score


def get_severity(score):

    if score <= 20:
        return "LOW"

    elif score <= 50:
        return "MEDIUM"

    else:
        return "HIGH"