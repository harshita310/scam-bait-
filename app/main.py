from app.database import SessionManager

db_manager = SessionManager()
from app.models import HoneypotRequest, JudgeResponse, ResponseMeta

@app.post("/api/v1/honeypot")
async def honeypot_endpoint(request: HoneypotRequest):
    """Main honeypot endpoint stub."""
    # Load or initialize session
    session_state = db_manager.get_session(request.sessionId) or {}
    print(f"Loaded session for {request.sessionId}")

    return {"status": "success", "reply": "Test reply"}

from fastapi import FastAPI

app = FastAPI(
    title="ScamBait AI - Honeypot Scam Detection",
    version="1.0.0",
    description="Active defense system that engages scammers and extracts forensic intelligence"
)

@app.get("/")
async def root():
    return {"status": "online"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

