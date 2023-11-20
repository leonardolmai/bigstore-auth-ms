from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.company import Company


class CompanyRepositoryInterface(ABC):
    @abstractmethod
    def list_companies(self) -> list[Company] | None:
        pass

    @abstractmethod
    def get_company(self, id: int) -> Company | None:
        pass

    @abstractmethod
    def get_company_by_cnpj(self, cnpj: str) -> Company | None:
        pass

    @abstractmethod
    def create_company(self, company: Company, owner_id: int) -> Company | None:
        pass

    @abstractmethod
    def update_company(self, id: int, update_fields: dict[str, Any]) -> Company | None:
        pass

    @abstractmethod
    def delete_company(self, id: int) -> bool:
        pass
