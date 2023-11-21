from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def list_users(self) -> list[User] | None:
        pass

    @abstractmethod
    def get_user(self, email: str) -> User | None:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User | None:
        pass

    @abstractmethod
    def update_user(self, email: str, update_fields: dict[str, Any]) -> User | None:
        pass

    @abstractmethod
    def delete_user(self, email: str) -> bool:
        pass
