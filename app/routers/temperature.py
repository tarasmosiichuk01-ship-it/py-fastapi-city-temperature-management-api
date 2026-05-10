import asyncio
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas, crud
from app.dependencies import get_db
from app.temperature_service import get_weather, create_temperature

router = APIRouter()


@router.post(
    "/temperatures/update",
    response_model=list[schemas.TemperatureRead]
)
async def update_temperatures(
    db: AsyncSession = Depends(get_db)
) -> list[schemas.TemperatureRead]:

    cities = await crud.read_all_cities(db=db)
    if not cities:
        return []

    tasks = [get_weather(city.name) for city in cities]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    if results is None:
        raise HTTPException(status_code=404, detail="City not found")

    saved = []
    for city, result in zip(cities, results):
        if isinstance(result, Exception):
            continue

        temperature = result["current"]["temp_c"]
        record = await create_temperature(
            db=db,
            city_id=city.id,
            temperature=temperature,
            date_time=datetime.now(timezone.utc)
        )
        if record is None:
            raise HTTPException(status_code=404, detail="City not found")

        saved.append(record)

    return saved


@router.get("/temperatures", response_model=list[schemas.TemperatureRead])
async def get_all_temperatures(
    city_id: int | None = None,
    db: AsyncSession = Depends(get_db)
) -> list[schemas.TemperatureRead]:
    return await crud.read_all_temperatures(db=db, city_id=city_id)
