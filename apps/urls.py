from fastapi import APIRouter

from .user.urls import router as user_router

__all__ = [
    "router",
]

router = APIRouter()

router.include_router(
    router=user_router,
    prefix="/users",
    tags=["users"],
)
