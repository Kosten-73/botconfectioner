from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

get_stop_sup_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Завершить разговор')]
    ], resize_keyboard=True, one_time_keyboard=True
)