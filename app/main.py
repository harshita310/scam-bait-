from app.agents.detection import DetectionAgent
from app.database import SessionManager

db_manager = SessionManager()
from app.models import HoneypotRequest, JudgeResponse, ResponseMeta

@app.post("/api/v1/honeypot")
async def honeypot_endpoint(request: HoneypotRequest):
    """Main honeypot endpoint stub."""
    # Load or initialize session
    session_state = db_manager.get_session(request.sessionId) or {}
    print(f"Loaded session for {request.sessionId}")


    try:
        # Placeholder for complex agent workflow
        detection_agent = DetectionAgent()
        det_result = detection_agent.process(request.message.text, session_state)
        session_state.update(det_result)
        reply = "Let me get my glasses..."
        status = "success"
    except Exception as e:
        reply = "I'm sorry, my phone is acting up."
        status = "error"
    return {"status": status, "reply": reply}

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

