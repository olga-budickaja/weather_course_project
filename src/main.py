import asyncio

import database.data as db
from bot import *

# import database.actions as da
from database.data import get_city_by_first_letters
from settings import BOT, INIT_DB, dp

cities = []


# print(cities_list[:5])
async def main():
    global cities
    if INIT_DB:
        await db.init_database()
        # await da.insert_cities()
        cities = await get_city_by_first_letters("Киї")

    await dp.start_polling(BOT)


asyncio.run(main())
for city in cities:
    print(city[0])
