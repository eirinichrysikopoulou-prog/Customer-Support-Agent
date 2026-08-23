from typing import Literal
from pydantic import BaseModel, Field

Category = Literal["technical", "billing", "general"]
Urgency = Literal["low", "medium", "high"]


class TicketClassification(BaseModel):
    category: Category
    urgency: Urgency
    summary: str

class ResponseEvaluation(BaseModel):
    confidence: float = Field(
        ge=0,
        le=1,
    )

    reason: str