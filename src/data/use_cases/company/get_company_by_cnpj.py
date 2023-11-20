from src.data.repositories.company_repository import CompanyRepositoryInterface
from src.domain.entities.company import Company
from src.domain.use_cases.company.get_company_by_cnpj import (
    GetCompanyByCNPJUseCaseInterface,
)


class GetCompanyByCNPJUseCase(GetCompanyByCNPJUseCaseInterface):
    def __init__(self, company_repository: CompanyRepositoryInterface) -> None:
        self.__company_repository = company_repository

    def execute(self, cnpj: str) -> Company | None:
        company = self.__company_repository.get_company_by_cnpj(cnpj)
        return company
