from src.data.use_cases.user.get_user import GetUserUseCase
from src.infrastructure.database.repositories.user_repository import (
    UserRepository,
)
from src.presentation.controllers.user.get_authenticated_user_controller import (
    GetAuthenticatedUserController,
)
from src.presentation.schemas.user import UserOut


def get_authenticated_user_composer(session, token) -> UserOut | None:
    repository = UserRepository(session)
    use_case = GetUserUseCase(repository)
    controller = GetAuthenticatedUserController(use_case)
    user = controller.handle(token)
    return user
