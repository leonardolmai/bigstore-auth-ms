from src.data.use_cases.company.update_company import UpdateCompanyUseCase
from src.infrastructure.database.repositories.company_repository import (
    CompanyRepository,
)
from src.presentation.controllers.company.update_company_controller import (
    UpdateCompanyController,
)
from src.presentation.schemas.company import CompanyOut


def update_company_composer(session, id, company) -> CompanyOut | None:
    repository = CompanyRepository(session)
    use_case = UpdateCompanyUseCase(repository)
    controller = UpdateCompanyController(use_case)
    company = controller.handle(id, company)
    return company
