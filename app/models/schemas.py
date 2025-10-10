from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class ChatRequest(BaseModel):
    message: str = Field(..., description="Patient's symptom or concern")
    age: int = Field(..., ge=0, le=120, description="Patient's age")
    sex: str = Field(
        ...,
        pattern="^(male|female|other)$",
        description="Patient's sex (male/female/other)"
    )


class PrescriptionSuggestion(BaseModel):
    drug: str
    reason: str
    evidence: Optional[List[str]]
    clinician_required: bool = True

class ChatResponse(BaseModel):
    reply: str
    suggestions: List[PrescriptionSuggestion] = [] 