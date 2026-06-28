import socket
from urllib.parse import urlparse


def get_dns_info(url: str):

    domain = urlparse(url).netloc

    try:
        ip_address = socket.gethostbyname(domain)

        return {
            "domain": domain,
            "ip_address": ip_address
        }

    except Exception as e:

        return {
            "domain": domain,
            "ip_address": None,
            "error": str(e)
        }