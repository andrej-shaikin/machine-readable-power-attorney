from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from db.models import BaseModel

__all__ = [
    "User",
]


class User(BaseModel):
    """Пользователь."""
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String(length=120),
        unique=True,
        index=True,
        info={
            "verbose_name": "Адрес электронной почты",
        },
    )
    username: Mapped[str] = mapped_column(
        String(length=120),
        unique=True,
        index=True,
        info={
            "verbose_name": "Логин",
        },
    )
    is_email_confirmed: Mapped[bool] = mapped_column(
        info={
            "verbose_name": "Адрес электронной почты подтвержден",
        },
    )
    first_name: Mapped[str] = mapped_column(
        String(length=64),
        index=True,
        info={
            "verbose_name": "Имя",
        },
    )
    last_name: Mapped[str] = mapped_column(
        String(length=64),
        info={
            "verbose_name": "Фамилия",
        },
    )
    patronymic: Mapped[Optional[str]] = mapped_column(
        String(length=64),
        nullable=True,
        info={
            "verbose_name": "Отчество",
        },
    )
    password: Mapped[str] = mapped_column(
        String(length=128),
        info={
            "verbose_name": "Пароль",
        },
    )

    def __repr__(self) -> str:
        return f"<{self.pk}> {self.get_full_name()}"

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        return " ".join([self.last_name, self.first_name, self.patronymic or ""]).strip()
