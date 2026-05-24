"""
Session async de la base de datos.
"""

from collections.abc import AsyncGenerator, AsyncIterator
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from src.config.settings import settings

class Database:
    """
    Clase que encapsula la sesión asincronca de la BDD.
    """
    def __init__(self) -> None:
        """Inicializa factory de sesiones.

        Args:
            None.

        Returns:
            None.
        """
        self._async_engine = create_async_engine(
            url=settings.DATABASE_URL,
            echo=False,
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
            pool_recycle=1800,
            pool_pre_ping=True,
        )

        self._sessionLocal = async_sessionmaker(
            self._async_engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Sessión de la base de datos.
        """
        async with self._sessionLocal() as session:
            yield session
    
    async def dispose(self) -> None:
        """Libera conexiones abiertas del engine.

        Args:
            None.

        Returns:
            None.
        """
        await self._async_engine.dispose()

db = Database()

async def get_db() -> AsyncIterator[AsyncSession]:
    """Devuelve sesiones de base para dependencias HTTP.

    Args:
        None.

    Returns:
        Iterador asincrono que produce sesiones.
    """
    async for session in db.get_session():
        yield session
