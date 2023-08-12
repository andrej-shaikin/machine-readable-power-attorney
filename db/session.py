from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from conf import settings

__all__ = [
    "get_db_session",
]

engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(expire_on_commit=False, class_=AsyncSession, bind=engine)


async def get_db_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
