from src.data.repositories.user_company_repository import UserCompanyRepositoryInterface
from src.domain.entities.user_company import UserCompany
from src.domain.use_cases.user_company.delete_user_company import (
    DeleteUserCompanyUseCaseInterface,
)


class DeleteUserCompanyUseCase(DeleteUserCompanyUseCaseInterface):
    def __init__(self, user_company_repository: UserCompanyRepositoryInterface) -> None:
        self.__user_company_repository = user_company_repository

    def execute(self, user_id: int, company_id: int) -> UserCompany | None:
        user_company = self.__user_company_repository.delete_user_company(
            user_id, company_id
        )
        return user_company
