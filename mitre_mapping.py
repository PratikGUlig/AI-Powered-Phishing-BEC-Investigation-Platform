def map_attack(data):

    techniques = []

    # Phishing Link
    if data["suspicious_urls"]:

        techniques.append({

            "id": "T1566.002",

            "name": "Spearphishing Link"
        })

    # Attachment
    if data["attachments"]:

        techniques.append({

            "id": "T1566.001",

            "name": "Spearphishing Attachment"
        })

    # Spoofing
    if data["spoof"]:

        techniques.append({

            "id": "T1583",

            "name": "Acquire Infrastructure"
        })

    # Credential Harvesting
    if data["keywords"]:

        for word in data["keywords"]:

            if word in [

                "verify",
                "password",
                "login immediately",
                "bank account"

            ]:

                techniques.append({

                    "id": "T1056",

                    "name": "Input Capture"
                })

                break

    # BEC
    if data["bec"]:

        techniques.append({

            "id": "T1656",

            "name": "Impersonation"
        })

        techniques.append({

            "id": "T1566",

            "name": "Phishing"
        })

    return techniques