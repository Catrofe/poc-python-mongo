from fastapi import APIRouter

from src.domain.models.entity import Proponente
from src.service.proponente_service import ProponenteService

router = APIRouter()

service = ProponenteService()


@router.post("/emissao/proponente", status_code=201, response_model=Proponente)
async def registrar_proponente(proponente: Proponente) -> Proponente:
    """
    Endpoint responsável por registrar um novo proponente.
    """
    return await service.registrar_proponente(proponente)


@router.get("/emissao/proponente/{localizador_cotacao}", response_model=Proponente)
async def buscar_proponente(localizador_cotacao: str) -> Proponente:
    """
    Endpoint responsável por buscar um proponente.
    """
    return await service.buscar_proponente(localizador_cotacao)


@router.put("/emissao/proponente", response_model=Proponente)
async def atualizar_proponente(proponente: Proponente) -> Proponente:
    """
    Endpoint responsável por atualizar um proponente.
    """
    return await service.atualizar_proponente(proponente)
