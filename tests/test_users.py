import aiosqlite
import pytest

from src.database.actions import insert_user
from src.database.queries import CREATE_USERS_TABLE
from src.settings import DB_NAME


@pytest.fixture(scope="module")
async def setup_database():
    """Creates a test database and users table."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(CREATE_USERS_TABLE)
        await db.commit()
    yield
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DROP TABLE users")
        await db.commit()


@pytest.mark.asyncio
async def test_insert_user(setup_database):
    """Test inserting a user into the database."""
    async with aiosqlite.connect(DB_NAME) as db:
        await insert_user(1, "TestUser", 1)

        async with db.execute(
            "SELECT id, name, lang FROM users WHERE id = ?", (1,)
        ) as cursor:
            user = await cursor.fetchone()

    assert user is not None, "User should be inserted into the database"
    assert user[0] == 1, "User ID should be 1"
    assert user[1] == "TestUser", "User name should match"
    assert user[2] == 1, "Language should be 1 (Ukrainian)"
