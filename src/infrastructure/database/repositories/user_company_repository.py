from typing import Any

from sqlalchemy.orm import Session

from src.data.repositories.user_company_repository import UserCompanyRepositoryInterface
from src.domain.entities.company import Company
from src.domain.entities.user import User
from src.domain.entities.user_company import UserCompany
from src.infrastructure.database.models.user_company import (
    UserCompany as UserCompanyModel,
)


class UserCompanyRepository(UserCompanyRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_user_companies(
        self, user: User, company: Company
    ) -> list[UserCompany] | None:
        try:
            return (
                self.session.query(UserCompanyModel)
                .filter_by(company_id=company.id, is_employee=True)
                .all()
            )
        except:
            return None

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
            if not existing_relation.is_employee and user_company.is_employee:
                try:
                    self.session.query(UserCompanyModel).filter(
                        UserCompanyModel.id == existing_relation.id
                    ).update({UserCompanyModel.is_employee: True})
                    self.session.commit()
                    user_company_updated = self.get_user_company(existing_relation.id)

                    return user_company_updated
                except:
                    return None

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

    def delete_user_company(self, user_id: int, company_id: int) -> bool:
        existing_relation = (
            self.session.query(UserCompanyModel)
            .filter_by(user_id=user_id, company_id=company_id)
            .first()
        )

        try:
            if existing_relation:
                self.session.query(UserCompanyModel).filter(
                    UserCompanyModel.id == existing_relation.id
                ).update({UserCompanyModel.is_employee: False})
                self.session.commit()
                return True
        except:
            return False
        return False
