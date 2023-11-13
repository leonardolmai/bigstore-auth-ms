from typing import Any

from src.data.repositories.user_repository import UserRepositoryInterface
from src.domain.entities.user import User
from src.domain.use_cases.user.update_user import UpdateUserUseCaseInterface


class UpdateUserUseCase(UpdateUserUseCaseInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def execute(self, email, update_fields: dict[str, Any]) -> User | None:
        user = self.__user_repository.update_user(email, update_fields)
        return user
