from src.data.use_cases.company.get_company_by_cnpj import GetCompanyByCNPJUseCase
from src.infrastructure.database.repositories.company_repository import (
    CompanyRepository,
)
from src.presentation.controllers.company.get_company_by_cnpj_controller import (
    GetCompanyByCNPJController,
)
from src.presentation.schemas.company import CompanyOut


def get_company_by_cnpj_composer(session, cnpj) -> CompanyOut | None:
    repository = CompanyRepository(session)
    use_case = GetCompanyByCNPJUseCase(repository)
    controller = GetCompanyByCNPJController(use_case)
    company = controller.handle(cnpj)
    return company
