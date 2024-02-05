from fastapi import HTTPException

from src.domain.enums import RepositoryEnum
from src.domain.models.entity import Proponente
from src.domain.repository.repository_manager import RepositoryManager


class ProponenteService:

    def __init__(self, collection: RepositoryEnum = RepositoryEnum.PROPONENTE) -> None:
        self.collection = collection
        self._repository = RepositoryManager()

    async def registrar_proponente(self, proponente: Proponente) -> Proponente:
        query = await self._repository.registrar_novo_documento(
            proponente.model_dump(), self.collection, True
        )
        return Proponente(**query)

    async def buscar_proponente(self, localizador_cotacao: str) -> Proponente:
        query = await self._repository.buscar_um_documento(
            {"localizadorCotacao": localizador_cotacao}, self.collection
        )
        if not query:
            raise HTTPException(status_code=404, detail="Proponente não encontrado")
        return Proponente(**query)

    async def atualizar_proponente(self, proponente: Proponente) -> Proponente:
        query = await self._repository.atualizar_documento(
            proponente.model_dump(),
            self.collection,
            query={"localizadorCotacao": proponente.localizadorCotacao},
        )
        if not query:
            raise HTTPException(status_code=404, detail="Proponente não encontrado")
        return Proponente(**query)
