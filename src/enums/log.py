"""
Contiene los enums utilizados en el proyecto
"""

from enum import Enum, auto, unique


@unique
class LogType(Enum):
    """
    Representa los tipos de logs asociados a las aplicaciones.

    INFO = Confirmación de que las cosas funcionan como se espera.
    DEBUG = Información detallada para diagnóstico. Solo en desarrollo.
    WARNING = Algo inesperado ocurrió, pero la app sigue funcionando.
    ERROR = Un problema serio, una funcionalidad falló.
    CRITICAL = Error fatal. La aplicación o el servidor podrían morir.

    """

    INFO = auto()
    DEBUG = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()
