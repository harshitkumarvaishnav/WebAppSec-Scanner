import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy"
]


def get_security_headers(url):

    try:

        response = requests.get(url, timeout=10)

        result = {}

        for header in SECURITY_HEADERS:

            if header in response.headers:
                result[header] = response.headers[header]
            else:
                result[header] = "Missing"

        return result

    except Exception as e:

        return {
            "error": str(e)
        }