from fastapi import FastAPI

from backend.config.settings import SCANNER_NAME, VERSION
from backend.api.routes.scan import router as scan_router

app = FastAPI(
    title=SCANNER_NAME,
    version=VERSION
)

app.include_router(scan_router)


@app.get("/")
def home():
    return {
        "message": f"{SCANNER_NAME} is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }