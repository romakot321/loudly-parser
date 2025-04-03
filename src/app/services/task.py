import asyncio
from uuid import UUID
from fastapi import Depends

from app.db.tables import Account, TaskItem
from app.repositories.external import ExternalRepository
from app.repositories.task import TaskRepository
from app.schemas.external import ExternalGenerationRequest
from app.schemas.task import (
    TaskCreateAdvancedSchema,
    TaskCreateTextSchema,
    TaskSchema,
)


class TaskService:
    def __init__(
        self,
        task_repository: TaskRepository = Depends(TaskRepository.depend),
        external_repository: ExternalRepository = Depends(),
    ):
        self.task_repository = task_repository
        self.external_repository = external_repository

    async def get(self, task_id: UUID) -> TaskSchema:
        model = await self.task_repository.get(task_id)
        return TaskSchema.model_validate(model)

    async def create(self, schema: TaskCreateAdvancedSchema | TaskCreateTextSchema, account: Account) -> TaskSchema:
        model = await self.task_repository.create(
            user_id=str(schema.user_id),
            app_bundle=schema.app_bundle,
            account_id=account.id,
        )
        await self.task_repository.refresh()
        return TaskSchema.model_validate(model.__dict__ | {"items": []})

    async def _send(self, task_id: UUID, request: ExternalGenerationRequest, account: Account):
        generation = await self.external_repository.generate(
            request, account.access_token
        )

        response = None
        for _ in range(12):
            external_task = await self.external_repository.get_generation(
                generation.id, account.access_token
            )
            if external_task.errors:
                return await self.task_repository.update(task_id, error=str(external_task.errors))
            if external_task.is_finished:
                response = external_task
                break
            await asyncio.sleep(5)

        if response is None:
            return await self.task_repository.update(task_id, error="Timeout")
        items = [
            TaskItem(
                task_id=task_id,
                external_id=song.id,
                title=song.title,
                music_url=song.music_file_path,
            )
            for song in response.vega_songs
        ]
        return await self.task_repository.create_items(*items)

    async def send_advanced(
        self, task_id: UUID, schema: TaskCreateAdvancedSchema, account: Account
    ):
        request = ExternalGenerationRequest.model_validate(
            schema.model_dump() | {"bundle_type": "ADVANCED"}
        )
        return await self._send(task_id, request, account)

    async def send_text(
        self, task_id: UUID, schema: TaskCreateTextSchema, account: Account
    ):
        request = ExternalGenerationRequest.model_validate(
            schema.model_dump() | {"bundle_type": "TEXT2MUSIC"}
        )
        return await self._send(task_id, request, account)
