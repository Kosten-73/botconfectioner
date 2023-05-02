from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

item_callback = CallbackData('item', 'page')


def get_items_keyboard_user(page: int = 0, count_items: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    has_next_page = count_items > page + 1
    if page != 0:
        keyboard.insert(
            InlineKeyboardButton(
                text="⏪",
                callback_data=item_callback.new(page=page - 1)
            )
        )

    keyboard.insert(
        InlineKeyboardButton(
            text=f"⬛️{page + 1}⬛️",
            callback_data="dont_click_me"
        )
    )

    if has_next_page:
        keyboard.insert(
            InlineKeyboardButton(
                text="⏩",
                callback_data=item_callback.new(page=page + 1)
            )
        )

    keyboard.add(
        InlineKeyboardButton(text='Вернутся в меню↩️',
                             callback_data='return_main_menu'
                             )
    )

    return keyboard