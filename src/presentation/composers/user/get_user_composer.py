from src.data.use_cases.user.get_user import GetUserUseCase
from src.infrastructure.database.repositories.user_repository import (
    UserRepository,
)
from src.presentation.controllers.user.get_user_controller import (
    GetUserController,
)
from src.presentation.schemas.user import UserOut


def get_user_composer(session, email) -> UserOut | None:
    repository = UserRepository(session)
    use_case = GetUserUseCase(repository)
    controller = GetUserController(use_case)
    user = controller.handle(email)
    return user
