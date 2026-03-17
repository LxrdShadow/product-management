from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.products.models import Product


class ProductRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def insert(self, product: dict[str, any]) -> Product:
        """Insert a product in the database."""
        stmt = insert(Product).values(product).returning(Product)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Product]:
        """Get all products in the database"""
        stmt = select(Product)
        result = await self.session.execute(stmt)
        return result.scalars()
