import os
import logging
from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai

logger = logging.getLogger(__name__)

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.llm = None
        self.model_name = None
        self.initialize_llm()

    def initialize_llm(self):
        """Automatically pick the latest available Gemini model."""
        try:
            client = genai.Client(api_key=self.api_key)
            models = [m.name for m in client.models.list()]

            # Define priority order for choosing the most stable or latest model
            preferred_order = [
                "models/gemini-2.5-pro",
                "models/gemini-2.5-flash",
                "models/gemini-2.0-flash",
                "models/gemini-pro-latest",
                "models/gemini-flash-latest"
            ]

            # Pick the first available preferred model
            for name in preferred_order:
                if name in models:
                    self.model_name = name
                    break

            # If no preferred model found, fall back to any gemini model available
            if not self.model_name and models:
                self.model_name = next((m for m in models if "gemini" in m), models[0])

            if not self.model_name:
                raise RuntimeError("❌ No Gemini models available for your API key.")

            # Initialize model with temperature for balanced creativity
            self.llm = ChatGoogleGenerativeAI(
                model=self.model_name,
                temperature=0.7,
                google_api_key=self.api_key
            )
            logger.info(f"✅ Gemini LLM initialized with model: {self.model_name}")

        except Exception as e:
            logger.error(f"❌ Failed to initialize Gemini model: {e}")
            self.llm = None

    async def ask(self, prompt: str) -> str:
        if not self.llm:
            return "Sorry, AI model not initialized."
        try:
            response = await self.llm.ainvoke(prompt)
            return response.content.strip().replace("\n\n", "\n")
        except Exception as e:
            logger.error(f"❌ Gemini API Error: {e}")
            return "Sorry, could not process your request."
