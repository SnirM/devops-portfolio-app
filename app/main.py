from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="DevOps Portfolio App", version="1.0.0")

@app.get("/")
def root():
    return {
        "message": "DevOps Portfolio App running on GKE 🚀",
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
