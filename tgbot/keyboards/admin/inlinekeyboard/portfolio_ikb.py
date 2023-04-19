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

item_callback = CallbackData('item', 'page', 'action')

def get_items_keyboard(page: int = 0, count_items: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    has_next_page = count_items > page + 1
    if page != 0:
        keyboard.insert(
            InlineKeyboardButton(
                text="< Назад",
                callback_data=item_callback.new(page=page - 1, action='following')
            )
        )

    keyboard.insert(
        InlineKeyboardButton(
            text=f"• {page + 1}",
            callback_data="dont_click_me"
        )
    )

    if has_next_page:
        keyboard.insert(
            InlineKeyboardButton(
                text="Вперёд >",
                callback_data=item_callback.new(page=page + 1, action='following')
            )
        )

    keyboard.add(
        InlineKeyboardButton(text='Вернутся в меню',
                             callback_data='return_menu_portfolio'

        )
    )

    keyboard.add(
        InlineKeyboardButton(text='Удалить',
                             callback_data=item_callback.new(page=page + 1, action='delete')
        )
    )

    keyboard.add(
        InlineKeyboardButton(text='Изменить название',
                             callback_data=item_callback.new(page=page + 1, action='edit_name')
                             )
    )

    keyboard.add(
        InlineKeyboardButton(text='Изменить описание',
                             callback_data=item_callback.new(page=page + 1, action='edit_description')
                             )
    )

    keyboard.add(
        InlineKeyboardButton(text='Изменить фото',
                             callback_data=item_callback.new(page=page + 1, action='edit_photo')
                             )
    )

    return keyboard