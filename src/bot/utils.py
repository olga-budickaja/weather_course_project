from bot.states import *
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import bot.keyboards as kb
from settings import logger
from database.actions import insert_user
from bot.messages.texts import get_text
from database.data import get_user_by_id


async def add_user(message: Message, state: FSMContext) -> None:
    """
    Adds a user to the database or sends a welcome message if they already exist.

    :param message: Incoming Telegram message.
    :param state: Finite State Machine context for storing user session data.
    """
    data: dict = await state.get_data()
    if data:
        await message.answer(get_text(message, data["lang"], "welcome"))
        await insert_user(
            message.from_user.id, message.from_user.first_name, data["lang"]
        )
    else:
        user = await get_user_by_id(message.from_user.id)
        if user:
            await message.answer(get_text(message, user[0][2], "welcome"))
        else:
            logger.warning(f"User {message.from_user.id} not found in database.")


async def choise_language(message: Message, state: FSMContext) -> None:
    """
    Starts the language selection process for the user.

    :param message: Incoming Telegram message.
    :param state: FSMContext for handling user state transitions.
    """
    logger.info(
        f"Received /start command from user {message.from_user.id} with message: {message.text}"
    )
    await state.set_state(OnbordingUserState.select_language)
    await message.answer(
        get_text(message, 1, "hello"), reply_markup=kb.user.select_language
    )
