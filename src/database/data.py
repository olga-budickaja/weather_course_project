import functools

import aiosqlite

from database.queries import *
from settings import DB_NAME, logger


def db_operation(func):
    """Decorator for wrapping database functions."""

    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        db_name = kwargs.get("db_name", DB_NAME)
        async with aiosqlite.connect(db_name) as db:
            try:
                logger.info(f"Starting {func.__name__} operation...")
                result = await func(db, *args, **kwargs)
                await db.commit()
                logger.info(f"{func.__name__} operation completed successfully.")
                return result
            except Exception as e:
                logger.error(f"Error in {func.__name__} operation: {e}")
                raise

    return wrapper


@db_operation
async def city_create_table(db):
    """Function to create a table of cities in a database."""
    logger.info("Creating cities table in database.")
    await db.execute(CREATE_CITY_TABLE)


@db_operation
async def users_create_table(db):
    """Function to create a table of cities in a database."""
    logger.info("Creating cities table in database.")
    await db.execute(CREATE_USERS_TABLE)


async def init_database():
    logger.info("Initializing database")
    await city_create_table()
    await users_create_table()
    logger.info("Database created successfully")


@db_operation
async def get_cities_from_start_name():
    """
    Gets cities by the first 3 letters in name.

    :return: the first 3 letters of the city name (string)
    """


async def get_city_by_first_letters(start_name: str, uk=True):
    """
    Gets the name of the city from the first 3 letters.

    :param start_name: the first 3 letters of the city name (string)
    :param uk: which language checked in app (boolean),
    if the user checked Urranian: uk == True, else: uk == False
    :return:
    """
    logger.info("Getting city name")
    async with aiosqlite.connect(DB_NAME) as db:
        query = FIND_CITY_BY_START_NAME_UK if uk else FIND_CITY_BY_START_NAME_EN

        try:
            async with db.execute(query, (f"%{start_name}%",)) as cursor:
                data = await cursor.fetchall()
                logger.info("Data getted successfully:")
                logger.info(data)
                return data
        except Exception as e:
            logger.error(e)


async def get_user_by_id(id: int):
    """
    Gets the user by ID.

    :param id: user ID from telegram bot
    :return: True if user finded, else False
    """
    logger.info("Getting user by id")
    logger.info(GET_USER_BY_ID)
    async with aiosqlite.connect(DB_NAME) as db:
        try:
            async with db.execute(GET_USER_BY_ID, (id,)) as cursor:
                data = await cursor.fetchall()
                logger.info("Data of user getted successfully:")
                logger.info(data)
                return data
        except Exception as e:
            logger.error(e)
