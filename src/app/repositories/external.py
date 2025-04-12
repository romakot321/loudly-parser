from aiohttp import ClientSession, MultipartWriter
from loguru import logger

from app.db.tables import Account
from app.schemas.external import ExternalAccountLimitsSchema, ExternalAuthorizeRequestSchema, ExternalAuthorizeResponseSchema, ExternalGenerationRequest, ExternalGenerationSchema


class ExternalRepository:
    EXTERNAL_API_URL = "https://soundtracks.loudly.com"

    async def get_limits(self, account: Account) -> ExternalAccountLimitsSchema | None:
        async with ClientSession(base_url=self.EXTERNAL_API_URL, headers={"authorization": "Bearer " + account.access_token}) as session:
            resp = await session.get("/users/limits")
            if resp.status == 401:
                return None
            body = await resp.json()
            logger.debug("Limits response: " + str(body))
            return ExternalAccountLimitsSchema.model_validate(body)

    async def login_with_refresh_token(self, account: Account) -> ExternalAuthorizeResponseSchema:
        if account.refresh_token is None:
            raise ValueError("Account refresh token is None")
        body = ExternalAuthorizeRequestSchema(client_id=account.client_id, refresh_token=account.refresh_token)

        async with ClientSession(base_url=self.EXTERNAL_API_URL, headers={"authorization": "Bearer " + account.access_token, "Content-Type": "application/x-www-form-urlencoded"}) as session:
            resp = await session.post("/oauth/v2/token", data=body.to_params())
            if resp.status // 2 != 2:
                raise ValueError(await resp.text())
            body = await resp.json()
            logger.debug("Login response: " + str(body))
            return ExternalAuthorizeResponseSchema.model_validate(body)

    async def generate(self, schema: ExternalGenerationRequest, access_token: str) -> ExternalGenerationSchema:
        boundary = "------geckoformboundaryb02865f069a7e2e9c238355d71873c1c"
        logger.debug("Sending generate request: " + str(schema))
        with MultipartWriter('form-data', boundary) as mpwriter:
            for key, value in schema.model_dump(exclude_none=True).items():
                if isinstance(value, list):
                    key = key + "[]"
                    for i in value:
                        part = mpwriter.append(i, {'content-type': 'form-data'})
                        part.set_content_disposition('form-data', name=key)
                    continue
                part = mpwriter.append(str(value), {'content-type': 'form-data'})
                part.set_content_disposition('form-data', name=key)

            async with ClientSession(base_url=self.EXTERNAL_API_URL, headers={"authorization": "Bearer " + access_token, "Content-Type": "multipart/form-data; boundary=" + boundary}) as session:
                resp = await session.post("/ai/vega/bundles", data=mpwriter)
                if resp.status != 200:
                    raise ValueError("Status code: " + str(resp.status) + ", error: " + await resp.text())
                body = await resp.json()
                logger.debug("Generate response: " + str(body))
                return ExternalGenerationSchema.model_validate(body)

    async def get_generation(self, generation_id: str, access_token: str) -> ExternalGenerationSchema:
        async with ClientSession(base_url=self.EXTERNAL_API_URL, headers={"authorization": "Bearer " + access_token}) as session:
            resp = await session.get("/ai/vega/bundles/" + generation_id, params={"limit": 10})
            if resp.status != 200:
                raise ValueError("Status code: " + str(resp.status) + ", error: " + await resp.text())
            body = await resp.json()
            logger.debug("Get generation response: " + str(body))
            return ExternalGenerationSchema.model_validate(body)

