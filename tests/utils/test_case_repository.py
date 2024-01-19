from unittest.mock import Mock

from sqlalchemy.orm import Session

from tests.utils.test_case_base import TestCaseBase


class TestCaseRepositoryBase(TestCaseBase):
    def setUp(self):
        self.session_mock = Mock(spec=Session)

    def tearDown(self):
        self.session_mock.reset_mock()
