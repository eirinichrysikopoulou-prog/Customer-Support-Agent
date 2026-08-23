from state import AgentState
from RAG.ingest import create_rag_chain

general_rag = create_rag_chain("general")


def general(state: AgentState) -> dict:
    response = general_rag.invoke(state["ticket"])

    result = {
        "proposed_response": response
    }

    return result


