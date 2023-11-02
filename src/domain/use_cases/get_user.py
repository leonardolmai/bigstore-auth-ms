from abc import ABC, abstractmethod

from src.domain.entities.user import User


class GetUserUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, email: str) -> User | None:
        pass
