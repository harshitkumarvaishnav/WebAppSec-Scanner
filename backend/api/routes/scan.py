from fastapi import APIRouter
from pydantic import BaseModel

from backend.core.scan_engine import start_scan

router = APIRouter()


class ScanRequest(BaseModel):
    url: str
    testing_type: str = "black_box"


@router.post("/validate")
def validate(scan: ScanRequest):

    return start_scan(scan)