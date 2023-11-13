from abc import ABC, abstractmethod

from src.domain.entities.company import Company


class GetCompanyUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: int) -> Company | None:
        pass
