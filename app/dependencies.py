from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session


async def get_db() -> AsyncSession:
    db = async_session()

    try:
        yield db
    finally:
        await db.close()
