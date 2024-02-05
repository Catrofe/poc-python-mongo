from fastapi import APIRouter

from src.domain.models.entity import Cotacao
from src.service.cotacao_service import CotacaoService

router = APIRouter()

service = CotacaoService()


@router.post("/emissao/cotacao", status_code=201, response_model=Cotacao)
async def iniciar_cotacao() -> Cotacao:
    """
    Endpoint responsável por iniciar uma nova cotação.
    """
    return await service.iniciar_cotacao()


@router.get(
    "/emissao/cotacao/{localizadorCotacao}", status_code=200, response_model=Cotacao
)
async def buscar_cotacao(localizadorCotacao: str) -> Cotacao:
    """
    Endpoint responsável por buscar uma cotação pelo id.
    """
    return await service.buscar_cotacao_completa(localizadorCotacao)
