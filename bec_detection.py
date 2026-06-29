def detect_bec(email):

    score = 0

    indicators = []

    email = email.lower()

    # Urgency
    urgent_words = [
        "urgent",
        "immediately",
        "asap",
        "right now",
        "today"
    ]

    for word in urgent_words:

        if word in email:

            indicators.append(
                f"Urgency: {word}"
            )

            score += 10

    # Financial request
    finance_words = [
        "transfer",
        "wire",
        "payment",
        "funds",
        "invoice",
        "bank account"
    ]

    for word in finance_words:

        if word in email:

            indicators.append(
                f"Financial: {word}"
            )

            score += 20

    # Secrecy
    secret_words = [
        "confidential",
        "do not discuss",
        "secret",
        "private"
    ]

    for word in secret_words:

        if word in email:

            indicators.append(
                f"Secrecy: {word}"
            )

            score += 15

    # Authority
    authority_words = [
        "ceo",
        "director",
        "manager",
        "executive"
    ]

    for word in authority_words:

        if word in email:

            indicators.append(
                f"Authority: {word}"
            )

            score += 15

    return {

        "score": score,

        "indicators": indicators
    }