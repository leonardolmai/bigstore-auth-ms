from src.data.repositories.user_repository import UserRepositoryInterface
from src.domain.entities.user import User
from src.domain.use_cases.user.create_user import CreateUserUseCaseInterface


class CreateUserUseCase(CreateUserUseCaseInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def execute(self, user: User) -> User | None:
        user = self.__user_repository.create_user(user)
        return user
