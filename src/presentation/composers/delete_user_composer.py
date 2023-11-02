from src.data.use_cases.delete_user import DeleteUserUseCase
from src.infrastructure.database.repositories.user_repository import (
    UserRepository,
)
from src.presentation.controllers.delete_user_controller import (
    DeleteUserController,
)
from src.presentation.schemas.user import UserOut


def delete_user_composer(session, email) -> UserOut | None:
    repository = UserRepository(session)
    use_case = DeleteUserUseCase(repository)
    controller = DeleteUserController(use_case)
    user = controller.handle(email)
    return user
