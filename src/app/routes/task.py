from fastapi import APIRouter, BackgroundTasks, Depends
from uuid import UUID

from app.db.tables import Account
from app.schemas.task import TaskCreateAdvancedSchema, TaskCreateTextSchema, TaskSchema
from app.services.account import AccountService
from app.services.task import TaskService
from . import validate_api_token

router = APIRouter(prefix="/api/task", tags=["Task"])


@router.post("/advanced", response_model=TaskSchema, dependencies=[Depends(validate_api_token)])
async def create_task_advanced(
    schema: TaskCreateAdvancedSchema,
    background_tasks: BackgroundTasks,
    service: TaskService = Depends(),
    account: Account = Depends(AccountService.get_available_account)
):
    """Generate with specified style"""
    task = await service.create(schema, account)
    background_tasks.add_task(service.send_advanced, task.id, schema, account)
    return task


@router.post("/text", response_model=TaskSchema, dependencies=[Depends(validate_api_token)])
async def create_task_text(
    schema: TaskCreateTextSchema,
    background_tasks: BackgroundTasks,
    service: TaskService = Depends(),
    account: Account = Depends(AccountService.get_available_account)
):
    """Generate from text"""
    task = await service.create(schema, account)
    background_tasks.add_task(service.send_text, task.id, schema, account)
    return task


@router.get("/{task_id}", response_model=TaskSchema, dependencies=[Depends(validate_api_token)])
async def get_task(task_id: UUID, service: TaskService = Depends()):
    return await service.get(task_id)

