from src.domain.use_cases.company.delete_company import (
    DeleteCompanyUseCaseInterface,
)
from src.presentation.schemas.company import CompanyOut


class DeleteCompanyController:
    def __init__(self, use_case: DeleteCompanyUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id) -> CompanyOut | None:
        response = self.__use_case.execute(id)
        return response
