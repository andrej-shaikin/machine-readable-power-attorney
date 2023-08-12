from passlib.context import CryptContext

_pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

__all__ = [
    "is_compare_passwords",
    "get_password_hash",
]


def is_compare_passwords(hashed_password: str, password: str) -> bool:
    """Проверка корректности пароля."""
    return _pwd_context.verify(secret=password, hash=hashed_password)


def get_password_hash(password: str) -> str:
    """Хеширование пароля."""
    return _pwd_context.hash(password)
