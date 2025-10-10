from app.services.llm_client import LLMClient

class Prescriber:
    """AI-assisted medical prescription system using Gemini."""

    def __init__(self):
        self.llm_client = LLMClient()

    async def recommend(self, symptoms: str, age: int = None, sex: str = None) -> str:
        """
        Recommend medication based on symptoms, with Gemini reasoning.
        """
        # Base fallback for known symptoms (fast rule-based)
        text = symptoms.lower()
        if "headache" in text:
            base_recommendation = "Paracetamol 500mg every 6 hours as needed for pain."
        elif "fever" in text:
            base_recommendation = "Ibuprofen 400mg or Acetaminophen 500mg to reduce fever."
        elif "cough" in text:
            base_recommendation = "Dextromethorphan cough syrup or warm honey lemon tea."
        elif "sore throat" in text:
            base_recommendation = "Warm saline gargle and lozenges; if bacterial, amoxicillin 500mg."
        elif "stomach" in text or "nausea" in text:
            base_recommendation = "Oral rehydration salts and light diet; use an antacid if needed."
        else:
            base_recommendation = "No clear rule-based match. Let's ask AI for further analysis."

        # Now engage Gemini to refine the recommendation
        ai_prompt = f"""
        You are a certified medical assistant AI.
        Patient details: age={age}, sex={sex}.
        Symptoms: {symptoms}.
        Suggest an appropriate over-the-counter medication or first aid treatment.
        Avoid antibiotics unless clearly justified.
        Respond concisely and safely.
        """

        ai_response = await self.llm_client.ask(ai_prompt)

        # Clean & combine
        return f"{base_recommendation} AI Suggestion: {ai_response}"
