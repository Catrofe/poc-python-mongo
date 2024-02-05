from fastapi import APIRouter

from src.domain.models.entity import Beneficiario
from src.service.beneficiario_service import BeneficiarioService

router = APIRouter()

service = BeneficiarioService()


@router.post("/emissao/beneficiario", status_code=201, response_model=Beneficiario)
async def registrar_beneficiario(beneficiario: Beneficiario) -> Beneficiario:
    """
    Endpoint responsável por registrar um novo beneficiário.
    """
    return await service.registrar_beneficiario(beneficiario)


@router.get("/emissao/beneficiario/{localizador_cotacao}", response_model=Beneficiario)
async def buscar_beneficiario(localizador_cotacao: str) -> Beneficiario:
    """
    Endpoint responsável por buscar um beneficiário.
    """
    return await service.buscar_beneficiario(localizador_cotacao)


@router.put("/emissao/beneficiario", response_model=Beneficiario)
async def atualizar_beneficiario(beneficiario: Beneficiario) -> Beneficiario:
    """
    Endpoint responsável por atualizar um beneficiário.
    """
    return await service.atualizar_beneficiario(beneficiario)
