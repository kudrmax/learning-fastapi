from fastapi import APIRouter, HTTPException, status

from . import crud
from .schemas import Product, ProductCreate

router = APIRouter(tags=["products"])


@router.get('/', response_model=list[Product])
async def get_products(session):
    return await crud.get_products(session=session)
