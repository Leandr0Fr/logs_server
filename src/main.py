"""
Módulo principal de la aplicación.
Inicializa la APP, registra las rutas y el lifespan.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.routes import register_routes
from src.config.settings import settings
from src.database.engine import async_engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan de la base de datos"""
    yield
    await async_engine.dispose()


def create_app() -> FastAPI:
    """
    Crea la aplicación FastAPI y registra las rutas.
    Returns:
        FastAPI: La instancia de la aplicación FastAPI.
    """
    app_fastapi = FastAPI(
        title="logs_system",
        version="1.0.0",
        debug=settings.DEBUG,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        lifespan=lifespan,
    )
    register_routes(app_fastapi)
    return app_fastapi


app = create_app()
