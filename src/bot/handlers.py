import bot.keyboards as kb

from settings import dp
from aiogram.filters import Command
from aiogram.types import Message
from bot.states import *
from aiogram.fsm.context import FSMContext

from bot.messages.texts import get_text
from database.data import get_user_by_id
from bot.utils import add_user, choise_language


@dp.message(Command("start"))
async def start(message: Message, state: FSMContext):
    has_user = await get_user_by_id(message.from_user.id)
    if not has_user:
        await choise_language(message, state)
    else:
        await add_user(message, state)


@dp.message(OnbordingUserState.select_language)
async def select_language(message: Message, state: FSMContext):
    lang = 1 if message.text == "🇺🇦" else 0
    print(lang)
    action = "мови" if message.text == "🇺🇦" else "language"
    await state.update_data(lang=lang)
    choice_lang = "🇺🇦" if lang == 1 else "🇺🇸"
    await message.answer(
        get_text(message, lang, "confirm", f"{action} - {choice_lang}"),
        reply_markup=kb.user.confirm,
    )
    await state.set_state(OnbordingUserState.confirm)


@dp.message(OnbordingUserState.confirm)
async def confirm_languge(message: Message, state: FSMContext):
    if message.text == "👍":
        await add_user(message, state)
    else:
        await choise_language(message, state)
