from utils.snowflake_conn import get_connection
from agents.state import WarehouseState

def sentinel_node(state: WarehouseState) -> WarehouseState:
    print("🔍 Sentinel is auditing the warehouse...")

    conn = get_connection()
    cursor = conn.cursor()

    issues = {}

    # 1️⃣ Negative inventory check
    cursor.execute("""
        SELECT COUNT(*) 
        FROM WAREHOUSE_INVENTORY 
        WHERE QUANTITY < 0
    """)
    issues["negative_quantity"] = cursor.fetchone()[0]

    # 2️⃣ Extreme pricing check
    cursor.execute("""
        SELECT COUNT(*) 
        FROM WAREHOUSE_INVENTORY 
        WHERE PRICE > 10000
    """)
    issues["extreme_price"] = cursor.fetchone()[0]

    # 3️⃣ Missing critical fields
    cursor.execute("""
        SELECT COUNT(*) 
        FROM WAREHOUSE_INVENTORY 
        WHERE PRODUCT_NAME IS NULL
           OR CATEGORY IS NULL
    """)
    issues["missing_metadata"] = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    state["issues"] = issues
    return state