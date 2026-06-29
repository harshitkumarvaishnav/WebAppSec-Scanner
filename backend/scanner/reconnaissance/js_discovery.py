from bs4 import BeautifulSoup
from urllib.parse import urljoin


def discover_js(response):

    try:

        soup = BeautifulSoup(response.text, "html.parser")

        js_files = set()

        for script in soup.find_all("script"):

            src = script.get("src")

            if src:

                js_files.add(urljoin(response.url, src))

        return {
            "total": len(js_files),
            "files": sorted(list(js_files))
        }

    except Exception as e:

        return {
            "error": str(e)
        }