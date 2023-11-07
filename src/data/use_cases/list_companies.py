from src.data.repositories.company_repository import CompanyRepositoryInterface
from src.domain.entities.company import Company
from src.domain.use_cases.list_companies import ListCompaniesUseCaseInterface


class ListCompaniesUseCase(ListCompaniesUseCaseInterface):
    def __init__(self, company_repository: CompanyRepositoryInterface) -> None:
        self.__company_repository = company_repository

    def execute(self) -> list[Company] | None:
        companies = self.__company_repository.list_companies()
        return companies
