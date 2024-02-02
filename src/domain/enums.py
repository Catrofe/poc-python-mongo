import enum


class Repository(enum.Enum):
    OBJETO_SEGURADO = "objeto_segurado"
    COTACAO = "cotacao"
    PROPONENTE = "proponente"
    BENEFICIARIO = "beneficiario"


class SituacaoEnum(enum.Enum):
    EM_ANDAMENTO = {"nmSituacao": "Em andamento", "nrSituacao": 1}
    CANCELADA = {"nmSituacao": "Cancelada", "nrSituacao": 2}
    CONTRATADA = {"nmSituacao": "Contratada", "nrSituacao": 3}
