import whois
from urllib.parse import urlparse
from datetime import datetime, timezone


def extract_domain(url):

    try:
        return urlparse(url).netloc

    except:
        return None


def get_domain_age(domain):

    try:

        info = whois.whois(domain)

        creation = info.creation_date

        if isinstance(creation, list):
            creation = creation[0]

        if creation is None:
            return None

        if creation.tzinfo is None:
            creation = creation.replace(
                tzinfo=timezone.utc
            )

        now = datetime.now(
            timezone.utc
        )

        age = (
            now - creation
        ).days

        return age

    except Exception as e:

        print(
            "WHOIS ERROR:",
            e
        )

        return None