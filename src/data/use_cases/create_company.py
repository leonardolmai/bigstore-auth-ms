from src.data.repositories.company_repository import CompanyRepositoryInterface
from src.domain.entities.company import Company
from src.domain.use_cases.create_company import CreateCompanyUseCaseInterface


class CreateCompanyUseCase(CreateCompanyUseCaseInterface):
    def __init__(self, company_repository: CompanyRepositoryInterface) -> None:
        self.__company_repository = company_repository

    def execute(self, company: Company, owner_id) -> Company | None:
        company = self.__company_repository.create_company(company, owner_id)
        return company
