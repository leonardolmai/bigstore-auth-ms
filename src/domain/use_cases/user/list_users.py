from abc import ABC, abstractmethod

from src.domain.entities.user import User


class ListUsersUseCaseInterface(ABC):
    @abstractmethod
    def execute(self) -> list[User] | None:
        pass
