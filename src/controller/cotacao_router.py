from fastapi import APIRouter

from src.domain.models.entity import Cotacao, Proponente
from src.service.cotacao_service import CotacaoService
from src.service.proponente_service import ProponenteService

router = APIRouter()

cotacao_service = CotacaoService()
proponente_service = ProponenteService()


@router.post("/emissao/cotacao", status_code=201, response_model=Cotacao)
async def iniciar_cotacao() -> Cotacao:
    """
    Endpoint responsável por iniciar uma nova cotação.
    """
    return await cotacao_service.iniciar_cotacao()


@router.post("/emissao/proponente", status_code=201, response_model=Proponente)
async def registrar_proponente(proponente: Proponente) -> Proponente:
    """
    Endpoint responsável por registrar um novo proponente.
    """
    return await proponente_service.registrar_proponente(proponente)
