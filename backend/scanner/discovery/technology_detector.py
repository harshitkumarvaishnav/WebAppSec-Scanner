"""
technology_detector.py

Purpose:
Detect technologies from an existing HTTP response.
"""


def detect_technologies(response):

    try:

        headers = response.headers

        server = headers.get("Server", "Unknown")

        backend = "Unknown"
        framework = "Unknown"
        cdn = "Unknown"

        server_lower = server.lower()

        if "cloudflare" in server_lower:
            cdn = "Cloudflare"

        elif "akamai" in server_lower:
            cdn = "Akamai"

        elif "fastly" in server_lower:
            cdn = "Fastly"

        elif "nginx" in server_lower:
            backend = "Nginx"

        elif "apache" in server_lower:
            backend = "Apache"

        elif "iis" in server_lower:
            backend = "Microsoft IIS"

        if "X-Powered-By" in headers:
            framework = headers["X-Powered-By"]

        return {

            "server": server,

            "backend": backend,

            "framework": framework,

            "cdn": cdn,

            "headers": dict(headers)

        }

    except Exception as e:

        return {
            "error": str(e)
        }