from db.models import BaseModel

__all__ = [
    "User",
]


class User(BaseModel):
    """Пользователь."""
    __tablename__ = "users"
