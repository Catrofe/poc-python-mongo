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
