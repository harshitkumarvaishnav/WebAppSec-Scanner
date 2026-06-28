from fastapi import APIRouter
from pydantic import BaseModel

from backend.scanner.discovery.validator import validate_url

router = APIRouter()


class ScanRequest(BaseModel):
    url: str


@router.post("/validate")
def validate(scan: ScanRequest):

    valid, message = validate_url(scan.url)

    return {
        "target": scan.url,
        "valid": valid,
        "message": message
    }