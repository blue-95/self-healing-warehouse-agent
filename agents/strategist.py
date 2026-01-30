from agents.state import WarehouseState

def strategist_node(state: WarehouseState) -> WarehouseState:
    """
    Decide how to heal detected data issues.
    No external clients initialized at import time.
    """
    issues = state.get("issues", {})
    fixes = []

    if issues.get("negative_quantity", 0) > 0:
        fixes.append({
            "action": "update_quantity",
            "condition": "QUANTITY < 0",
            "new_value": 0
        })

    if issues.get("extreme_price", 0) > 0:
        fixes.append({
            "action": "normalize_price",
            "condition": "PRICE > 10000"
        })

    state["fixes"] = fixes
    return state