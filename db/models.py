from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

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
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        info={
            "verbose_name": "Дата создания",
        },
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        info={
            "verbose_name": "Дата обновления",
        },
    )

    def __repr__(self) -> str:
        return f"{self.pk}"
