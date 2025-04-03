from fastapi import Response
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_service import BaseService as BaseRepository

from app.db.tables import Account, engine


class AccountRepository[Table: Account, int](BaseRepository):
    base_table = Account
    engine = engine
    session: AsyncSession
    response: Response

    async def create(self, **fields) -> Account:
        return await self._create(**fields)

    async def list(self, page=None, count=None) -> list[Account]:
        return list(await self._get_list(page=page, count=count))

    async def get(self, model_id: int) -> Account:
        return await self._get_one(
            id=model_id
        )

    async def update(self, model_id: int, **fields) -> Account:
        return await self._update(model_id, **fields)

    async def count(self):
        return await self._count()
