from abc import ABC, abstractmethod

from src.domain.entities.user_company import UserCompany


class CreateUserCompanyUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, user_company: UserCompany) -> UserCompany | None:
        pass
