from typing import Any

import motor.motor_asyncio

from src.domain.enums import RepositoryEnum
from src.infra.settings import Settings

settings = Settings()  # type: ignore


class RepositoryBase:
    def __init__(self) -> None:
        self.client: Any = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
        self._db_connection = self.client["cotacao"]

    def get_connection(self, repository: RepositoryEnum) -> Any:
        return self._db_connection.get_collection(repository.value)

    async def get_async_collection(self, repository: RepositoryEnum) -> Any:
        return motor.motor_asyncio.AsyncIOMotorCollection(
            self._db_connection, repository.value
        )
