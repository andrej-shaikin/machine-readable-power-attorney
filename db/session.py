from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from conf import settings

__all__ = [
    "AsyncSessionLocal",
]

engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(expire_on_commit=False, class_=AsyncSession, bind=engine)
