from abc import ABC, abstractmethod

from src.domain.entities.user_company import UserCompany


class DeleteUserCompanyUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, user_id: int, company_id: int) -> UserCompany | None:
        pass
