import asyncio
from typing import Dict, Optional
import aiohttp
import pandas as pd

from constants import PATH_CITIES_LIST_XLSX
from settings import WEATHER_API_KEY, WEATHER_API_URL
from settings import logger

# Get cities_list from
df = pd.read_excel(PATH_CITIES_LIST_XLSX)

cities_data = df.to_dict(orient="records")

async def get_local_names(session, lat: float, lon: float) -> Optional[Dict[str, str]]:
    """
    Gets local city names by their latitude (lat) and longitude (lon),
    returning only Ukrainian (uk) and English (en) names.

    :param lat: Latitude of the place
    :param lon: Longitude of the place
    :return: Dictionary with local city names or None if the query fails
    """
    url = f"{WEATHER_API_URL}geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={WEATHER_API_KEY}"
    logger.info(f"Request to {url} started")

    try:
        async with session.get(url) as response:
            status = response.status
            logger.info(f"Response for {url} received with status {status}")

            if status == 200:
                data = await response.json()
                if data and isinstance(data, list) and "local_names" in data[0]:
                    local_names = data[0]["local_names"]
                    return {key: local_names[key] for key in ("uk", "en") if key in local_names}
            return None
    except Exception as e:
        logger.error(e)

async def get_cities_data():
    """
    Gets Ukrainian (uk) and English (en) names with the function get_local_names()
    and added their in cities_list.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [get_local_names(session, city["lat"], city["lon"]) for city in cities_data]
        results = await asyncio.gather(*tasks)

        for city, local_names in zip(cities_data, results):
            if local_names:
                city["name_uk"] = local_names.get("uk")
                city["name_en"] = local_names.get("en")
            else:
                city["name_uk"] = None
                city["name_en"] = None

        return cities_data

cities_list = asyncio.run(get_cities_data())
