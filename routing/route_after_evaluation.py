from state import AgentState

def route_after_evaluation(state: AgentState) -> str:

    if state["confidence"] >= 0.75:
        return "resolve"

    return "human_review"