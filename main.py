import uuid
from langgraph.graph import StateGraph, END
from agents.state import WarehouseState
from agents.sentinel import sentinel_node

def build_graph():
    graph = StateGraph(WarehouseState)

    graph.add_node("sentinel", sentinel_node)
    graph.set_entry_point("sentinel")
    graph.add_edge("sentinel", END)

    return graph.compile()

if __name__ == "__main__":
    graph = build_graph()

    result = graph.invoke({
        "issues": {},
        "run_id": str(uuid.uuid4())
    })

    print("\n✅ Audit Results")
    for k, v in result["issues"].items():
        print(f" - {k}: {v}")