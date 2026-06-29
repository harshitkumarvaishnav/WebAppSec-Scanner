import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime


def get_ssl_info(url: str):

    try:

        hostname = urlparse(url).hostname

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:

                cert = ssock.getpeercert()

                return {
                    "enabled": True,
                    "issuer": dict(x[0] for x in cert["issuer"]),
                    "subject": dict(x[0] for x in cert["subject"]),
                    "valid_from": cert["notBefore"],
                    "valid_to": cert["notAfter"]
                }

    except Exception as e:

        return {
            "enabled": False,
            "error": str(e)
        }