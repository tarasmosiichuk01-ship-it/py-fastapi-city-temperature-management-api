import datetime

from pydantic import BaseModel, ConfigDict


class CityCreate(BaseModel):
    name: str
    additional_info: str | None = None


class CityRead(CityCreate):

    id: int
    model_config = ConfigDict(from_attributes=True)


class TemperatureBase(BaseModel):
    city_id: int
    date_time: datetime.datetime
    temperature: float


class TemperatureRead(TemperatureBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
