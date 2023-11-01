import pytest

from src.infrastructure.database.settings.db_connection import get_db


@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db = get_db()

    assert db is not None
