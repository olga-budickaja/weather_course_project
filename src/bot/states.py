from aiogram.fsm.state import State, StatesGroup


class OnbordingUserState(StatesGroup):
    select_language = State()
    confirm = State()
