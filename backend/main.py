from fastapi import FastAPI
from backend.config.settings import SCANNER_NAME, VERSION

app = FastAPI(
    title=SCANNER_NAME,
    version=VERSION
)

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