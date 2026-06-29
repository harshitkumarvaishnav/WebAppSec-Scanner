"""
cookie_analyzer.py

Purpose:
Analyze cookies from an existing HTTP response.
"""


def analyze_cookies(response):

    try:

        cookies = []

        for cookie in response.cookies:

            cookies.append({
                "name": cookie.name,
                "value": cookie.value,
                "domain": cookie.domain,
                "path": cookie.path,
                "secure": cookie.secure,
                "expires": cookie.expires
            })

        framework = "Unknown"

        names = [c["name"].lower() for c in cookies]

        if any("php" in n for n in names):
            framework = "PHP"

        elif any("asp" in n for n in names):
            framework = "ASP.NET"

        elif any("jsessionid" in n for n in names):
            framework = "Java"

        elif any("laravel" in n for n in names):
            framework = "Laravel"

        return {
            "total": len(cookies),
            "framework_hint": framework,
            "cookies": cookies
        }

    except Exception as e:
        return {
            "error": str(e)
        }