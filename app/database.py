from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = ("sqlite+aiosqlite:///./"
                           "city_temperature_management.db")

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
)

async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()
