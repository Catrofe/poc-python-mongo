from fastapi import HTTPException

from src.domain.enums import RepositoryEnum
from src.domain.models.entity import Beneficiario
from src.domain.repository.repository_manager import RepositoryManager


class BeneficiarioService:

    def __init__(
        self, collection: RepositoryEnum = RepositoryEnum.BENEFICIARIO
    ) -> None:
        self.collection = collection
        self._repository = RepositoryManager()

    async def registrar_beneficiario(self, beneficiario: Beneficiario) -> Beneficiario:
        query = await self._repository.registrar_novo_documento(
            beneficiario.model_dump(), self.collection, True
        )
        return Beneficiario(**query)

    async def buscar_beneficiario(self, localizador_cotacao: str) -> Beneficiario:
        query = await self._repository.buscar_um_documento(
            {"localizadorCotacao": localizador_cotacao}, self.collection
        )
        if not query:
            raise HTTPException(status_code=404, detail="Beneficiário não encontrado")
        return Beneficiario(**query)

    async def atualizar_beneficiario(self, beneficiario: Beneficiario) -> Beneficiario:
        query = await self._repository.atualizar_documento(
            beneficiario.model_dump(),
            self.collection,
            query={"localizadorCotacao": beneficiario.localizadorCotacao},
        )
        if not query:
            raise HTTPException(status_code=404, detail="Beneficiário não encontrado")
        return Beneficiario(**query)
