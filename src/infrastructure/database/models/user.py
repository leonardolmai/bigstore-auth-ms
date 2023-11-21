from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str | None] = mapped_column(String(14))
    cpf: Mapped[str | None] = mapped_column(String(11))
    is_active: Mapped[bool] = mapped_column(default=True)
