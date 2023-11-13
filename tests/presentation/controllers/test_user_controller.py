from unittest.mock import Mock

from src.domain.entities.user import User
from src.domain.use_cases.user.create_user import CreateUserUseCaseInterface
from src.domain.use_cases.user.delete_user import DeleteUserUseCaseInterface
from src.domain.use_cases.user.get_user import GetUserUseCaseInterface
from src.domain.use_cases.user.list_users import ListUsersUseCaseInterface
from src.domain.use_cases.user.update_user import UpdateUserUseCaseInterface
from src.presentation.controllers.user.create_user_controller import (
    CreateUserController,
)
from src.presentation.controllers.user.delete_user_controller import (
    DeleteUserController,
)
from src.presentation.controllers.user.get_user_controller import (
    GetUserController,
)
from src.presentation.controllers.user.list_users_controller import (
    ListUsersController,
)
from src.presentation.controllers.user.update_user_controller import (
    UpdateUserController,
)
from tests.utils.test_case_controller import TestCaseControllerBase


class TestUserController(TestCaseControllerBase):
    def test_list_users_handle_returns_users(self):
        list_users_use_case_mock = Mock(spec=ListUsersUseCaseInterface)
        list_users_controller = ListUsersController(list_users_use_case_mock)

        users_data = [
            {"id": 1, "name": "User 1", "email": "user1@example.com"},
            {"id": 2, "name": "User 2", "email": "user2@example.com"},
        ]
        list_users_use_case_mock.execute.return_value = users_data

        result = list_users_controller.handle()
        self.assertEqual(result, users_data)

    def test_get_user_handle_returns_user(self):
        get_user_use_case_mock = Mock(spec=GetUserUseCaseInterface)
        get_user_controller = GetUserController(get_user_use_case_mock)

        user_data = {"id": 1, "name": "User 1", "email": "user1@example.com"}
        get_user_use_case_mock.execute.return_value = user_data

        result = get_user_controller.handle("user1@example.com")
        self.assertEqual(result, user_data)

    def test_delete_user_handle_returns_user(self):
        delete_user_use_case_mock = Mock(spec=DeleteUserUseCaseInterface)
        delete_user_controller = DeleteUserController(delete_user_use_case_mock)

        user_data = {"id": 1, "name": "User 1", "email": "user1@example.com"}
        delete_user_use_case_mock.execute.return_value = user_data

        result = delete_user_controller.handle("user1@example.com")
        self.assertEqual(result, user_data)

    def test_create_user_handle_returns_user(self):
        create_user_use_case_mock = Mock(spec=CreateUserUseCaseInterface)
        create_user_controller = CreateUserController(create_user_use_case_mock)

        user_data = User(id=1, name="User 1", email="user1@example.com", password="123")
        create_user_use_case_mock.execute.return_value = user_data

        result = create_user_controller.handle(user_data)
        self.assertEqual(result, user_data)

    def test_update_user_handle_returns_user(self):
        update_user_use_case_mock = Mock(spec=UpdateUserUseCaseInterface)
        update_user_controller = UpdateUserController(update_user_use_case_mock)

        user_data = {"id": 1, "name": "User 1", "email": "user1@example.com"}
        update_user_use_case_mock.execute.return_value = user_data

        result = update_user_controller.handle("user1@example.com", user_data)
        self.assertEqual(result, user_data)
