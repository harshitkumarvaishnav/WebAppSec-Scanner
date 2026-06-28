from fastapi import APIRouter
from pydantic import BaseModel

from backend.scanner.discovery.validator import validate_url
from backend.scanner.discovery.dns_lookup import get_dns_info

router = APIRouter()


class ScanRequest(BaseModel):
    url: str


@router.post("/validate")
def validate(scan: ScanRequest):
    valid, message = validate_url(scan.url)

    if not valid:
        return {
        "target": scan.url,
        "valid": False,
        "message": message
    }

    dns = get_dns_info(scan.url)

    return {
        "target": scan.url,
        "valid": True,
        "message": message,
        "dns": dns
    }