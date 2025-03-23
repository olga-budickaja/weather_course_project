import aiohttp
import pandas as pd
import pytest

from src.constants import PATH_CITIES_LIST_XLSX
from src.database.utils import get_cities_data, get_local_names


@pytest.fixture(scope="module")
def cities_df():
    """Readed Excel file and returned the cities list."""
    return pd.read_excel(PATH_CITIES_LIST_XLSX).to_dict(orient="records")


@pytest.mark.asyncio(loop_scope="module")
async def test_get_local_names():
    """Verify that get_local_names returns the expected values."""
    async with aiohttp.ClientSession() as session:
        result = await get_local_names(session, 50.45, 30.52)  # Kyiv

    assert result is not None, "The function must return data"
    assert "uk" in result, "Missing Ukrainian name"
    assert "en" in result, "Missing English name"
    assert isinstance(result["uk"], str) and isinstance(
        result["en"], str
    ), "Names must be strings"


@pytest.mark.asyncio(loop_scope="module")
async def test_get_cities_data(cities_df):
    """Checks that get_cities_data returns a valid list of cities."""
    results = await get_cities_data()

    assert isinstance(results, list), "Function must retutn the list."
    assert len(results) > 0, "The list of cities names don`t must be empty."

    for city in results:
        assert "name_uk" in city and "name_en" in city, "Missing local names"
        assert city["name_uk"] is None or isinstance(
            city["name_uk"], str
        ), "name_uk must be str or None"
        assert city["name_en"] is None or isinstance(
            city["name_en"], str
        ), "name_en must be str or None"
