from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

support_user_callback = CallbackData('support', 'user_id')


def get_link_to_user_keyboard(user_id: int = None) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(
        text='Связаться с покупателем',
        callback_data=support_user_callback.new(user_id=user_id)
    ))
    return keyboard


order_ikb = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text='Посмотреть все заказы',
                                                           callback_data='all_orders')],
                                     [InlineKeyboardButton(text='Назад↩️',
                                                           callback_data='back')]
                                 ]
                                 )

order_callback = CallbackData('item', 'page', 'action')


def get_order_keyboard(page: int = 0, count_items: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    has_next_page = count_items > page + 1
    if page != 0:
        keyboard.insert(
            InlineKeyboardButton(
                text="⏪",
                callback_data=order_callback.new(page=page - 1, action='follow')
            )
        )

    keyboard.insert(
        InlineKeyboardButton(
            text=f"↔️",
            callback_data="dont_click_me"
        )
    )

    if has_next_page:
        keyboard.insert(
            InlineKeyboardButton(
                text="⏩",
                callback_data=order_callback.new(page=page + 1, action='follow')
            )
        )

    keyboard.add(
        InlineKeyboardButton(text='Принять в работу',
                             callback_data=order_callback.new(page=page + 1, action='accept_pay_order')
                             )
    )

    keyboard.add(
        InlineKeyboardButton(text='Связаться с пользователем',
                             callback_data=order_callback.new(page=page + 1, action='link_user')
                             )
    )

    keyboard.add(
        InlineKeyboardButton(text='Удалить',
                             callback_data=order_callback.new(page=page + 1, action='delete_order')
                             )
    )

    keyboard.add(
        InlineKeyboardButton(text='Вернутся в меню↩️',
                             callback_data='back_to_menu_order'

                             )
    )

    return keyboard


return_to_menu_ikb = InlineKeyboardMarkup(row_width=1,
                                          inline_keyboard=[
                                              [InlineKeyboardButton(text='Вернутся в главное меню',
                                                                    callback_data='back')]
                                          ]
                                          )
