from src.data.use_cases.get_user import GetUserUseCase
from src.data.use_cases.update_user import UpdateUserUseCase
from src.presentation.controllers.get_user_controller import GetUserController
from src.presentation.schemas.user import UserOut

from src.infrastructure.database.repositories.user_repository import (  # isort:skip
    UserRepository,
)
from src.presentation.controllers.update_user_controller import (  # isort:skip
    UpdateUserController,
)

from src.presentation.controllers.authenticate_user_controller import (  # isort:skip
    AuthenticateUserUserController,
)


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
