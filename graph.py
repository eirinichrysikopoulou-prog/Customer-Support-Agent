
from langgraph.graph import StateGraph, START, END
from nodes.billing import billing
from nodes.technical import technical
from nodes.general import general
from state import AgentState
from nodes.classification import ticket_classification
from routing.route_ticket import route_ticket
from routing.route_after_evaluation import route_after_evaluation
from nodes.evaluate import evaluate_response
from nodes.resolve import *

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("classification",ticket_classification)
    graph.set_entry_point("classification")

    graph.add_node("router",lambda state:state) #passthrough function
    graph.add_edge("classification","router")
    graph.add_node("billing", billing)
    graph.add_node("technical",technical)
    graph.add_node("general",general)
    graph.add_conditional_edges(
        "router",
        route_ticket,
        {
            "Route to Billing":"billing",
            "Route to Technical": "technical",
            "Route to General": "general",
        }

    )
    graph.add_node("evaluation", evaluate_response)
    graph.add_node("resolve",resolve)
    graph.add_node("human_review",human_review)

    graph.add_edge("billing", "evaluation")
    graph.add_edge("technical", "evaluation")
    graph.add_edge("general", "evaluation")

    graph.add_conditional_edges(
        "evaluation",
        route_after_evaluation,
        {
            "resolve": "resolve",
            "human_review": "human_review"
        }
    )
    graph.add_edge("resolve", END)
    graph.add_edge("human_review", END)


    return graph.compile()

