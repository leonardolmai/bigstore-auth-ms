from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.company import Company


class UpdateCompanyUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id, update_fields: dict[str, Any]) -> Company | None:
        pass
