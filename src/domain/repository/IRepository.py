from abc import ABC, abstractmethod
from typing import Any

from src.domain.enums import Repository
from src.infra.repository.RepositoryManager import RepositoryManager


class IRepository(ABC):

    def __init__(self) -> None:
        self.__repository = RepositoryManager()

    @abstractmethod
    async def registrar_novo_documento(
        self,
        documento: dict[str, Any],
        collection: Repository,
        return_object: bool = False,
    ) -> Any:
        row = await self.__repository.get_connection(collection).insert_one(documento)
        if return_object:
            return await self.__repository.get_connection(collection).find_one(
                {"_id": row.inserted_id}
            )

    async def registrar_novos_documentos(
        self,
        documentos: list[dict[str, Any]],
        collection: Repository,
        return_object: bool = False,
    ) -> Any:
        row = await self.__repository.get_connection(collection).insert_many(documentos)
        if return_object:
            return await self.__repository.get_connection(collection).find(
                {"_id": {"$in": row.inserted_ids}}
            )

    @abstractmethod
    async def atualizar_documento(
        self, documento: dict[str, Any], collection: Repository
    ) -> Any:
        return await self.__repository.get_connection(collection).find_one_and_update(
            {"_id": documento["_id"]}, {"$set": documento}
        )

    @abstractmethod
    async def buscar_um_documento(
        self, query: dict[str, Any], collection: Repository
    ) -> Any:
        return await self.__repository.get_connection(collection).find_one(query)

    @abstractmethod
    async def buscar_muitos_documentos(
        self, query: dict[str, Any], collection: Repository
    ) -> Any:
        return await self.__repository.get_connection(collection).find(query)

    @abstractmethod
    async def deletar_documento(
        self, documento: dict[str, Any], collection: Repository
    ) -> Any:
        return await self.__repository.get_connection(collection).delete_one(documento)
