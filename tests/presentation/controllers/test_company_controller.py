from unittest.mock import Mock

from src.domain.use_cases.create_company import CreateCompanyUseCaseInterface
from src.domain.use_cases.delete_company import DeleteCompanyUseCaseInterface
from src.domain.use_cases.get_company import GetCompanyUseCaseInterface
from src.domain.use_cases.list_companies import ListCompaniesUseCaseInterface
from src.domain.use_cases.update_company import UpdateCompanyUseCaseInterface
from src.presentation.controllers.create_company_controller import (
    CreateCompanyController,
)
from src.presentation.controllers.delete_company_controller import (
    DeleteCompanyController,
)
from src.presentation.controllers.get_company_controller import (
    GetCompanyController,
)
from src.presentation.controllers.list_companies_controller import (
    ListCompaniesController,
)
from src.presentation.controllers.update_company_controller import (
    UpdateCompanyController,
)
from tests.utils.test_case_controller import TestCaseControllerBase


class TestCompanyController(TestCaseControllerBase):
    def test_create_company_handle_returns_company(self):
        create_company_use_case_mock = Mock(spec=CreateCompanyUseCaseInterface)
        create_company_controller = CreateCompanyController(
            create_company_use_case_mock
        )

        company_data = {"id": 1, "name": "Company 1", "cnpj": "12345678901234"}
        create_company_use_case_mock.execute.return_value = company_data

        result = create_company_controller.handle(company_data, owner_id=1)
        self.assertEqual(result, company_data)

    def test_delete_company_handle_returns_company(self):
        delete_company_use_case_mock = Mock(spec=DeleteCompanyUseCaseInterface)
        delete_company_controller = DeleteCompanyController(
            delete_company_use_case_mock
        )

        company_data = {"id": 1, "name": "Company 1", "cnpj": "12345678901234"}
        delete_company_use_case_mock.execute.return_value = company_data

        result = delete_company_controller.handle(company_data["id"])
        self.assertEqual(result, company_data)

    def test_get_company_handle_returns_company(self):
        get_company_use_case_mock = Mock(spec=GetCompanyUseCaseInterface)
        get_company_controller = GetCompanyController(get_company_use_case_mock)

        company_data = {"id": 1, "name": "Company 1", "cnpj": "12345678901234"}
        get_company_use_case_mock.execute.return_value = company_data

        result = get_company_controller.handle(company_data["id"])
        self.assertEqual(result, company_data)

    def test_list_companies_handle_returns_companies(self):
        list_companies_use_case_mock = Mock(spec=ListCompaniesUseCaseInterface)
        list_companies_controller = ListCompaniesController(
            list_companies_use_case_mock
        )

        companies_data = [
            {"id": 1, "name": "Company 1", "cnpj": "12345678901234"},
            {"id": 2, "name": "Company 2", "cnpj": "56789012345678"},
        ]
        list_companies_use_case_mock.execute.return_value = companies_data

        result = list_companies_controller.handle()
        self.assertEqual(result, companies_data)

    def test_update_company_handle_returns_company(self):
        update_company_use_case_mock = Mock(spec=UpdateCompanyUseCaseInterface)
        update_company_controller = UpdateCompanyController(
            update_company_use_case_mock
        )

        company_data = {"id": 1, "name": "Company 1", "cnpj": "12345678901234"}
        update_company_use_case_mock.execute.return_value = company_data

        result = update_company_controller.handle(company_data["id"], company_data)
        self.assertEqual(result, company_data)
