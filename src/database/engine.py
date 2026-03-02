"""
Engine async de la base de datos.
"""

from sqlalchemy.ext.asyncio import create_async_engine
from src.config.settings import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=False,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)
