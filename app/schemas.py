import datetime

from pydantic import BaseModel, ConfigDict


class CityBase(BaseModel):
    name: str
    additional_info: str


class CityCreate(CityBase):
    id: int


class CityRead(CityBase):

    id: int
    model_config = ConfigDict(from_attributes=True)


class TemperatureBase(BaseModel):
    city_id: int
    date_time: datetime.datetime
    temperature: float


class TemperatureRead(TemperatureBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
