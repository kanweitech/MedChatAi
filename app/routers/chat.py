from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.llm_client import LLMClient
from app.services.prescriber import Prescriber
import re

router = APIRouter()

# Initialize AI and prescriber services
llm_client = LLMClient()
prescriber = Prescriber()

def clean_ai_text(text: str) -> str:
    """Remove Markdown symbols and excess newlines for clean JSON output."""
    if not text:
        return ""
    
    # Remove markdown symbols
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # remove bold markdown
    text = re.sub(r'[_`#>-]', '', text)           # strip other markdown chars
    
    # Replace multiple newlines with two (paragraph spacing)
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    
    # Replace remaining single newlines with spaces (for wrapped lines)
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    
    # Remove excessive spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Restore paragraph spacing (convert double spaces back to double newlines)
    text = re.sub(r'(\.\s)', r'\1\n\n', text)
    
    return text.strip()

@router.post("/chat/")
async def chat_with_patient(request: ChatRequest):
    """
    Chat endpoint where the AI interacts with the patient,
    understands symptoms, and the prescriber suggests medication.
    """
    # Step 1: Build a clinical-style AI prompt
    user_prompt = (
        f"Patient info: age={request.age}, sex={request.sex}. "
        f"Symptoms: {request.message}. "
        "Provide a short and clear medical assessment with possible diagnosis."
    )

    # Step 2: Ask the Gemini AI model
    ai_reply = await llm_client.ask(user_prompt)

    # Step 3: Clean the AI reply
    cleaned_reply = clean_ai_text(ai_reply)

    # Step 4: Let the prescriber recommend a drug (rule-based or AI-assisted)
    medication_suggestion = prescriber.recommend(request.message)

    # Step 5: Return combined response
    return {
        "ai_analysis": cleaned_reply,
        "prescribed_medication": medication_suggestion,
    }
