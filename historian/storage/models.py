from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass


class Rate(Base):
    __tablename__ = "mt5_rates"

    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[datetime] = mapped_column()
    instrument_id: Mapped[int] = mapped_column(ForeignKey("instruments.id"))
    period: Mapped[int] = mapped_column()
    open: Mapped[float] = mapped_column()
    high: Mapped[float] = mapped_column()
    low: Mapped[float] = mapped_column()
    close: Mapped[float] = mapped_column()
    volume: Mapped[int] = mapped_column()
    spread: Mapped[int] = mapped_column()


class Instrument(Base):
    __tablename__ = "instruments"

    id: Mapped[int] = mapped_column(primary_key=True)
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"))
    name: Mapped[str] = mapped_column()
    path: Mapped[str] = mapped_column()
    currency_base: Mapped[str] = mapped_column()
    currency_margin: Mapped[str] = mapped_column()
    currency_profit: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    digits: Mapped[int] = mapped_column()
    volume_min: Mapped[float] = mapped_column()
    volume_max: Mapped[float] = mapped_column()
    volume_step: Mapped[float] = mapped_column()
    spread_floating: Mapped[bool] = mapped_column()


class Tick(Base):
    __tablename__ = "mt5_ticks"

    id: Mapped[int] = mapped_column(primary_key=True)
    instrument_id: Mapped[int] = mapped_column(ForeignKey("instruments.id"))
    timestamp: Mapped[datetime] = mapped_column()
    ask: Mapped[float] = mapped_column()
    bid: Mapped[float] = mapped_column()
    # last: Mapped[float] = mapped_column()
    # volume: Mapped[int] = mapped_column()
    # flags: Mapped[int] = mapped_column()


class Source(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
