from fastapi import FastAPI

app = FastAPI(title="WebAppSec Scanner")

@app.get("/")
def home():
    return {
        "message": "WebAppSec Scanner API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
