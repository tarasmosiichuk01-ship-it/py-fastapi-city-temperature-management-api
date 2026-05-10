import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class DBCity(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(63), nullable=False, unique=True)
    additional_info: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )
    temperatures: Mapped[list["DBTemperature"]] = relationship(
        back_populates="city"
    )


class DBTemperature(Base):
    __tablename__ = "temperatures"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), index=True)
    date_time: Mapped[datetime.datetime]
    temperature: Mapped[float]
    city: Mapped["DBCity"] = relationship(back_populates="temperatures")
