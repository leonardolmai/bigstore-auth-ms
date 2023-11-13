from src.domain.use_cases.company.update_company import (
    UpdateCompanyUseCaseInterface,
)
from src.presentation.schemas.company import CompanyOut


class UpdateCompanyController:
    def __init__(self, use_case: UpdateCompanyUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id, company) -> CompanyOut | None:
        response = self.__use_case.execute(id, company)
        return response
