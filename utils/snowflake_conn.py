import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE"),

        # 🔑 THIS IS THE IMPORTANT PART
        login_timeout=15,
        network_timeout=15,
        disable_ocsp_checks=True,
        client_session_keep_alive=False
    )