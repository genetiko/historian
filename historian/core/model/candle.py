from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Candle(DeclarativeBase):
    __tablename__ = "candles"

    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[int] = mapped_column()
    open: Mapped[float] = mapped_column()
    high: Mapped[float] = mapped_column()
    low: Mapped[float] = mapped_column()
    close: Mapped[float] = mapped_column()
    tick_volume: Mapped[int] = mapped_column()
    volume: Mapped[int] = mapped_column()
    spread: Mapped[int] = mapped_column()
