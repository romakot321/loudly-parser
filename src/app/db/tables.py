import datetime as dt
import uuid
from uuid import UUID
from enum import Enum, auto

from sqlalchemy import bindparam
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import text
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped as M
from sqlalchemy.orm import mapped_column as column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import false
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.associationproxy import AssociationProxy

from sqlalchemy_service import Base
from sqlalchemy_service.base_db.base import ServiceEngine

sql_utcnow = text("(now() at time zone 'utc')")

engine = ServiceEngine()


class BaseMixin:
    @declared_attr.directive
    def __tablename__(cls):
        letters = ["_" + i.lower() if i.isupper() else i for i in cls.__name__]
        return "".join(letters).lstrip("_") + "s"

    id: M[UUID] = column(
        server_default=text("gen_random_uuid()"), primary_key=True, index=True
    )
    created_at: M[dt.datetime] = column(server_default=sql_utcnow)
    updated_at: M[dt.datetime | None] = column(nullable=True, onupdate=sql_utcnow)


class TaskItem(Base):
    __tablename__ = "task_items"

    id: M[int] = column(primary_key=True, index=True, autoincrement=True)
    task_id: M[UUID] = column(ForeignKey("tasks.id", ondelete="CASCADE"))

    external_id: M[str]
    title: M[str]
    music_url: M[str]

    task: M["Task"] = relationship(back_populates="items", lazy="selectin")


class Task(BaseMixin, Base):
    error: M[str | None] = column(nullable=True)
    account_id: M[int] = column(ForeignKey("accounts.id", ondelete="CASCADE"))
    user_id: M[str]
    app_bundle: M[str]

    items: M[list["TaskItem"]] = relationship(back_populates="task", lazy="selectin")


class Account(BaseMixin, Base):
    id: M[int] = column(primary_key=True, index=True, autoincrement=True)

    username: M[str]
    client_id: M[str]
    access_token: M[str | None]
    refresh_token: M[str | None]
