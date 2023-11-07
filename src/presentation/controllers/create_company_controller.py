from src.domain.use_cases.create_company import CreateCompanyUseCaseInterface
from src.presentation.schemas.company import CompanyOut


class CreateCompanyController:
    def __init__(self, use_case: CreateCompanyUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, company, owner_id) -> CompanyOut | None:
        response = self.__use_case.execute(company, owner_id)
        return response
