from state import AgentState

def resolve(state: AgentState) -> dict:
    return {
        "final_response": state["proposed_response"]
    }


def human_review(state: AgentState) -> dict:
    # We'll replace this later with interrupt()
    return {}