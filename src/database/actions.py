from database.data import db_operation
from database.queries import CREATE_CITY_INSTANCE
from database.utils import cities_list
from settings import logger

@db_operation
async def insert_city(
    db,
    name: str,
    lon: float,
    lat: float,
    country: str,
    name_uk: str,
    name_en: str
):
    """
    Function to insert a table of cities in a database.

    :param name: city name (string)
    :param lon: longitude (float)
    :param lat: latitude (float)
    :param country: contry name (string)
    :param name_uk: name of the city in Ukrainian (string)
    :param name_en: name of the city in English (string)
    """
    logger.info("Iserting cities table in database.")
    await db.execute(CREATE_CITY_INSTANCE, (name, lon, lat, country, name_uk, name_en))

async def insert_cities():
    logger.info("Inserting cities database")
    for city in cities_list:
        await insert_city(
            name=city["name"],
            lon=city["lon"],
            lat=city["lat"],
            country=city["country"],
            name_uk=city["name_uk"],
            name_en=city["name_en"]
        )
    # await users_create_table()
    logger.info("Inserting cities created successfully")
