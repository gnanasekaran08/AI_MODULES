from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.mysql import Database
from app.services.qdrant_service import QdrantService
from app.services.training_service import TrainingService
from app.api.escalation_api import router
from app.utils.config import Config


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when the application starts.
    """

    Database.initialize()

    QdrantService.initialize()

    QdrantService.create_collection()

    TrainingService.initialize()

    yield

    # Future cleanup can be added here
    # Example:
    # Database.close_pool()


app = FastAPI(
    title=Config.API_TITLE,
    version=Config.API_VERSION,
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


@app.get("/")
def home():

    return {
        "application": Config.API_TITLE,
        "version": Config.API_VERSION,
        "status": "Running"
    }


@app.get("/health")
def health():

    return {
        "status": "UP",
        "mysql": "UP",
        "qdrant": "UP",
        "embedding_model": "UP"
    }