from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.user_company import UserCompany


class UpdateUserCompanyUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id, update_fields: dict[str, Any]) -> UserCompany | None:
        pass
