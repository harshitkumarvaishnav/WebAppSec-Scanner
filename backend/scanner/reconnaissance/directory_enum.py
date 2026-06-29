from urllib.parse import urljoin

import requests


COMMON_PATHS = [

    "admin",
    "login",
    "dashboard",
    "api",
    "graphql",
    "swagger",
    "docs",
    "uploads",
    "backup",
    ".git",
    "robots.txt",
    "sitemap.xml"

]


def enumerate_directories(base_url):

    found = []

    try:

        for path in COMMON_PATHS:

            url = urljoin(base_url.rstrip("/") + "/", path)

            try:

                response = requests.get(
                    url,
                    timeout=5,
                    allow_redirects=False
                )

                if response.status_code in [200, 301, 302, 401, 403]:

                    found.append({

                        "path": path,

                        "status": response.status_code,

                        "url": url

                    })

            except:

                continue

        return {

            "checked": len(COMMON_PATHS),

            "found": len(found),

            "directories": found

        }

    except Exception as e:

        return {
            "error": str(e)
        }