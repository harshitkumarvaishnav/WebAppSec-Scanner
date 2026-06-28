from urllib.parse import urlparse


def validate_url(url: str):
    """
    Validate the target URL.
    """

    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        return False, "Invalid URL. Use http:// or https://"

    if not parsed.netloc:
        return False, "Invalid Domain"

    return True, "Valid URL"