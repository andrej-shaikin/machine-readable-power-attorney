from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models import BaseModel

__all__ = [
    "Region",
]


class Region(BaseModel):
    __tablename__ = "reference_region"

    name: Mapped[str] = mapped_column(
        String(length=440),
        unique=True,
        index=True,
        info={
            "verbose_name": "Наименование",
        },
    )
    number: Mapped[int] = mapped_column(
        index=True,
        unique=True,
        info={
            "verbose_name": "Числовой код",
        },
    )
    code: Mapped[str] = mapped_column(
        String(length=2),
        index=True,
        unique=True,
        info={
            "verbose_name": "Код",
        },
    )

    def __repr__(self) -> str:
        return f"<{self.pk}> {self.name} №{self.number}"

    def __str__(self) -> str:
        return f"{self.name} №{self.number}"
