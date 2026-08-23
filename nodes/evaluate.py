
from llm import llm
from schemas import ResponseEvaluation
from state import AgentState


evaluator = llm.with_structured_output(
    ResponseEvaluation
)

def evaluate_response(state: AgentState) -> dict:
    print("\n=== EVALUATION NODE EXECUTED ===")
    print("State entering evaluation:", state)

    result = evaluator.invoke(
        f"""
Evaluate this customer support response.

Customer question:
{state["ticket"]}

Proposed response:
{state["proposed_response"]}

Return:
- confidence between 0 and 1
- a short reason
"""
    )

    print("Evaluator output:", result)

    update = {
        "confidence": result.confidence,
        "evaluation_reason": result.reason
    }

    print("Evaluation returning:", update)

    return update