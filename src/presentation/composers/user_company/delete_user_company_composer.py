from src.data.use_cases.user.get_user import GetUserUseCase
from src.data.use_cases.user_company.delete_user_company import DeleteUserCompanyUseCase
from src.infrastructure.database.repositories.user_company_repository import (
    UserCompanyRepository,
)
from src.infrastructure.database.repositories.user_repository import UserRepository
from src.presentation.controllers.user.get_user_controller import GetUserController
from src.presentation.controllers.user_company.delete_user_company_controller import (
    DeleteUserCompanyController,
)
from src.presentation.schemas.user_company import UserCompanyOut


def delete_user_company_composer(session, company, email) -> UserCompanyOut | None:
    repository = UserRepository(session)
    use_case = GetUserUseCase(repository)
    controller = GetUserController(use_case)
    user = controller.handle(email)
    if user:
        repository = UserCompanyRepository(session)
        use_case = DeleteUserCompanyUseCase(repository)
        controller = DeleteUserCompanyController(use_case)
        user_company = controller.handle(user_id=user.id, company_id=company.id)
        return user_company
    return None
