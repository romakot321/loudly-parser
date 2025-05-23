from fastapi import Depends
import asyncio
from loguru import logger

from app.db.tables import Account
from app.repositories.account import AccountRepository
from app.repositories.external import ExternalRepository


class AccountService:
    def __init__(
        self,
        account_repository: AccountRepository = Depends(AccountRepository.depend),
        external_repository: ExternalRepository = Depends(ExternalRepository),
    ):
        self.account_repository = account_repository
        self.external_repository = external_repository

    async def authorize_accounts(self) -> list[Account]:
        accounts = await self.account_repository.list()
        authorized_accounts = []
        for account in accounts:
            if (await self.external_repository.get_limits(account)) is not None:
                continue
            for attempt in range(3):
                try:
                    tokens = await self.external_repository.login_with_refresh_token(
                        account
                    )
                except ValueError as e:
                    tokens = await self.external_repository.login_with_password(account)
            authorized_account = await self.account_repository.update(
                account.id,
                refresh_token=tokens.refresh_token,
                access_token=tokens.access_token,
            )
            authorized_accounts.append(authorized_account)
        return authorized_accounts

    @classmethod
    async def get_available_account(
        cls, account_repository: AccountRepository = Depends(AccountRepository.depend)
    ) -> Account:
        return (await account_repository.list())[0]

    async def __aenter__(self):
        self.account_repository = await AccountRepository().__aenter__()
        self.external_repository = ExternalRepository()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.account_repository.__aexit__(*args, **kwargs)
