from src.domain.use_cases.user.update_user import UpdateUserUseCaseInterface
from src.main.settings.config import pwd_context
from src.presentation.schemas.user import UserOut


class UpdateUserController:
    def __init__(self, use_case: UpdateUserUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, email, user) -> UserOut | None:
        if "password" in user and user["password"]:
            user["password"] = self.__get_password_hash(user["password"])
        response = self.__use_case.execute(email, user)
        return response

    def __get_password_hash(self, password):
        return pwd_context.hash(password)
