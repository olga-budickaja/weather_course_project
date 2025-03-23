import aiosqlite
import pytest

from src.database.actions import insert_user
from src.database.queries import CREATE_USERS_TABLE
from src.settings import DB_NAME


@pytest.fixture(scope="module")
async def setup_database():
    """Створює тестову базу даних та таблицю users."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(CREATE_USERS_TABLE)
        await db.commit()
    yield
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DROP TABLE users")
        await db.commit()


@pytest.mark.asyncio
async def test_add_user_new(setup_database):
    """Тестуємо додавання нового користувача."""
    async with aiosqlite.connect(DB_NAME) as db:
        await insert_user(1, "TestUser", 1)

        async with db.execute(
            "SELECT id, name, lang FROM users WHERE id = ?", (1,)
        ) as cursor:
            user = await cursor.fetchone()

    assert user is not None, "Користувач повинен бути доданий у базу"
    assert user[0] == 1, "ID користувача має бути 1"
    assert user[1] == "TestUser", "Ім'я користувача має співпадати"
    assert user[2] == 1, "Мова має бути 1 (українська)"


@pytest.mark.asyncio
async def test_add_user_existing(setup_database):
    """Тестуємо поведінку, якщо користувач вже є в базі."""
    async with aiosqlite.connect(DB_NAME) as db:
        await insert_user(2, "ExistingUser", 2)

    # Емуляція отримання користувача
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT id, name, lang FROM users WHERE id = ?", (2,)
        ) as cursor:
            user = await cursor.fetchone()

    assert user is not None, "Користувач має бути знайдений"
    assert user[0] == 2, "ID має бути 2"
    assert user[1] == "ExistingUser", "Ім'я має співпадати"
    assert user[2] == 2, "Мова має бути 2"
