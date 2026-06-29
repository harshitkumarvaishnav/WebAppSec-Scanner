import requests
from urllib.parse import urlparse


def get_subdomains(url: str):

    try:

        domain = urlparse(url).netloc.replace("www.", "")

        api = f"https://crt.sh/?q=%25.{domain}&output=json"

        response = requests.get(api, timeout=20)

        if response.status_code != 200:

            return {
                "count": 0,
                "subdomains": []
            }

        data = response.json()

        names = set()

        for item in data:

            value = item.get("name_value", "")

            for host in value.split("\n"):

                host = host.strip()

                if host.endswith(domain):

                    names.add(host)

        names = sorted(names)

        return {

            "count": len(names),

            "subdomains": names[:100]

        }

    except Exception as e:

        return {
            "error": str(e)
        }