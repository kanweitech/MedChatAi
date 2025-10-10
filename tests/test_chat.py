import asyncio
from app.services.llm_client import LLMClient

async def test():
    llm = LLMClient()
    resp = await llm.ask("Hello, Gemini. How are you today?")
    print(resp)

asyncio.run(test())
