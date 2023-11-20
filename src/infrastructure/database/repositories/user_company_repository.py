from typing import Any

from sqlalchemy.orm import Session

from src.data.repositories.user_company_repository import UserCompanyRepositoryInterface
from src.domain.entities.user_company import UserCompany
from src.infrastructure.database.models.user_company import (
    UserCompany as UserCompanyModel,
)


class UserCompanyRepository(UserCompanyRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def get_user_company(self, id: int) -> UserCompany | None:
        try:
            return (
                self.session.query(UserCompanyModel)
                .filter(UserCompanyModel.id == id)
                .one_or_none()
            )
        except:
            return None

    def create_user_company(self, user_company: UserCompany) -> UserCompany | None:
        existing_relation = (
            self.session.query(UserCompanyModel)
            .filter_by(user_id=user_company.user_id, company_id=user_company.company_id)
            .first()
        )

        if existing_relation:
            return existing_relation

        try:
            user_company_data = {
                "user_id": user_company.user_id,
                "company_id": user_company.company_id,
                "is_employee": user_company.is_employee,
            }
            user_company_model = UserCompanyModel(**user_company_data)

            self.session.add(user_company_model)
            self.session.commit()

            return user_company_model
        except:
            return None

    def update_user_company(
        self, id: int, update_fields: dict[str, Any]
    ) -> UserCompany | None:
        try:
            self.session.query(UserCompanyModel).filter(
                UserCompanyModel.id == id
            ).update(update_fields)
            self.session.commit()
            user_company_updated = self.get_user_company(id)

            return user_company_updated
        except:
            return None
