"""Ciclo de vida de la aplicacion."""

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI

from src.database.session import db

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Administra recursos compartidos durante el ciclo de vida.

    Args:
        app: Aplicacion FastAPI en ejecucion.

    Returns:
        Iterador asincrono para startup y shutdown.
    """
    yield
    await db.dispose()
