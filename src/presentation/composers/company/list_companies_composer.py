from src.data.use_cases.company.list_companies import ListCompaniesUseCase
from src.infrastructure.database.repositories.company_repository import (
    CompanyRepository,
)
from src.presentation.controllers.company.list_companies_controller import (
    ListCompaniesController,
)
from src.presentation.schemas.company import CompanyOut


def list_companies_composer(session) -> list[CompanyOut] | None:
    repository = CompanyRepository(session)
    use_case = ListCompaniesUseCase(repository)
    controller = ListCompaniesController(use_case)
    companies = controller.handle()
    return companies
