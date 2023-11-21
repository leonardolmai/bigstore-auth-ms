from src.data.use_cases.company.create_company import CreateCompanyUseCase
from src.data.use_cases.user_company.create_user_company import CreateUserCompanyUseCase
from src.infrastructure.database.repositories.company_repository import (
    CompanyRepository,
)
from src.infrastructure.database.repositories.user_company_repository import (
    UserCompanyRepository,
)
from src.presentation.controllers.company.create_company_controller import (
    CreateCompanyController,
)
from src.presentation.controllers.user_company.create_user_company_controller import (
    CreateUserCompanyController,
)
from src.presentation.schemas.company import CompanyOut
from src.presentation.schemas.user_company import UserCompanyCreate


def create_company_composer(session, company, owner_id) -> CompanyOut | None:
    repository = CompanyRepository(session)
    use_case = CreateCompanyUseCase(repository)
    controller = CreateCompanyController(use_case)
    company = controller.handle(company, owner_id)
    if company:
        repository = UserCompanyRepository(session)
        use_case = CreateUserCompanyUseCase(repository)
        controller = CreateUserCompanyController(use_case)
        user_company = UserCompanyCreate(
            user_id=company.owner_id, company_id=company.id, is_employee=True
        )
        user_company = controller.handle(user_company)
    return company
