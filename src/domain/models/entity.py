from typing import Optional

from pydantic import BaseModel


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
    localizadorCotacao: str
    email: str
    endereco: Endereco
    telefone: str
    nmCpfCnpj: str
    nmNome: str
    pessoaFisica: bool


class Cotacao(BaseModel):
    localizadorCotacao: str
    nrVersao: str
    dtCotacao: str
    lsObjetoSegurado: Optional[list[dict[str, str]]]
    lsProponente: Optional[list[Proponente]]
    lsBeneficiario: Optional[list[Beneficiario]]
    situacao: Situacao
