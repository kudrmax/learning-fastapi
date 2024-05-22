from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models import Product

from .schemas import ProductCreate, ProductUpdate, ProductUpdatePartial


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)  # типо SQL запрос
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def update_product(
        session: AsyncSession,
        product: Product,
        product_update: ProductUpdate
) -> Product:
    for attr_name, new_val in product_update.model_dump().items():
        setattr(product, attr_name, new_val)  # product.'attr_name' = new_val
    await session.commit()
    return product


async def update_product_partial(
        session: AsyncSession,
        product: Product,
        product_update: ProductUpdatePartial
) -> Product:
    for attr_name, new_val in product_update.model_dump(exclude_unset=True).items():
        setattr(product, attr_name, new_val)  # product.'attr_name' = new_val
    await session.commit()
    return product
