# agents/healer.py
from utils.snowflake_conn import get_connection
from agents.state import WarehouseState

def healer_node(state: WarehouseState) -> WarehouseState:
    """
    Execute SQL updates suggested by Strategist.
    """
    fixes = state.get("fixes", [])

    if not fixes:
        return state  # Nothing to fix

    session = get_connection()

    for fix in fixes:
        if fix["action"] == "update_quantity":
            sql = f"""
            UPDATE WAREHOUSE_INVENTORY
            SET QUANTITY = {fix['new_value']}
            WHERE {fix['condition']}
            """
            session.cursor().execute(sql)

        elif fix["action"] == "normalize_price":
            # For demo: cap extreme price to average
            sql = f"""
            UPDATE WAREHOUSE_INVENTORY
            SET PRICE = (
                SELECT AVG(PRICE) FROM WAREHOUSE_INVENTORY
            )
            WHERE {fix['condition']}
            """
            session.cursor().execute(sql)

    session.close()

    # Optional: mark issues as resolved for Sentinel loop
    state["issues"] = {}
    return state