from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()


@router.post("/cities", response_model=schemas.CityRead)
async def create_city(
    city: schemas.CityCreate,
    db: AsyncSession = Depends(get_db)
) -> schemas.CityCreate:

    return await crud.create_city(db=db, city=city)


@router.get("/cities", response_model=list[schemas.CityRead])
async def get_all_cities(
    db: AsyncSession = Depends(get_db)
) -> list[schemas.CityRead]:
    return await crud.read_all_cities(db=db)


@router.get("/cities/{city_id}", response_model=schemas.CityRead)
async def get_city_detail(
    city_id: int,
    db: AsyncSession = Depends(get_db)
) -> schemas.CityRead:
    city = await crud.read_city(db=db, city_id=city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@router.put("/cities/{city_id}", response_model=schemas.CityRead)
async def put_city(
    city_id: int,
    city: schemas.CityBase,
    db: AsyncSession = Depends(get_db)
) -> schemas.CityRead:
    city = await crud.update_city(db=db, city_id=city_id, city=city)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@router.delete("/cities/{city_id}", status_code=204)
async def delete_city(
    city_id: int,
    db: AsyncSession = Depends(get_db)
) -> None:
    return await crud.delete_city(db=db, city_id=city_id)
