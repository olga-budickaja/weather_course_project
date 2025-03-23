import asyncio
import functools
import aiosqlite

from database.queries import *
from settings import DB_NAME, logger

def db_operation(func):
    '''Decorator for wrapping database functions.'''
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        db_name = kwargs.get("db_name", DB_NAME)
        async with aiosqlite.connect(db_name) as db:
            try:
                logger.info(f"Starting {func.__name__} operation...")
                # Викликаємо оригінальну функцію та передаємо `db`
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

async def init_database():
    logger.info("Initializing database")
    await city_create_table()
    # await users_create_table()
    logger.info("Database created successfully")


@db_operation
async def get_cities_from_start_name():
    '''
    Gets cities by the first 3 letters in name.

    :return: the first 3 letters of the city name (string)
    '''
