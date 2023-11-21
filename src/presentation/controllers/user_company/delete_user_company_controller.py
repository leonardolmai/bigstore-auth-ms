from src.domain.use_cases.user_company.delete_user_company import (
    DeleteUserCompanyUseCaseInterface,
)
from src.presentation.schemas.user_company import UserCompanyOut


class DeleteUserCompanyController:
    def __init__(self, use_case: DeleteUserCompanyUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, user_id, company_id) -> UserCompanyOut | None:
        response = self.__use_case.execute(user_id, company_id)
        return response
