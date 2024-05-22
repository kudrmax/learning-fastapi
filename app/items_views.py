from _pytest.nodes import Item
from fastapi import APIRouter, Path
from typing import Annotated

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/admin")
def get_admin_items():
    return {"items": -1}


@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    return {"best_name": "Max", "item_id": item_id}
