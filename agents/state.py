from typing import TypedDict, Dict

class WarehouseState(TypedDict):
    issues: Dict[str, int]
    run_id: str