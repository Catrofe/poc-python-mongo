from typing import Any, Optional

from pymongo.collection import ReturnDocument

from src.domain.enums import RepositoryEnum
from src.infra.repository.repository_base import RepositoryBase


class RepositoryManagerMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs) -> Any:  # type: ignore
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class RepositoryManager(metaclass=RepositoryManagerMeta):

    def __init__(self) -> None:
        self.__repository = RepositoryBase()

    async def registrar_novo_documento(
        self,
        documento: dict[str, Any],
        collection: RepositoryEnum,
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
        collection: RepositoryEnum,
        return_object: bool = False,
    ) -> Any:
        row = await self.__repository.get_connection(collection).insert_many(documentos)
        if return_object:
            return await self.__repository.get_connection(collection).find(
                {"_id": {"$in": row.inserted_ids}}
            )

    async def atualizar_documento(
        self,
        documento: dict[str, Any],
        collection: RepositoryEnum,
        doc_atualizado: bool = True,
        query: Optional[dict[str, Any]] = None,
    ) -> Any:
        doc_return = ReturnDocument.AFTER if doc_atualizado else ReturnDocument.BEFORE
        if query:
            return await self.__repository.get_connection(
                collection
            ).find_one_and_update(
                query, {"$set": documento}, return_document=doc_return
            )
        return await self.__repository.get_connection(collection).find_one_and_update(
            {"_id": documento["_id"]}, {"$set": documento}, return_document=doc_return
        )

    async def buscar_um_documento(
        self,
        query: dict[str, Any] | list[dict[str, dict[str, str]]],
        collection: RepositoryEnum,
    ) -> Any:
        return await self.__repository.get_connection(collection).find_one(query)

    async def buscar_muitos_documentos(
        self, query: dict[str, Any], collection: RepositoryEnum
    ) -> Any:
        return (
            await self.__repository.get_connection(collection).find(query).to_list(1000)
        )

    async def deletar_documento(
        self, documento: dict[str, Any], collection: RepositoryEnum
    ) -> Any:
        return await self.__repository.get_connection(collection).delete_one(documento)

    async def buscar_com_agregacao(
        self, query: list[dict[str, Any]], collection: RepositoryEnum, limit: int = 1
    ) -> Any:
        conexao = await self.__repository.get_async_collection(collection)
        return await conexao.aggregate(query).to_list(limit)
