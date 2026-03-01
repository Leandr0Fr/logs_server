from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, func, Relationship
from src.enums.log import LogType


class App(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)

    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: datetime = Field(
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()}
    )

    instances: List["AppInstance"] = Relationship(back_populates="app")
    api_keys: List["ApiKey"] = Relationship(back_populates="app")


class AppInstance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    instance_name: str

    app_id: int = Field(foreign_key="app.id")
    app: App = Relationship(back_populates="instances")

    logs: List["Log"] = Relationship(back_populates="instance")

    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})


class Log(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: LogType
    message: Optional[str]

    instance_id: int = Field(foreign_key="app_instance.id")
    instance: AppInstance = Relationship(back_populates="logs")

    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})


class ApiKey(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    key: str = Field(index=True, unique=True)
    description: Optional[str] = Field(default="Main Key")
    is_active: bool = Field(default=True)

    app_id: int = Field(foreign_key="app.id")
    app: App = Relationship(back_populates="api_keys")

    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})
