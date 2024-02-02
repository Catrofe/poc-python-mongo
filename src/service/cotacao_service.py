from src.domain.enums import Repository
from src.domain.models.entity import Cotacao
from src.domain.repository.repository_manager import RepositoryManager


class CotacaoService:

    def __init__(self, collection: Repository = Repository.COTACAO) -> None:
        self.collection = collection
        self._repository = RepositoryManager()

    async def iniciar_cotacao(self) -> Cotacao:
        cotacao = Cotacao()
        query = await self._repository.registrar_novo_documento(
            cotacao.model_dump(), self.collection, True
        )
        return Cotacao(**query)
