import uuid
from langgraph.graph import StateGraph, END

from agents.state import AgentState
from agents.sentinel import sentinel_node
from agents.strategist import strategist_node
from agents.healer import healer_node

def should_continue(state):
    total_issues = sum(state["issues"].values())
    if total_issues == 0:
        print("No issues left. Ending workflow.")
        return "end"
    return "continue"

builder = StateGraph(AgentState)

builder.add_node("sentinel", sentinel_node)
builder.add_node("strategist", strategist_node)
builder.add_node("healer", healer_node)

builder.set_entry_point("sentinel")

builder.add_edge("strategist", "healer")
builder.add_edge("healer", "sentinel")

builder.add_conditional_edges(
    "sentinel",
    should_continue,
    {
        "continue": "strategist",
        "end": END
    }
)

graph = builder.compile()

if __name__ == "__main__":
    graph.invoke({
        "issues": {},
        "run_id": str(uuid.uuid4())
    })