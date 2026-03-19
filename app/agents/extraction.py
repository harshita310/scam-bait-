import re
from app.agents.base import BaseAgent

class ExtractionAgent(BaseAgent):
    def process(self, text: str, state: dict) -> dict:
        entities = {}
        # Bad basic regex for emails: matching any string with an @
        emails = re.findall(r"\S+@\S+", text)
        if emails:
            entities["emails"] = emails
            
        phones = re.findall(r"\d{10}", text)
        if phones:
            entities["phone_numbers"] = phones
            
        return {"extractedIntelligence": entities}
