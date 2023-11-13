from abc import ABC, abstractmethod

from src.domain.entities.company import Company


class ListCompaniesUseCaseInterface(ABC):
    @abstractmethod
    def execute(self) -> list[Company] | None:
        pass
