from database.data import db_operation, users_create_table
from database.queries import CREATE_CITY_INSTANCE, INSERT_USER
from database.utils import cities_list
from settings import logger


@db_operation
async def insert_city(
    db, name: str, lon: float, lat: float, country: str, name_uk: str, name_en: str
):
    """
    Function to insert a table of cities in a database.

    :param db: not entries
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
            name_en=city["name_en"],
        )
    await users_create_table()
    logger.info("Inserting cities created successfully")


@db_operation
async def insert_user(db, id: int, user_name: str, lang: int):
    """
    Function to insert a table of users in a database.

    :param db: not entries
    :param user_name: user name (string) getted from telegram
    :param lang: if user checked Ukranian language: lang == 1, else: lang == 0
    """
    logger.info("Iserting users table in database: ")
    logger.info(INSERT_USER)
    await db.execute(INSERT_USER, (id, user_name, lang))
