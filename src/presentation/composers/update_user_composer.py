from src.data.use_cases.update_user import UpdateUserUseCase
from src.infrastructure.database.repositories.user_repository import (
    UserRepository,
)
from src.presentation.controllers.update_user_controller import (
    UpdateUserController,
)
from src.presentation.schemas.user import UserOut


def update_user_composer(session, email, user) -> UserOut | None:
    repository = UserRepository(session)
    use_case = UpdateUserUseCase(repository)
    controller = UpdateUserController(use_case)
    user = controller.handle(email, user)
    return user
