from time import perf_counter

from backend.models.result_manager import ResultManager

# Discovery
from backend.scanner.discovery.validator import validate_url
from backend.scanner.discovery.dns_lookup import get_dns_info
from backend.scanner.discovery.http_info import get_http_info
from backend.scanner.discovery.ssl_checker import get_ssl_info
from backend.scanner.discovery.security_headers import get_security_headers
from backend.scanner.discovery.robots import get_robots
from backend.scanner.discovery.sitemap import get_sitemap
from backend.scanner.discovery.technology_detector import detect_technologies
from backend.scanner.discovery.waf_detector import detect_waf
from backend.scanner.discovery.cookie_analyzer import analyze_cookies

# Reconnaissance
from backend.scanner.reconnaissance.whois_lookup import get_whois_info
from backend.scanner.reconnaissance.subdomains import get_subdomains
from backend.scanner.reconnaissance.js_discovery import discover_js
from backend.scanner.reconnaissance.directory_enum import enumerate_directories
from backend.scanner.reconnaissance.api_discovery import discover_api
from backend.scanner.reconnaissance.port_scan import scan_ports

# Shared Request
from backend.scanner.common.request_handler import get_response


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

    start = perf_counter()
    response = get_response(scan.url)
    elapsed = perf_counter() - start

    # -------------------------
    # Discovery
    # -------------------------

    try:
        http = get_http_info(response, elapsed)
    except:
        http = {"error": "HTTP information unavailable"}

    try:
        ssl = get_ssl_info(scan.url)
    except:
        ssl = {"error": "SSL check failed"}

    try:
        headers = get_security_headers(response)
    except:
        headers = {"error": "Security header scan failed"}

    try:
        robots = get_robots(scan.url)
    except:
        robots = {"error": "robots.txt scan failed"}

    try:
        sitemap = get_sitemap(scan.url)
    except:
        sitemap = {"error": "Sitemap scan failed"}

    try:
        technology = detect_technologies(response)
    except:
        technology = {"error": "Technology detection failed"}

    try:
        waf = detect_waf(response)
    except:
        waf = {"error": "WAF detection failed"}

    try:
        cookies = analyze_cookies(response)
    except:
        cookies = {"error": "Cookie analysis failed"}

    # -------------------------
    # Reconnaissance
    # -------------------------

    try:
        whois = get_whois_info(scan.url)
    except:
        whois = {"error": "WHOIS lookup failed"}

    try:
        subdomains = get_subdomains(scan.url)
    except:
        subdomains = {"error": "Subdomain enumeration failed"}

    try:
        javascript = discover_js(response)
    except:
        javascript = {"error": "JavaScript discovery failed"}

    try:
        directories = enumerate_directories(scan.url)
    except:
        directories = {"error": "Directory enumeration failed"}

    try:
        apis = discover_api(scan.url, response)
    except:
        apis = {"error": "API discovery failed"}

    try:
        ports = scan_ports(dns.get("ip_address"))
    except:
        ports = {"error": "Port scan failed"}

    # -------------------------
    # Scan Info
    # -------------------------

    result.result["scan_info"] = {
        "target": scan.url,
        "testing_type": scan.testing_type,
        "status": "Completed"
    }

    # -------------------------
    # Discovery Results
    # -------------------------

    result.add_discovery("dns", dns)
    result.add_discovery("http", http)
    result.add_discovery("ssl", ssl)
    result.add_discovery("security_headers", headers)
    result.add_discovery("robots", robots)
    result.add_discovery("sitemap", sitemap)
    result.add_discovery("technology", technology)
    result.add_discovery("waf", waf)
    result.add_discovery("cookies", cookies)

    # -------------------------
    # Reconnaissance Results
    # -------------------------

    result.result["reconnaissance"]["whois"] = whois
    result.result["reconnaissance"]["subdomains"] = subdomains
    result.result["reconnaissance"]["javascript"] = javascript
    result.result["reconnaissance"]["directories"] = directories
    result.result["reconnaissance"]["api"] = apis
    result.result["reconnaissance"]["ports"] = ports

    return result.get_result()