from src.domain.use_cases.company.get_company_by_cnpj import (
    GetCompanyByCNPJUseCaseInterface,
)
from src.presentation.schemas.company import CompanyOut


class GetCompanyByCNPJController:
    def __init__(self, use_case: GetCompanyByCNPJUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, cnpj) -> CompanyOut | None:
        response = self.__use_case.execute(cnpj)
        return response
