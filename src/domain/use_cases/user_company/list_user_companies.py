from abc import ABC, abstractmethod

from src.domain.entities.user_company import UserCompany


class ListUserCompaniesUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, user, company) -> list[UserCompany] | None:
        pass
