"""
request_handler.py

Creates one reusable HTTP session.
Every module uses the same response object.
"""

import requests


session = requests.Session()

session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36 "
        "WebAppSec-Scanner/1.0"
    )
})


def get_response(url):
    """
    Fetch target URL once.

    Returns:
        requests.Response | None
    """

    try:

        response = session.get(
            url,
            timeout=15,
            allow_redirects=True,
            verify=True
        )

        return response

    except requests.exceptions.RequestException:

        return None