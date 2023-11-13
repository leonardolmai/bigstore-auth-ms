from abc import ABC, abstractmethod

from src.domain.entities.user import User


class CreateUserUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, user: User) -> User | None:
        pass
