from fastapi import Depends

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

    async def authorize_accounts(self):
        accounts = await self.account_repository.list()
        for account in accounts:
            if (await self.external_repository.get_limits(account)) is not None:
                continue
            tokens = await self.external_repository.login_with_refresh_token(
                account
            )
            await self.account_repository.update(
                account.id,
                refresh_token=tokens.refresh_token,
                access_token=tokens.access_token,
            )

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
