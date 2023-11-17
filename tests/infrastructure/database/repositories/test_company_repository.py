from src.infrastructure.database.models.company import Company as CompanyModel
from src.infrastructure.database.repositories.company_repository import (
    CompanyRepository,
)
from tests.factories.factories import CompanyFactory
from tests.utils.test_case_repository import TestCaseRepositoryBase


class TestCompanyRepository(TestCaseRepositoryBase):
    def setUp(self):
        super().setUp()
        self.repo = CompanyRepository(self.session_mock)

    def test_list_companies_returns_companies(self):
        self.session_mock.query.return_value.all.return_value = [
            {
                "id": 1,
                "name": "Company 1",
                "cnpj": "123456789",
                "website": "company1.com",
            },
            {
                "id": 2,
                "name": "Company 2",
                "cnpj": "987654321",
                "website": "company2.com",
            },
        ]

        result = self.repo.list_companies()

        self.session_mock.query.return_value.all.assert_called_once()
        self.assertEqual(len(result), 2)

    def test_list_companies_returns_none_on_exception(self):
        self.session_mock.query.return_value.all.side_effect = Exception(
            "Simulating an exception"
        )

        result = self.repo.list_companies()

        self.session_mock.query.return_value.all.assert_called_once()
        self.assertIsNone(result)

    def test_get_company_return_company(self):
        company = {
            "id": 1,
            "name": "Company 1",
            "cnpj": "123456789",
            "website": "company1.com",
        }
        self.session_mock.query.return_value.filter.return_value.one_or_none.return_value = (
            company
        )

        result = self.repo.get_company(1)

        self.session_mock.query.return_value.filter.return_value.one_or_none.assert_called_once()
        self.assertEqual(result, company)

    def test_get_company_return_none_on_exception(self):
        self.session_mock.query.return_value.filter.return_value.one_or_none.side_effect = Exception(
            "Simulating an exception"
        )

        result = self.repo.get_company(1)

        self.session_mock.query.return_value.filter.return_value.one_or_none.assert_called_once()
        self.assertIsNone(result)

    def test_create_company_returns_company(self):
        company_data = CompanyFactory()

        company_data = {
            "name": company_data.name,
            "cnpj": company_data.cnpj,
            "website": company_data.website,
            "owner_id": company_data.owner.id,
        }
        result = self.repo.create_company(CompanyModel(**company_data), owner_id=1)

        self.session_mock.add.assert_called_once()
        self.session_mock.commit.assert_called_once()
        self.assertEqual(result.name, company_data["name"])
        self.assertEqual(result.cnpj, company_data["cnpj"])

    def test_create_company_returns_none_on_exception(self):
        self.session_mock.add.side_effect = Exception("Simulating an exception")

        result = self.repo.create_company(CompanyModel(), owner_id=1)

        self.session_mock.add.assert_called_once()
        self.session_mock.commit.assert_not_called()
        self.assertIsNone(result)

    def test_update_company_returns_company(self):
        company_data = {
            "name": "Company",
            "website": "company.com",
        }
        self.session_mock.query.return_value.filter.return_value.update.return_value = 1
        self.session_mock.query.return_value.filter.return_value.one_or_none.return_value = CompanyModel(
            name="Company", cnpj="123456789", website="company.com"
        )

        result = self.repo.update_company(1, company_data)

        self.session_mock.query.return_value.filter.return_value.update.assert_called_once_with(
            company_data
        )
        self.session_mock.commit.assert_called_once()
        self.assertEqual(result.name, company_data["name"])

    def test_update_company_returns_none_on_exception(self):
        self.session_mock.query.return_value.filter.return_value.update.side_effect = (
            Exception("Simulating an exception")
        )

        result = self.repo.update_company(1, {})

        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once()
        self.session_mock.commit.assert_not_called()
        self.assertIsNone(result)

    def test_delete_company_returns_true(self):
        self.session_mock.query.return_value.filter.return_value.update.return_value = 1

        result = self.repo.delete_company(1)

        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once()
        self.session_mock.commit.assert_called_once()
        self.assertTrue(result)

    def test_delete_company_returns_false_on_exception(self):
        self.session_mock.query.return_value.filter.return_value.update.side_effect = (
            Exception("Simulating an exception")
        )

        result = self.repo.delete_company(1)

        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once()
        self.session_mock.commit.assert_not_called()
        self.assertFalse(result)
