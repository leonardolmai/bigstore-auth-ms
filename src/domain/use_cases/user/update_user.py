from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.user import User


class UpdateUserUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, email, update_fields: dict[str, Any]) -> User | None:
        pass
