from src.data.use_cases.company.delete_company import DeleteCompanyUseCase
from src.infrastructure.database.repositories.company_repository import (
    CompanyRepository,
)
from src.presentation.controllers.company.delete_company_controller import (
    DeleteCompanyController,
)
from src.presentation.schemas.company import CompanyOut


def delete_company_composer(session, id) -> CompanyOut | None:
    repository = CompanyRepository(session)
    use_case = DeleteCompanyUseCase(repository)
    controller = DeleteCompanyController(use_case)
    company = controller.handle(id)
    return company
