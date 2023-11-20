from src.data.use_cases.company.get_company_by_cnpj import GetCompanyByCNPJUseCase
from src.data.use_cases.user.get_user import GetUserUseCase
from src.data.use_cases.user.update_user import UpdateUserUseCase
from src.data.use_cases.user_company.create_user_company import CreateUserCompanyUseCase
from src.infrastructure.database.repositories.company_repository import (
    CompanyRepository,
)
from src.infrastructure.database.repositories.user_company_repository import (
    UserCompanyRepository,
)
from src.infrastructure.database.repositories.user_repository import UserRepository
from src.presentation.controllers.company.get_company_by_cnpj_controller import (
    GetCompanyByCNPJController,
)
from src.presentation.controllers.user.authenticate_user_controller import (
    AuthenticateUserUserController,
)
from src.presentation.controllers.user.get_user_controller import GetUserController
from src.presentation.controllers.user.update_user_controller import (
    UpdateUserController,
)
from src.presentation.controllers.user_company.create_user_company_controller import (
    CreateUserCompanyController,
)
from src.presentation.schemas.user import UserOut
from src.presentation.schemas.user_company import UserCompanyCreate


def authenticate_user_composer(session, form_data, x_company_cnpj) -> UserOut | None:
    repository = UserRepository(session)
    use_case = GetUserUseCase(repository)
    controller = GetUserController(use_case)
    user = controller.handle(form_data.username)
    controller = AuthenticateUserUserController()
    token = controller.handle(user, form_data)
    if token:
        if not user.is_active:
            use_case = UpdateUserUseCase(repository)
            controller = UpdateUserController(use_case)
            user = controller.handle(user.email, {"is_active": True})
        if x_company_cnpj:
            repository = CompanyRepository(session)
            use_case = GetCompanyByCNPJUseCase(repository)
            controller = GetCompanyByCNPJController(use_case)
            company = controller.handle(x_company_cnpj)
            if company:
                repository = UserCompanyRepository(session)
                use_case = CreateUserCompanyUseCase(repository)
                controller = CreateUserCompanyController(use_case)
                user_company = UserCompanyCreate(user_id=user.id, company_id=company.id)
                user_company = controller.handle(user_company)
        return token
    return None
