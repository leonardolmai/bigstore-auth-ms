from src.data.repositories.user_repository import UserRepositoryInterface
from src.domain.entities.user import User
from src.domain.use_cases.user.get_user import GetUserUseCaseInterface


class GetUserUseCase(GetUserUseCaseInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def execute(self, email: str) -> User | None:
        user = self.__user_repository.get_user(email)
        return user
