
from state import AgentState
from RAG.ingest import create_rag_chain


billing_rag= create_rag_chain("billing")

def billing(state:AgentState)->dict:

    response = billing_rag.invoke(state["ticket"])


    result = {
        "proposed_response": response
    }

    return result
