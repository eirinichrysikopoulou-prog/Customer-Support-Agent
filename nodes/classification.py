from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from state import AgentState
from schemas import TicketClassification
from llm import llm


parser = JsonOutputParser(
    pydantic_object=TicketClassification
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a customer support ticket classifier.

Classify every ticket into exactly one category:

technical:
- bugs
- application errors
- login failures
- API failures
- integration problems
- product malfunction

BillingFiles:
- payments
- charges
- invoices
- refunds
- subscription BillingFiles
- pricing issues

general:
- product questions
- how-to questions
- account questions
- requests that do not belong to technical or BillingFiles

Urgency:

high:
- service completely unusable
- security problem
- data loss
- severe business impact

medium:
- important problem requiring attention
- repeated technical problem
- incorrect BillingFiles or charge

low:
- general question
- informational request
- minor inconvenience

Create a concise one-sentence summary.

{format_instructions}
"""
    ),
    (
        "human",
        "Ticket: {ticket}"
    )
])


chain = prompt | llm | parser


def ticket_classification(state: AgentState) -> dict:
    result = chain.invoke({
        "ticket": state["ticket"],
        "format_instructions":
            parser.get_format_instructions(),
    })

    return {
        "category": result["category"],
        "urgency": result["urgency"],
        "summary": result["summary"],
    }