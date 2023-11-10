from src.infrastructure.database.models.user import User as UserModel
from src.infrastructure.database.repositories.user_repository import (
    UserRepository,
)
from tests.utils.test_case_repository import TestCaseRepositoryBase


class TestUserRepository(TestCaseRepositoryBase):
    def setUp(self):
        super().setUp()
        self.repo = UserRepository(self.session_mock)

    def test_list_users_returns_users(self):
        self.session_mock.query.return_value.all.return_value = [
            {"id": 1, "name": "User 1", "email": "user1@example.com"},
            {"id": 2, "name": "User 2", "email": "user2@example.com"},
        ]

        result = self.repo.list_users()

        self.session_mock.query.return_value.all.assert_called_once()
        self.assertEqual(len(result), 2)

    def test_list_users_returns_none_on_exception(self):
        self.session_mock.query.return_value.all.side_effect = Exception(
            "Simulating an exception"
        )

        result = self.repo.list_users()

        self.session_mock.query.return_value.all.assert_called_once()
        self.assertIsNone(result)

    def test_get_user_return_user(self):
        user = {
            "id": 1,
            "name": "User 1",
            "email": "user1@example.com",
        }
        self.session_mock.query.return_value.filter.return_value.one_or_none.return_value = (
            user
        )

        result = self.repo.get_user("user1@example.com")

        self.session_mock.query.return_value.filter.return_value.one_or_none.assert_called_once()
        self.assertEqual(result, user)

    def test_get_user_return_none_on_exception(self):
        self.session_mock.query.return_value.filter.return_value.one_or_none.side_effect = Exception(
            "Simulating an exception"
        )

        result = self.repo.get_user("user1@example.com")

        self.session_mock.query.return_value.filter.return_value.one_or_none.assert_called_once()
        self.assertIsNone(result)

    def test_create_user_returns_user(self):
        user_data = {
            "name": "User",
            "email": "user@example.com",
            "password": "123",
            "phone": "123456789",
            "cpf": "12345678901",
        }
        result = self.repo.create_user(UserModel(**user_data))

        self.session_mock.add.assert_called_once()
        self.session_mock.commit.assert_called_once()
        self.assertEqual(result.name, user_data["name"])
        self.assertEqual(result.email, user_data["email"])

    def test_create_user_returns_none_on_exception(self):
        self.session_mock.add.side_effect = Exception("Simulating an exception")

        result = self.repo.create_user(UserModel())

        self.session_mock.add.assert_called_once()
        self.session_mock.commit.assert_not_called()
        self.assertIsNone(result)

    def test_update_user_returns_user(self):
        user_data = {
            "name": "User",
            "phone": "987654321",
        }
        self.session_mock.query.return_value.filter.return_value.update.return_value = 1
        self.session_mock.query.return_value.filter.return_value.one_or_none.return_value = UserModel(
            name="User", email="user@example.com", phone="123456789"
        )

        result = self.repo.update_user("user@example.com", user_data)

        self.session_mock.query.return_value.filter.return_value.update.assert_called_once_with(
            user_data
        )
        self.session_mock.commit.assert_called_once()
        self.assertEqual(result.name, "User")

    def test_update_user_returns_none_on_exception(self):
        self.session_mock.query.return_value.filter.return_value.update.side_effect = (
            Exception("Simulating an exception")
        )

        result = self.repo.update_user("user@example.com", {})

        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once()
        self.session_mock.commit.assert_not_called()
        self.assertIsNone(result)

    def test_delete_user_returns_true(self):
        self.session_mock.query.return_value.filter.return_value.update.return_value = 1

        result = self.repo.delete_user("user@example.com")

        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once()
        self.session_mock.commit.assert_called_once()
        self.assertTrue(result)

    def test_delete_user_returns_false_on_exception(self):
        self.session_mock.query.return_value.filter.return_value.update.side_effect = (
            Exception("Simulating an exception")
        )

        result = self.repo.delete_user("user@example.com")

        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once()
        self.session_mock.commit.assert_not_called()
        self.assertFalse(result)
