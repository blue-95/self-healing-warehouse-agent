from utils.snowflake_conn import get_connection

def sentinel_node(state):
    print("🔍 Sentinel is auditing the warehouse...")

    # Get Snowflake connection
    conn = get_connection()
    cursor = conn.cursor()

    issues = {}

    # 1️⃣ Negative quantity check
    cursor.execute("""
        SELECT COUNT(*) 
        FROM AGENTIC_WAREHOUSE_DB.PUBLIC.WAREHOUSE_INVENTORY
        WHERE QUANTITY < 0
    """)
    issues["negative_quantity"] = cursor.fetchone()[0]

    # 2️⃣ Extreme price check (adjusted to your table)
    cursor.execute("""
        SELECT COUNT(*) 
        FROM AGENTIC_WAREHOUSE_DB.PUBLIC.WAREHOUSE_INVENTORY
        WHERE PRICE > 10000
    """)
    issues["extreme_price"] = cursor.fetchone()[0]

    # 3️⃣ Optional: Missing metadata check (if you want)
    cursor.execute("""
        SELECT COUNT(*) 
        FROM AGENTIC_WAREHOUSE_DB.PUBLIC.WAREHOUSE_INVENTORY
        WHERE PRODUCT_NAME IS NULL OR CATEGORY IS NULL
    """)
    issues["missing_metadata"] = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    print("✅ Audit Results:", issues)

    return {
        **state,
        "issues": issues
    }