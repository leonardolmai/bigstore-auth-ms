# pylint: disable=duplicate-code
from src.data.use_cases.user_company.list_user_companies import ListUserCompaniesUseCase
from src.infrastructure.database.repositories.user_company_repository import (
    UserCompanyRepository,
)
from src.presentation.controllers.user_company.list_user_companies_controller import (
    ListUserCompaniesController,
)
from src.presentation.schemas.user_company import UserCompanyOut


def list_user_companies_composer(session, user, company) -> list[UserCompanyOut] | None:
    repository = UserCompanyRepository(session)
    use_case = ListUserCompaniesUseCase(repository)
    controller = ListUserCompaniesController(use_case)
    user_companies = controller.handle(user, company)
    return user_companies
