from src.data.use_cases.user.get_user import GetUserUseCase
from src.data.use_cases.user_company.create_user_company import CreateUserCompanyUseCase
from src.infrastructure.database.repositories.user_company_repository import (
    UserCompanyRepository,
)

# pylint: disable=duplicate-code
from src.infrastructure.database.repositories.user_repository import UserRepository
from src.presentation.controllers.user.get_user_controller import GetUserController
from src.presentation.controllers.user_company.create_user_company_controller import (
    CreateUserCompanyController,
)
from src.presentation.schemas.user_company import UserCompanyCreate, UserCompanyOut


def create_user_company_composer(session, company, email) -> UserCompanyOut | None:
    repository = UserRepository(session)
    use_case = GetUserUseCase(repository)
    controller = GetUserController(use_case)
    user = controller.handle(email)
    if user:
        repository = UserCompanyRepository(session)
        use_case = CreateUserCompanyUseCase(repository)
        controller = CreateUserCompanyController(use_case)
        user_company = UserCompanyCreate(
            user_id=user.id, company_id=company.id, is_employee=True
        )
        user_company = controller.handle(user_company)

        return user_company
    return None
