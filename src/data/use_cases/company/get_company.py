from src.data.repositories.company_repository import CompanyRepositoryInterface
from src.domain.entities.company import Company
from src.domain.use_cases.company.get_company import GetCompanyUseCaseInterface


class GetCompanyUseCase(GetCompanyUseCaseInterface):
    def __init__(self, company_repository: CompanyRepositoryInterface) -> None:
        self.__company_repository = company_repository

    def execute(self, id: int) -> Company | None:
        company = self.__company_repository.get_company(id)
        return company
