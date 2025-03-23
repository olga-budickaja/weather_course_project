from aiogram.types import Message


def get_text(message: Message, lang: int, key: str, action=None):
    messages = {
        "hello": {
            1: (
                f"Hello, {message.from_user.first_name}, change language\n"
                f"Вітаю, {message.from_user.first_name}, оберіть мову"
            ),
            0: "",
        },
        "confirm": {
            1: (
                f"{message.from_user.first_name},"
                f"підтвердіть, будь ласка, свій вибір {action}"
            ),
            0: (
                f"{message.from_user.first_name},"
                f" please confirm your choice {action}"
            ),
        },
        "welcome": {
            1: (
                f"Вітаю, {message.from_user.first_name} 👋.\n"
                f"Я бот погоди 🌤☔️☀️.\n"
                f"І я можу показати вам погоду в любому місті 🌆."
            ),
            0: (
                f"Hello, {message.from_user.first_name} 👋.\n"
                f"I`m bot weather 🌤☔️☀️.\n"
                f"And I can show you the weather by any city🌆."
            ),
        },
    }
    return messages[key][lang]
