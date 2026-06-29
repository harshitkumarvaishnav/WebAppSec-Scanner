from urllib.parse import urlparse

import whois


def get_whois_info(url: str):

    try:

        domain = urlparse(url).netloc.replace("www.", "")

        info = whois.whois(domain)

        return {

            "domain": domain,

            "registrar": info.registrar,

            "creation_date": str(info.creation_date),

            "expiration_date": str(info.expiration_date),

            "updated_date": str(info.updated_date),

            "name_servers": info.name_servers,

            "emails": info.emails,

        }

    except Exception as e:

        return {
            "error": str(e)
        }