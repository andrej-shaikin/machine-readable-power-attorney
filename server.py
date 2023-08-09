from fastapi import FastAPI

from conf import settings

app = FastAPI(
    debug=settings.DEBUG,
)
