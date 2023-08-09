from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func

__all__ = [
    "BaseModel",
]


class BaseModel(DeclarativeBase):
    """Абстрактная базовая модель."""
    __tablename__ = None

    pk: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True,
        info={
            "verbose_name": "Первичный ключ",
        },
    )
    uuid: Mapped[UUID] = mapped_column(
        default=uuid4,
        info={
            "verbose_name": "Уникальный идентификатор",
        },
    )
    is_active: Mapped[bool] = mapped_column(
        default=True,
        info={
            "verbose_name": "Активный",
        }
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        info={
            "verbose_name": "Дата создания",
        },
    )
    updated_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(),
        info={
            "verbose_name": "Дата обновления",
        },
        nullable=True,
    )

    def __repr__(self) -> str:
        return f"{self.pk}"
