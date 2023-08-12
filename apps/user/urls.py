from fastapi import APIRouter

__all__ = [
    "router",
]

from sqlalchemy.orm import load_only
from sqlalchemy import select
from apps.user.models import User
from db.session import AsyncSessionLocal

router = APIRouter()


async def get_all_users():
    load_only(User.pk, User.first_name, User.email)
    select(User).filter(User.email == "first@kl.ru")
    async with AsyncSessionLocal():
        pass
