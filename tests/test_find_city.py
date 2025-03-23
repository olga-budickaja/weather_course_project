import aiosqlite
import pytest

from src.database.utils import get_city_by_first_letters

DB_NAME = "test_db.sqlite"


@pytest.fixture(scope="module")
async def setup_database():
    """Creates a test database with a table of cities."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS cities ("
            "id INTEGER PRIMARY KEY, "
            "name_uk TEXT, "
            "name_en TEXT"
            ");"
        )

        await db.executemany(
            "INSERT INTO cities (name_uk, name_en) VALUES (?, ?)",
            [
                ("Київ", "Kyiv"),
                ("Харків", "Kharkiv"),
                ("Львів", "Lviv"),
                ("Одеса", "Odesa"),
            ],
        )
        await db.commit()


@pytest.mark.asyncio
async def test_get_city_by_first_letters_uk(setup_database):
    """Checks whether Ukrainian city names are returned correctly."""
    results = await get_city_by_first_letters("Ки", uk=True)

    assert isinstance(results, list), "The result should be a list."
    assert len(results) > 0, "The list of cities must not be empty."
    assert ("Kyiv",) in results, "Expected result: 'Київ'"


@pytest.mark.asyncio
async def test_get_city_by_first_letters_en(setup_database):
    """Checks whether English city names are returned correctly."""
    results = await get_city_by_first_letters("Kha", uk=False)

    assert isinstance(results, list), "The result should be a list."
    assert len(results) > 0, "The list of cities must not be empty."
    assert ("Kharkiv",) in results, "Expected result: 'Kharkiv'"


@pytest.mark.asyncio
async def test_get_city_by_first_letters_no_match():
    """Checks the case where the city is not found."""
    results = await get_city_by_first_letters("XYZ", uk=True)

    assert isinstance(results, list), "The result should be a list."
    assert len(results) == 0, "Expect an empty list if there are no matches"
