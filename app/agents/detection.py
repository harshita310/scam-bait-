from app.agents.base import BaseAgent

class DetectionAgent(BaseAgent):
    def process(self, text: str, state: dict) -> dict:
        text_lower = text.lower()
        # Basic rule-based detection
        scam_keywords = ["lottery", "urgent", "police", "arrest", "bank account"]
        is_scam = any(kw in text_lower for kw in scam_keywords)
        
        return {
            "scamDetected": is_scam,
            "confidence": 0.8 if is_scam else 0.2
        }
