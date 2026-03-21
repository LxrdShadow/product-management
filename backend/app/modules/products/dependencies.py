from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.products.repository import ProductRepository
from app.modules.products.service import ProductService
from db.session import get_async_session
from upload.local_storage import LocalStorage
from upload.storage import Storage


async def get_product_repository(
    session: AsyncSession = Depends(get_async_session),
) -> ProductRepository:
    return ProductRepository(session)


async def get_local_storage() -> Storage:
    return LocalStorage()


async def get_product_service(
    repo: ProductRepository = Depends(get_product_repository),
    storage: Storage = Depends(get_local_storage),
) -> ProductService:
    return ProductService(repo)
