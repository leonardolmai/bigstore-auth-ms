from src.domain.use_cases.user_company.list_user_companies import (
    ListUserCompaniesUseCaseInterface,
)
from src.presentation.schemas.user_company import UserCompanyOut


class ListUserCompaniesController:
    def __init__(self, use_case: ListUserCompaniesUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, user, company) -> list[UserCompanyOut] | None:
        response = self.__use_case.execute(user, company)
        return response
