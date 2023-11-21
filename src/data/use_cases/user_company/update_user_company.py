from typing import Any

from src.data.repositories.user_company_repository import UserCompanyRepositoryInterface
from src.domain.entities.user_company import UserCompany
from src.domain.use_cases.user_company.update_user_company import (
    UpdateUserCompanyUseCaseInterface,
)


class UpdateUserCompanyUseCase(UpdateUserCompanyUseCaseInterface):
    def __init__(self, user_company_repository: UserCompanyRepositoryInterface) -> None:
        self.__user_company_repository = user_company_repository

    def execute(self, id, update_fields: dict[str, Any]) -> UserCompany | None:
        user_company = self.__user_company_repository.update_user_company(
            id, update_fields
        )
        return user_company
