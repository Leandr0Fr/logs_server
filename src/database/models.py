"""
Modelos de la base de datos con relaciones corregidas.
"""

from __future__ import annotations
from datetime import datetime
from sqlmodel import Field, SQLModel, func, Relationship
from src.enums.log import LogType


class Log(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: LogType
    message: str

    instance_id: int = Field(foreign_key="appinstance.id")
    instance: AppInstance = Relationship(back_populates="logs")

    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})


class ApiKey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    key: str = Field(index=True, unique=True)
    description: str = Field(default="Main Key")
    is_active: bool = Field(default=True)

    app_id: int = Field(foreign_key="app.id")
    app: App = Relationship(back_populates="api_keys")

    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})


class AppInstance(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    instance_name: str

    app_id: int = Field(foreign_key="app.id")
    app: App = Relationship(back_populates="instances")

    logs: list[Log] = Relationship(back_populates="instance")

    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})


class App(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)

    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: datetime = Field(
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()}
    )

    instances: list[AppInstance] = Relationship(back_populates="app")
    api_keys: list[ApiKey] = Relationship(back_populates="app")
