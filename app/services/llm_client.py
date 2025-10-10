import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class LLMClient:
    def __init__(self):
        self.model = os.getenv("GOOGLE_GENAI_MODEL", "models/gemini-1.5-flash")
        self.api_key = os.getenv("GOOGLE_API_KEY")

        if not self.api_key:
            raise ValueError("❌ GOOGLE_API_KEY not found. Set it in your .env file.")

        

        try:
            self.llm = ChatGoogleGenerativeAI(
                model=self.model, 
                api_key=self.api_key,
                temperature=0.7 # Controls creativity
            )
            print(f"✅ Gemini LLM initialized with model: {self.model}")
        except Exception as e:
            print(f"❌ Error initializing LLM: {e}")
            self.llm = None

    async def ask(self, prompt: str) -> str:
        if not self.llm:
            return "Sorry, AI model not initialized."
        try:
            
            response = await self.llm.ainvoke(prompt)
            content = response.content if hasattr(response, "content") else str(response)

            # Clean up unnecessary whitespace, line breaks, and bullet artifacts
            clean_response = " ".join(content.split())
            return clean_response
            
        except Exception as e:
            print(f"❌ Gemini API Error: {e}")
            return "Sorry, could not process your request."
