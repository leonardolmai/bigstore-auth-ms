from src.domain.use_cases.user_company.create_user_company import (
    CreateUserCompanyUseCaseInterface,
)
from src.presentation.schemas.user_company import UserCompanyOut


class CreateUserCompanyController:
    def __init__(self, use_case: CreateUserCompanyUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, user_company) -> UserCompanyOut | None:
        response = self.__use_case.execute(user_company)
        return response
