from src.data.repositories.user_repository import UserRepositoryInterface
from src.domain.entities.user import User
from src.domain.use_cases.user.list_users import ListUsersUseCaseInterface


class ListUsersUseCase(ListUsersUseCaseInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def execute(self) -> list[User] | None:
        users = self.__user_repository.list_users()
        return users
