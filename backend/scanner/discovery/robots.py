import requests


def get_robots(url):

    try:

        robots_url = url.rstrip("/") + "/robots.txt"

        response = requests.get(
            robots_url,
            timeout=10,
            headers={"User-Agent": "WebAppSec-Scanner/1.0"}
        )

        return {
            "url": robots_url,
            "status_code": response.status_code,
            "found": response.status_code == 200,
            "content": response.text if response.status_code == 200 else None
        }

    except Exception as e:

        return {
            "error": str(e)
        }