import requests
import time


API_KEY = "50a3ca6c1714d71941141a2e0957fb6108002acd790332b8bc8f7e9667d49e7d"


def check_url(url):

    headers = {
        "x-apikey": API_KEY
    }

    try:

        # Submit URL
        response = requests.post(

            "https://www.virustotal.com/api/v3/urls",

            headers=headers,

            data={
                "url": url
            }
        )

        if response.status_code != 200:

            return None

        analysis_id = response.json()["data"]["id"]

        # Wait for analysis
        time.sleep(3)

        # Get report
        report = requests.get(

            f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",

            headers=headers
        )

        if report.status_code != 200:

            return None

        stats = report.json(
        )["data"]["attributes"]["stats"]

        return {

            "malicious":
                stats["malicious"],

            "suspicious":
                stats["suspicious"],

            "harmless":
                stats["harmless"]
        }

    except Exception as e:

        print(
            "VirusTotal Error:",
            e
        )

        return None