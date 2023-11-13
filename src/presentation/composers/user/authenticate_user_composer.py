from src.data.use_cases.user.get_user import GetUserUseCase
from src.data.use_cases.user.update_user import UpdateUserUseCase
from src.infrastructure.database.repositories.user_repository import (
    UserRepository,
)
from src.presentation.controllers.user.authenticate_user_controller import (
    AuthenticateUserUserController,
)
from src.presentation.controllers.user.get_user_controller import (
    GetUserController,
)
from src.presentation.controllers.user.update_user_controller import (
    UpdateUserController,
)
from src.presentation.schemas.user import UserOut


def authenticate_user_composer(session, form_data) -> UserOut | None:
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
        return token
    return None
