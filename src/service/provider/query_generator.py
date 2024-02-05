from typing import Any


class QueryGenerator:
    @staticmethod
    async def query_buscar_cotacao_completa(
        localizador_cotacao: str,
    ) -> list[dict[str, Any]]:
        return [
            {"$match": {"localizadorCotacao": localizador_cotacao}},
            {
                "$lookup": {
                    "from": "proponente",
                    "localField": "localizadorCotacao",
                    "foreignField": "localizadorCotacao",
                    "as": "lsProponente",
                }
            },
        ]
