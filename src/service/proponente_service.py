from src.domain.enums import Repository
from src.domain.models.entity import Proponente
from src.domain.repository.repository_manager import RepositoryManager


class ProponenteService:

    def __init__(self, collection: Repository = Repository.PROPONENTE) -> None:
        self.collection = collection
        self._repository = RepositoryManager()

    async def registrar_proponente(self, proponente: Proponente) -> Proponente:
        query = await self._repository.registrar_novo_documento(
            proponente.model_dump(), self.collection, True
        )
        return Proponente(**query)
