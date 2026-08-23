from state import AgentState

from state import AgentState
from RAG.ingest import create_rag_chain

technical_rag= create_rag_chain("technical")

def technical(state:AgentState)->dict:
    response = technical_rag.invoke(state["ticket"])

    result = {
        "proposed_response": response
    }

    return result


