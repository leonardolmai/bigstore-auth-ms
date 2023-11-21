from src.domain.use_cases.user.delete_user import DeleteUserUseCaseInterface
from src.presentation.schemas.user import UserOut


class DeleteUserController:
    def __init__(self, use_case: DeleteUserUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, email) -> UserOut | None:
        response = self.__use_case.execute(email)
        return response
