from datetime import datetime
import os

import httpx
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import DBTemperature

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_WEATHER_KEY")

URL = "http://api.weatherapi.com/v1/current.json"

if not API_KEY:
    raise RuntimeError("API_KEY environment variable is not set")


async def get_weather(city: str) -> dict:
    params = {"key": API_KEY, "q": city}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(URL, params=params)
        except httpx.RequestError:
            raise HTTPException(
                status_code=503,
                detail="Weather service unavailable"
            )

        if response.status_code == 400:
            raise HTTPException(
                status_code=404,
                detail=f"City '{city}' not found"
            )

        if response.status_code != 200:
            raise HTTPException(
                status_code=502,
                detail="Error fetching weather data"
            )

        return response.json()


async def create_temperature(
    db: AsyncSession,
    city_id: int,
    temperature: float,
    date_time: datetime
) -> DBTemperature:
    temperature_record = DBTemperature(
        city_id=city_id,
        date_time=date_time,
        temperature=temperature
    )
    db.add(temperature_record)
    await db.commit()
    await db.refresh(temperature_record)
    return temperature_record
