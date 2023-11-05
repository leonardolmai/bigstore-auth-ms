from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship

from src.infrastructure.database.models.base import Base


class UserCompany(Base):
    __tablename__ = "user_company"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"), nullable=False)
    is_employee: Mapped[bool] = mapped_column(default=False)

    user = relationship(
        "User", backref=backref("companies", lazy="dynamic"), foreign_keys=[user_id]
    )
    company = relationship(
        "Company", backref=backref("users", lazy="dynamic"), foreign_keys=[company_id]
    )

    __table_args__ = (
        UniqueConstraint("user_id", "company_id", name="unique_user_company"),
    )
