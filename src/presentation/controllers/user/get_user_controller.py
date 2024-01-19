from src.domain.use_cases.user.get_user import GetUserUseCaseInterface
from src.presentation.schemas.user import UserOut


class GetUserController:
    def __init__(self, use_case: GetUserUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, email) -> UserOut | None:
        response = self.__use_case.execute(email)
        return response
