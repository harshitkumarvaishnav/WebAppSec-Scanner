"""
waf_detector.py

Purpose:
Detect Web Application Firewall using an existing HTTP response.
"""


def detect_waf(response):

    try:

        headers = response.headers

        server = headers.get("Server", "").lower()

        if "cloudflare" in server or "CF-Ray" in headers:
            return {
                "detected": True,
                "vendor": "Cloudflare",
                "confidence": 99,
                "reason": "CF-Ray / CF-Cache-Status headers detected."
            }

        if "akamai" in server:
            return {
                "detected": True,
                "vendor": "Akamai",
                "confidence": 95,
                "reason": "Server header indicates Akamai."
            }

        if "sucuri" in server:
            return {
                "detected": True,
                "vendor": "Sucuri",
                "confidence": 95,
                "reason": "Server header indicates Sucuri."
            }

        if "imperva" in server:
            return {
                "detected": True,
                "vendor": "Imperva",
                "confidence": 95,
                "reason": "Server header indicates Imperva."
            }

        if "f5" in server:
            return {
                "detected": True,
                "vendor": "F5 BIG-IP ASM",
                "confidence": 90,
                "reason": "Server header indicates F5."
            }

        return {
            "detected": False,
            "vendor": None,
            "confidence": 0,
            "reason": "No WAF signature detected."
        }

    except Exception as e:
        return {
            "error": str(e)
        }