from src.data.use_cases.create_company import CreateCompanyUseCase
from src.infrastructure.database.repositories.company_repository import (
    CompanyRepository,
)
from src.presentation.controllers.create_company_controller import (
    CreateCompanyController,
)
from src.presentation.schemas.company import CompanyOut


def create_company_composer(session, company, owner_id) -> CompanyOut | None:
    repository = CompanyRepository(session)
    use_case = CreateCompanyUseCase(repository)
    controller = CreateCompanyController(use_case)
    company = controller.handle(company, owner_id)
    return company
