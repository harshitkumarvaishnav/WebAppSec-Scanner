"""
Module Name: sitemap.py

Purpose:
Discover sitemap.xml or sitemap_index.xml
and extract useful URLs for further scanning.
"""

import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlparse


def get_sitemap(target: str):

    try:

        parsed = urlparse(target)

        base_url = f"{parsed.scheme}://{parsed.netloc}"

        sitemap_locations = [
            "/sitemap.xml",
            "/sitemap_index.xml"
        ]

        for location in sitemap_locations:

            sitemap_url = base_url + location

            response = requests.get(
                sitemap_url,
                timeout=10,
                headers={
                    "User-Agent": "WebAppSec-Scanner"
                }
            )

            if response.status_code != 200:
                continue

            root = ET.fromstring(response.content)

            namespace = {
                "sm": "http://www.sitemaps.org/schemas/sitemap/0.9"
            }

            urls = []

            for url in root.findall(".//sm:loc", namespace):

                urls.append(url.text)

            return {
                "found": True,
                "url": sitemap_url,
                "total_urls": len(urls),
                "sample_urls": urls[:10]
            }

        return {
            "found": False
        }

    except Exception as e:

        return {
            "found": False,
            "error": str(e)
        }