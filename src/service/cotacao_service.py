from src.domain.enums import Repository
from src.domain.models.entity import Cotacao
from src.domain.repository.repository_manager import RepositoryManager
from src.service.provider.query_generator import QueryGenerator


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

    async def buscar_cotacao_completa(self, localizador_cotacao: str) -> Cotacao:
        query = await QueryGenerator.query_buscar_cotacao_completa(localizador_cotacao)
        consulta = await self._repository.buscar_com_agregacao(query, self.collection)
        return Cotacao(**consulta[0])
