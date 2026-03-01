"""
Módulo principal de la aplicación.
Inicializa la APP y registra las rutas.
"""

from fastapi import FastAPI
from src.routes import register_routes
from src.config.settings import settings


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
    )
    register_routes(app_fastapi)
    return app_fastapi


app = create_app()
