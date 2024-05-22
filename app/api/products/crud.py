from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models import Product


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)  # типо SQL запрос
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)
