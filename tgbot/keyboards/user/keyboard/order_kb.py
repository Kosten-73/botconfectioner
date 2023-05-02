from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

get_contact_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Прислать свой номер телефона', request_contact=True)],
        [KeyboardButton(text='Отмена')]
    ], resize_keyboard=True, one_time_keyboard=True
)