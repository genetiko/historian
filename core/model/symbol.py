from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Symbol(DeclarativeBase):
    __tablename__ = "symbols"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
