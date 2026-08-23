from typing import TypedDict
from schemas import Category, Urgency

class AgentState(TypedDict, total=False):
    ticket: str
    category: Category
    urgency: Urgency
    summary: str
    proposed_response: str

    confidence: float
    evaluation_reason: str

    final_response: str
