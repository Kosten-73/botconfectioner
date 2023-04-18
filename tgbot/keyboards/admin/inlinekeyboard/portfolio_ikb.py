from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from tgbot.database.db_portfolio import command_portfolio as cmd_db

portfolio_ikb = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text='Посмотреть портфолио❌',
                                                               callback_data='show_portfolio')],
                                         [InlineKeyboardButton(text='Добавить✅',
                                                               callback_data='add_new_item')],
                                         [InlineKeyboardButton(text='Назад✅',
                                                               callback_data='back')]
                                     ]
                                     )

item_callback = CallbackData('item', 'page')

def get_items_keyboard(page: int = 0, count_items: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    has_next_page = count_items > page + 1

    if page != 0:
        keyboard.add(
            InlineKeyboardButton(
                text="< Назад",
                callback_data=item_callback.new(page=page - 1)
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text=f"• {page + 1}",
            callback_data="dont_click_me"
        )
    )

    if has_next_page:
        keyboard.add(
            InlineKeyboardButton(
                text="Вперёд >",
                callback_data=item_callback.new(page=page + 1)
            )
        )

    return keyboard