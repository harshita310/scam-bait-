from app.agents.detection import DetectionAgent
from app.agents.extraction import ExtractionAgent

def run_honeypot_workflow(text: str, session_state: dict) -> dict:
    """Orchestrates the honeypot processing pipeline."""
    detection_agent = DetectionAgent()
    det_result = detection_agent.process(text, session_state)
    session_state.update(det_result)
    
    extraction_agent = ExtractionAgent()
    ext_result = extraction_agent.process(text, session_state)
    session_state.update(ext_result)
    
    return session_state
