from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import db_helper
from . import crud
from .dependencies import get_product_by_id
from .schemas import Product, ProductCreate, ProductUpdate

router = APIRouter(tags=["products"])


@router.get('/', response_model=list[Product])
async def get_products(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_products(session=session)


@router.post('/', response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
        product_in: ProductCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get('/{product_id}', response_model=Product)
async def get_product(
        product: Product = Depends(get_product_by_id),
        # @todo почему мы используем dependencies, чем это лучше просто функции, что это за паттер и т.д.?
):
    """
    Раньше было так:
    async def get_product(
        product_id: int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ):
        product = await crud.get_product(session=session, product_id=product_id)
        if product:
            return product
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found",
        )
    """
    return product


@router.put('/{product_id}')
async def update_product(
        product_update: ProductUpdate,
        is_partial: bool = False,
        product: Product = Depends(get_product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(session=session, product=product, product_update=product_update, is_partial=is_partial)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product: Product = Depends(get_product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_product(session=session, product=product)
