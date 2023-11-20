from typing import Any

from sqlalchemy.orm import Session

from src.data.repositories.company_repository import CompanyRepositoryInterface
from src.domain.entities.company import Company
from src.infrastructure.database.models.company import Company as CompanyModel


class CompanyRepository(CompanyRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_companies(self) -> list[Company] | None:
        try:
            return self.session.query(CompanyModel).all()
        except:
            return None

    def get_company(self, id: int) -> Company | None:
        try:
            return (
                self.session.query(CompanyModel)
                .filter(CompanyModel.id == id)
                .one_or_none()
            )
        except:
            return None

    def get_company_by_cnpj(self, cnpj: str) -> Company | None:
        try:
            return (
                self.session.query(CompanyModel)
                .filter(CompanyModel.cnpj == cnpj)
                .one_or_none()
            )
        except:
            return None

    def create_company(self, company: Company, owner_id: int) -> Company | None:
        try:
            company_data = {
                "name": company.name,
                "cnpj": company.cnpj,
                "website": company.website,
                "owner_id": owner_id,
            }
            company_model = CompanyModel(**company_data)

            self.session.add(company_model)
            self.session.commit()

            return company_model
        except:
            return None

    def update_company(self, id: int, update_fields: dict[str, Any]) -> Company | None:
        try:
            self.session.query(CompanyModel).filter(CompanyModel.id == id).update(
                update_fields
            )
            self.session.commit()
            company_updated = self.get_company(id)

            return company_updated
        except:
            return None

    def delete_company(self, id: int) -> bool:
        try:
            self.session.query(CompanyModel).filter(CompanyModel.id == id).update(
                {CompanyModel.is_active: False}
            )
            self.session.commit()
            return True
        except:
            return False
