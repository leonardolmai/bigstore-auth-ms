from src.domain.use_cases.company.list_companies import (
    ListCompaniesUseCaseInterface,
)
from src.presentation.schemas.company import CompanyOut


class ListCompaniesController:
    def __init__(self, use_case: ListCompaniesUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self) -> list[CompanyOut] | None:
        response = self.__use_case.execute()
        return response
