import logging

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.controller.beneficiario_router import router as beneficiario_router
from src.controller.cotacao_router import router as cotacao_router
from src.controller.proponente_router import router as proponente_router

app = FastAPI()

BASE_PATH = "/api"


@app.on_event("startup")
async def startup_event() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:     %(message)s - DateTime: %(asctime)s",
    )
    logging.info("Starting database connection")


@app.get("/")
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")


@app.get("/health", status_code=204)
async def health() -> None:
    logging.info("Health check")


app.include_router(cotacao_router, prefix=BASE_PATH, tags=["Cotacao"])
app.include_router(proponente_router, prefix=BASE_PATH, tags=["Proponente"])
app.include_router(beneficiario_router, prefix=BASE_PATH, tags=["Beneficiario"])
