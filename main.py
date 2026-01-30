import uuid
from langgraph.graph import StateGraph, END

from agents.state import WarehouseState
from agents.sentinel import sentinel_node
from agents.strategist import strategist_node
from agents.healer import healer_node


graph = StateGraph(WarehouseState)

graph.add_node("sentinel", sentinel_node)
graph.add_node("strategist", strategist_node)
graph.add_node("healer", healer_node)

graph.set_entry_point("sentinel")

graph.add_edge("sentinel", "strategist")
graph.add_edge("strategist", "healer")
graph.add_edge("healer", END)

app = graph.compile()


if __name__ == "__main__":
    result = app.invoke({
        "issues": {},
        "fix_plan": {},
        "run_id": str(uuid.uuid4())
    })

    print("\n✅ Final Result")
    print(result)