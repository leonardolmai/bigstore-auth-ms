from src.data.repositories.user_company_repository import UserCompanyRepositoryInterface
from src.domain.entities.user_company import UserCompany
from src.domain.use_cases.user_company.create_user_company import (
    CreateUserCompanyUseCaseInterface,
)


class CreateUserCompanyUseCase(CreateUserCompanyUseCaseInterface):
    def __init__(self, user_company_repository: UserCompanyRepositoryInterface) -> None:
        self.__user_company_repository = user_company_repository

    def execute(self, user_company: UserCompany) -> UserCompany | None:
        user_company = self.__user_company_repository.create_user_company(user_company)
        return user_company
