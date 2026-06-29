import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


COMMON_APIS = [
    "/api",
    "/api/v1",
    "/api/v2",
    "/graphql",
    "/swagger",
    "/swagger-ui",
    "/openapi.json",
    "/swagger.json",
    "/v1",
    "/v2"
]


def discover_api(base_url, response):

    found = []

    try:

        soup = BeautifulSoup(response.text, "html.parser")

        # HTML links
        for tag in soup.find_all(["a", "form"]):

            value = tag.get("href") or tag.get("action")

            if value and "api" in value.lower():

                found.append(urljoin(base_url, value))

        # JS files
        scripts = []

        for script in soup.find_all("script"):

            src = script.get("src")

            if src:

                scripts.append(urljoin(base_url, src))

        for js in scripts:

            try:

                js_data = requests.get(js, timeout=5).text

                matches = re.findall(
                    r'["\'](\/api\/[^"\']+)["\']',
                    js_data
                )

                for m in matches:

                    found.append(urljoin(base_url, m))

            except:

                pass

        # Common endpoints

        for api in COMMON_APIS:

            url = urljoin(base_url, api)

            try:

                r = requests.get(
                    url,
                    timeout=5,
                    allow_redirects=False
                )

                if r.status_code in [200, 401, 403]:

                    found.append(url)

            except:

                pass

        found = sorted(list(set(found)))

        return {

            "count": len(found),

            "endpoints": found

        }

    except Exception as e:

        return {

            "error": str(e)

        }