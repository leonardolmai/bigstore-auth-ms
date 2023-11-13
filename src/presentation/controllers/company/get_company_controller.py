from src.domain.use_cases.company.get_company import GetCompanyUseCaseInterface
from src.presentation.schemas.company import CompanyOut


class GetCompanyController:
    def __init__(self, use_case: GetCompanyUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id) -> CompanyOut | None:
        response = self.__use_case.execute(id)
        return response
