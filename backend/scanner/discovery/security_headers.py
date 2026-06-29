"""
security_headers.py

Purpose:
Extract security headers from an existing HTTP response.
"""


SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy"
]


def get_security_headers(response):

    try:

        headers = {}

        for header in SECURITY_HEADERS:

            if header in response.headers:

                headers[header] = response.headers[header]

        return headers

    except Exception as e:

        return {
            "error": str(e)
        }