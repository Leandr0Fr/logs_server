"""
Módulo principal de la aplicación.
Inicializa la APP y registra las rutas.
"""

from fastapi import FastAPI
from src.routes import register_routes


def create_app() -> FastAPI:
    """
    Crea la aplicación FastAPI y registra las rutas.
    Returns:
        FastAPI: La instancia de la aplicación FastAPI.
    """
    app = FastAPI()
    register_routes(app)
    return app


app = create_app()
