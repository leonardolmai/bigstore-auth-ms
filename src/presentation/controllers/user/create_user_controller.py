from src.domain.use_cases.user.create_user import CreateUserUseCaseInterface
from src.main.settings.config import pwd_context
from src.presentation.schemas.user import UserOut


class CreateUserController:
    def __init__(self, use_case: CreateUserUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, user) -> UserOut | None:
        user.password = self.__get_password_hash(user.password)
        response = self.__use_case.execute(user)
        return response

    def __get_password_hash(self, password):
        return pwd_context.hash(password)
