"""
Módulo principal de la aplicación.
Inicializa la APP, registra las rutas y el lifespan.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import include_routers
from src.config.settings import settings
from src.config.lifespan import lifespan

app = FastAPI(
    title="logs_system",
    version="1.0.0",
    debug=settings.DEBUG,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
)

include_routers(app)
