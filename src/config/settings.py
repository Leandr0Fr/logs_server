"""
Modulo de configuración con Pydantic.
"""

import logging
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SRC_DIR = BASE_DIR / "src"

LOG_FILE = BASE_DIR / "logs" / "app.log"

# Crear el directorio 'logs' si no existe
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


# Configuración logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE, encoding="utf-8")],
)

# Se genera el logger para que tome la configuración
logger = logging.getLogger(__name__)

# Configurar logger de SQLAlchemy para evitar ruido
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
logging.getLogger("sqlalchemy.pool").setLevel(logging.WARNING)


class Settings(BaseSettings):
    """Clase de configuración para la aplicación FastAPI.

    Define todas las variables de entorno necesarias para la aplicación,
    cargándolas desde el archivo .env (si existe) y proporcionando validación
    a través de Pydantic BaseSettings.
    """

    DATABASE_URL: str

    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None

    REDIS_URL: str | None = None

    # Configuración de CORS
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    API_V1_STR: str = "/api/v1"

    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="allow",
    )


settings = Settings()  # type: ignore
