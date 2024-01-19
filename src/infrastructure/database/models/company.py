from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship

from src.infrastructure.database.models.base import Base


class Company(Base):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    cnpj: Mapped[str] = mapped_column(String(14), unique=True)
    website: Mapped[str | None] = mapped_column(String(255))
    owner_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    is_approved: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)

    owner = relationship(
        "User", backref=backref("company", uselist=False), foreign_keys=[owner_id]
    )
