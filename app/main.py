import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routers import router
from app.core.logger import setup_logging
from app.core.config import settings
from loguru import logger

os.makedirs("logs", exist_ok=True)
setup_logging()

app = FastAPI(title="Equilibrar Psicanálise")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)

logger.info("Aplicação Equilibrar Psicanálise inicializada com sucesso")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.server_port)