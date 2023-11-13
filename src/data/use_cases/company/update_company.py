from typing import Any

from src.data.repositories.company_repository import CompanyRepositoryInterface
from src.domain.entities.company import Company
from src.domain.use_cases.company.update_company import (
    UpdateCompanyUseCaseInterface,
)


class UpdateCompanyUseCase(UpdateCompanyUseCaseInterface):
    def __init__(self, company_repository: CompanyRepositoryInterface) -> None:
        self.__company_repository = company_repository

    def execute(self, id, update_fields: dict[str, Any]) -> Company | None:
        company = self.__company_repository.update_company(id, update_fields)
        return company
