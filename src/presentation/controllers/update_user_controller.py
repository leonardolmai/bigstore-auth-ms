from src.domain.use_cases.update_user import UpdateUserUseCaseInterface
from src.presentation.schemas.user import UserOut


class UpdateUserController:
    def __init__(self, use_case: UpdateUserUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, email, user) -> UserOut | None:
        response = self.__use_case.execute(email, user)
        return response
