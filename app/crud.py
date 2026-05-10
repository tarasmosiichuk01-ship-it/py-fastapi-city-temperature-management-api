from fastapi import HTTPException
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


from app import schemas, models


async def create_city(
    db: AsyncSession,
    city: schemas.CityBase,
) -> dict:
    queryset = insert(models.DBCity).values(
        name=city.name,
        additional_info=city.additional_info
    )
    result = await db.execute(queryset)
    await db.commit()
    response = {**city.model_dump(), "id": result.lastrowid}
    return response


async def read_all_cities(db: AsyncSession) -> list[models.DBCity]:
    queryset = select(models.DBCity)
    result = await db.execute(queryset)
    return result.scalars().all()


async def read_city(db: AsyncSession, city_id: int) -> models.DBCity | None:
    if not city_id:
        raise HTTPException(status_code=400, detail="City not found")
    return await db.scalar(
        select(models.DBCity).where(models.DBCity.id == city_id)
    )


async def update_city(
    db: AsyncSession,
    city_id: int,
    city: schemas.CityBase
) -> models.DBCity | None:
    if not city_id:
        raise HTTPException(status_code=400, detail="City not found")
    queryset = (
        update(models.DBCity)
        .where(models.DBCity.id == city_id)
        .values(name=city.name, additional_info=city.additional_info)
        .returning(models.DBCity)
    )
    result = await db.execute(queryset)
    await db.commit()
    return result.scalar_one_or_none()


async def delete_city(db: AsyncSession, city_id: int) -> None:
    if not city_id:
        raise HTTPException(status_code=400, detail="City not found")
    queryset = delete(models.DBCity).where(models.DBCity.id == city_id)
    await db.execute(queryset)
    await db.commit()


async def read_all_temperatures(
    city_id: int,
    db: AsyncSession
) -> list[models.DBTemperature]:
    queryset = select(models.DBTemperature)
    if city_id is not None:
        queryset = queryset.where(models.DBTemperature.city_id == city_id)
    result = await db.execute(queryset)
    return result.scalars().all()
