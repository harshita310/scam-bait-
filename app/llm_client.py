import os
# import groq

class LLMClient:
    """Wrapper for Groq / Cerebras API calls."""
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY", "dummy")
        # self.client = groq.AsyncGroq(api_key=self.api_key)
        
    async def generate(self, prompt: str) -> str:
        # Mock response
        return "I am confused..."
