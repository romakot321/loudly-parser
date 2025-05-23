from fastapi import FastAPI
from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi_utils.tasks import repeat_every
from pydantic_settings import BaseSettings
from loguru import logger
from contextlib import asynccontextmanager

from app.db.admin import attach_admin_panel
from app.services.account import AccountService


class ProjectSettings(BaseSettings):
    LOCAL_MODE: bool = False


def register_exception(application):
    @application.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
        # or logger.error(f'{exc}')
        logger.debug(f'{exc}')
        content = {'status_code': 422, 'message': exc_str, 'data': None}
        return JSONResponse(
            content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    application.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


def register_cors(application):
    application.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


@repeat_every(seconds=3000, wait_first=1, raise_exceptions=True)
async def relogin_accounts():
    async with AccountService() as account_service:
        await account_service.authorize_accounts()


async def lifespan(app: FastAPI):
    await relogin_accounts()
    yield


def init_web_application():
    project_settings = ProjectSettings()
    application = FastAPI(
        title="Task api",
        openapi_url='/openapi.json',
        docs_url='/docs',
        redoc_url='/redoc',
        lifespan=lifespan
    )

    if project_settings.LOCAL_MODE:
        register_exception(application)
        register_cors(application)

    from app.routes.task import router as task_router
    from app.routes.web import router as web_router

    application.include_router(task_router)
    application.include_router(web_router)
    # application.mount("/static", StaticFiles(directory="static"), name="static")

    attach_admin_panel(application)

    return application


def run() -> FastAPI:
    application = init_web_application()
    return application


fastapi_app = run()
