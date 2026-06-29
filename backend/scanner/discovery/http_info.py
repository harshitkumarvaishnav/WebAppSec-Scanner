"""
http_info.py

Purpose:
Extract HTTP information from an existing Response object.
"""


def get_http_info(response, response_time):

    try:

        return {

            "status_code": response.status_code,

            "response_time": f"{response_time:.3f} sec",

            "server": response.headers.get("Server", "Unknown"),

            "content_type": response.headers.get("Content-Type", "Unknown"),

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