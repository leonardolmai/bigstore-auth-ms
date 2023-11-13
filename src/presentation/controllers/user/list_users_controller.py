from src.domain.use_cases.user.list_users import ListUsersUseCaseInterface
from src.presentation.schemas.user import UserOut


class ListUsersController:
    def __init__(self, use_case: ListUsersUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self) -> list[UserOut] | None:
        response = self.__use_case.execute()
        return response
