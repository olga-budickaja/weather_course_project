from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


select_language = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🇺🇦")], [KeyboardButton(text="🇺🇸")]],
    one_time_keyboard=True,
    resize_keyboard=True,
)

confirm = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="👍")], [KeyboardButton(text="👎")]],
    one_time_keyboard=True,
    resize_keyboard=True,
)
