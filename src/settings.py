import logging
import os
import sys
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import locale
locale.setlocale(locale.LC_ALL, "uk_UA.UTF-8")


# Load .env
load_dotenv()

DB_NAME = os.environ["DB_NAME"]
INIT_DB = os.environ["INIT_DB"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
WEATHER_API_URL = os.environ["WEATHER_API_URL"]
WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]

# Logger
logger = logging.getLogger("server")
logger.setLevel(logging.DEBUG)

console_handler_database = logging.StreamHandler()
console_handler_database.setLevel(logging.INFO)

file_handler_database = logging.FileHandler("server.log")
file_handler_database.setLevel(logging.DEBUG)

database_formatter = logging.Formatter(
    "%(asctime)s -  %(name)s - %(levelname)s - %(message)s"
)

console_handler_database.setFormatter(database_formatter)
file_handler_database.setFormatter(database_formatter)

logger.addHandler(console_handler_database)
logger.addHandler(file_handler_database)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
try:
    BOT = Bot(BOT_TOKEN)
    dp = Dispatcher()
    logger.info("Bot created successfully")
except Exception as e:
    logger.error(e)
