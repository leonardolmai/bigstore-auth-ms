from src.data.use_cases.user.create_user import CreateUserUseCase
from src.infrastructure.database.repositories.user_repository import (
    UserRepository,
)
from src.presentation.controllers.user.create_user_controller import (
    CreateUserController,
)
from src.presentation.schemas.user import UserOut


def create_user_composer(session, user) -> UserOut | None:
    repository = UserRepository(session)
    use_case = CreateUserUseCase(repository)
    controller = CreateUserController(use_case)
    user = controller.handle(user)
    return user
