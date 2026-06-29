from backend.models.result_manager import ResultManager

from backend.scanner.discovery.validator import validate_url
from backend.scanner.discovery.dns_lookup import get_dns_info
from backend.scanner.discovery.http_info import get_http_info
from backend.scanner.discovery.ssl_checker import get_ssl_info
from backend.scanner.discovery.security_headers import get_security_headers
from backend.scanner.discovery.robots import get_robots
from backend.scanner.discovery.sitemap import get_sitemap


def start_scan(scan):

    result = ResultManager()

    valid, message = validate_url(scan.url)

    if not valid:

        result.result["scan_info"] = {
            "target": scan.url,
            "testing_type": scan.testing_type,
            "status": "Failed"
        }

        result.result["findings"].append({
            "severity": "Info",
            "message": message
        })

        return result.get_result()

    dns = get_dns_info(scan.url)
    http = get_http_info(scan.url)
    ssl = get_ssl_info(scan.url)
    headers = get_security_headers(scan.url)
    robots = get_robots(scan.url)
    sitemap = get_sitemap(scan.url)

    result.result["scan_info"] = {
        "target": scan.url,
        "testing_type": scan.testing_type,
        "status": "Completed"
    }

    result.add_discovery("dns", dns)
    result.add_discovery("http", http)
    result.add_discovery("ssl", ssl)
    result.add_discovery("security_headers", headers)
    result.add_discovery("robots", robots)
    result.add_discovery("sitemap", sitemap)

    return result.get_result()