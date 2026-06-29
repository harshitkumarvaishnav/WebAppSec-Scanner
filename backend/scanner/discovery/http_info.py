import requests
import time


def get_http_info(url: str):

    start = time.time()

    try:

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        elapsed = round(time.time() - start, 3)

        return {

            "status_code": response.status_code,

            "response_time": f"{elapsed} sec",

            "server": response.headers.get("Server", "Unknown"),

            "content_type": response.headers.get("Content-Type"),

            "content_length": response.headers.get(
                "Content-Length",
                "Unknown"
            ),

            "final_url": response.url

        }

    except Exception as e:

        return {
            "error": str(e)
        }