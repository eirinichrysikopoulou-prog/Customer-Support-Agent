

import graph
app= graph.build_graph()
result = app.invoke({
    "ticket": "I want to request a refund"
})


print(result)
print("Category:", result["category"])
print("Urgency:", result["urgency"])
print("Summary:", result["summary"])
print("Proposed_response:", result["proposed_response"])
print("FINAL RESULT:", result)
print("FINAL KEYS:", result.keys())


app.get_graph().draw_mermaid_png(
    output_file_path="graph.png"
)

