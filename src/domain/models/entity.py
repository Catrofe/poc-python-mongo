import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, Field

from src.domain.enums import SituacaoEnum


class Situacao(BaseModel):
    nmSituacao: str
    nrSituacao: int


class Endereco(BaseModel):
    cep: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    uf: str


class Beneficiario(BaseModel):
    localizadorCotacao: str
    email: str
    endereco: Endereco
    telefone: str
    nmCpfCnpj: str
    nmNome: str
    pessoaFisica: bool


class Proponente(BaseModel):
    localizadorCotacao: str = Field(exclude=True)
    email: str
    endereco: Endereco
    telefone: str
    nmCpfCnpj: str
    nmNome: str
    pessoaFisica: bool


class Cotacao(BaseModel):
    localizadorCotacao: str = str(uuid.uuid4())
    nrVersao: int = 1
    dtCotacao: str = str(datetime.datetime.now())
    lsObjetoSegurado: Optional[list[dict[str, str]]] = None
    lsProponente: Optional[list[Proponente]] = None
    lsBeneficiario: Optional[list[Beneficiario]] = None
    situacao: Situacao = Situacao(**SituacaoEnum.EM_ANDAMENTO.value)  # type: ignore
