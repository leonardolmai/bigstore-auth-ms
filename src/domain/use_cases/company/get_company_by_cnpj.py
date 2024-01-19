from abc import ABC, abstractmethod

from src.domain.entities.company import Company


class GetCompanyByCNPJUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, cnpj: str) -> Company | None:
        pass
