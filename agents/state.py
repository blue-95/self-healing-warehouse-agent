from typing import TypedDict, Dict, Any

class WarehouseState(TypedDict):
    issues: Dict[str, int]
    fix_plan: Dict[str, Any]
    run_id: str    