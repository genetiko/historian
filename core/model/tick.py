from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Tick(DeclarativeBase):
    __tablename__ = "ticks"

    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[int] = mapped_column()
    ask: Mapped[float] = mapped_column()
    bid: Mapped[float] = mapped_column()
    last: Mapped[float] = mapped_column()
    volume: Mapped[int] = mapped_column()
    flags: Mapped[int] = mapped_column()
