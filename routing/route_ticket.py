from nodes import classification
from state import AgentState


def route_ticket(state: AgentState) -> str:

    if state["category"] == "billing":
        return "Route to Billing"

    if state["category"] == "technical":
        return "Route to Technical"

    return "Route to General"





