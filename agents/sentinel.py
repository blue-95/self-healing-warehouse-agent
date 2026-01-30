from utils.snowflake_conn import get_connection

def sentinel_node(state):
    print("🔍 Sentinel is auditing the warehouse...")

    conn = get_connection()
    cursor = conn.cursor()

    issues = {}

    cursor.execute("""
        SELECT COUNT(*) FROM SALES WHERE QUANTITY < 0
    """)
    issues["negative_quantity"] = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM SALES WHERE PRICE > 10000
    """)
    issues["extreme_price"] = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    print("✅ Audit Results:", issues)

    return {
        **state,
        "issues": issues
    }