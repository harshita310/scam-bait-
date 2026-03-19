import re
from app.agents.base import BaseAgent

class ExtractionAgent(BaseAgent):
    def process(self, text: str, state: dict) -> dict:
        entities = {}
        # Fixed regex for emails
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
        if emails:
            entities["emails"] = emails
            
        phones = re.findall(r"\d{10}", text)
        if phones:
            entities["phone_numbers"] = phones
            
        return {"extractedIntelligence": entities}
