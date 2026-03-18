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
