from fastapi import APIRouter

__all__ = [
    "router",
]

from sqlalchemy.orm import load_only

router = APIRouter()

from db.session import get_db_session
from sqlalchemy import select
from apps.user.models import User
from db.session import AsyncSessionLocal


async def get_all_users():
    load_only(User.pk, User.first_name, User.email)
    session = get_db_session()
    select(User).filter(User.email == "first@kl.ru")
    q = 5
    async with AsyncSessionLocal() as session:
        a = 5
