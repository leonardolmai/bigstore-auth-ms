from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.company import Company
from src.domain.entities.user import User
from src.domain.entities.user_company import UserCompany


class UserCompanyRepositoryInterface(ABC):
    @abstractmethod
    def list_user_companies(
        self, user: User, company: Company
    ) -> list[UserCompany] | None:
        pass

    @abstractmethod
    def get_user_company(self, id: int) -> UserCompany | None:
        pass

    @abstractmethod
    def create_user_company(self, user_company: UserCompany) -> UserCompany | None:
        pass

    @abstractmethod
    def update_user_company(
        self, id: int, update_fields: dict[str, Any]
    ) -> UserCompany | None:
        pass

    def delete_user_company(self, user_id: int, company_id: int) -> bool:
        pass
