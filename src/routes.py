"""Routers de la aplicación"""

from fastapi import FastAPI



def include_routers(app: FastAPI) -> None:
    """Registra todos los routers de la aplicacion.

    Args:
        app: Instancia de FastAPI donde se montan routers.

    Returns:
        None.
    """
