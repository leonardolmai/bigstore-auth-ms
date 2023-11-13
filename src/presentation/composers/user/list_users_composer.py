from src.data.use_cases.user.list_users import ListUsersUseCase
from src.infrastructure.database.repositories.user_repository import (
    UserRepository,
)
from src.presentation.controllers.user.list_users_controller import (
    ListUsersController,
)
from src.presentation.schemas.user import UserOut


def list_users_composer(session) -> list[UserOut] | None:
    repository = UserRepository(session)
    use_case = ListUsersUseCase(repository)
    controller = ListUsersController(use_case)
    users = controller.handle()
    return users
