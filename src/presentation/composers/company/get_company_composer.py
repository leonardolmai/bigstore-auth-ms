from src.data.use_cases.company.get_company import GetCompanyUseCase
from src.infrastructure.database.repositories.company_repository import (
    CompanyRepository,
)
from src.presentation.controllers.company.get_company_controller import (
    GetCompanyController,
)
from src.presentation.schemas.company import CompanyOut


def get_company_composer(session, id) -> CompanyOut | None:
    repository = CompanyRepository(session)
    use_case = GetCompanyUseCase(repository)
    controller = GetCompanyController(use_case)
    company = controller.handle(id)
    return company
