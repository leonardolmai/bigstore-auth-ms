from abc import ABC, abstractmethod

from src.domain.entities.company import Company


class CreateCompanyUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, company: Company, owner_id) -> Company | None:
        pass
