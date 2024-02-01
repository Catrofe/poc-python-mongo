import os
from typing import Any

import motor.motor_asyncio

from src.domain.enums import Repository


class RepositoryManager:
    def __init__(self) -> None:
        self.client: Any = motor.motor_asyncio.AsyncIOMotorClient(
            os.environ["MONGODB_URL"]
        )
        self._db_connection = self.client["ultron.cotacao"]

    def get_connection(self, repository: Repository) -> Any:
        return self._db_connection.get_collection(repository.value)
