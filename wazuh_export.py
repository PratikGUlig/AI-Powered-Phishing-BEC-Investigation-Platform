import json
import os
from datetime import datetime


def export_wazuh(data):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    filename = (
        "reports/"
        "wazuh_alert.json"
    )

    mitre_ids = []

    for m in data["mitre"]:

        mitre_ids.append(
            m["id"]
        )

    alert = {

        "timestamp":
            str(
                datetime.now()
            ),

        "rule": {

            "id":
                "100500",

            "level":
                data["score"],

            "description":
                "AI Phishing Detection"
        },

        "agent": {

            "id":
                "001",

            "name":
                "AI-Phishing-Analyzer"
        },

        "event": {

            "sender":
                data["sender"],

            "severity":
                data["severity"],

            "score":
                data["score"],

            "indicators":
                data["indicators"],

            "bec":
                data["bec"]
        },

        "mitre":
            mitre_ids
    }

    with open(

        filename,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            alert,

            file,

            indent=4
        )

    return filename