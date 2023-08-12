from fastapi import FastAPI

from apps.urls import router
from conf import settings

app = FastAPI(
    debug=settings.DEBUG,
)

app.include_router(router=router, prefix="/api")
