from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu_ikb = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text='Посмотреть мои работы',
                                                               callback_data='show_portfolio_user')],
                                         [InlineKeyboardButton(text='Сделать заказ',
                                                               callback_data='make_order')],
                                         [InlineKeyboardButton(text='Посмотреть мой текущий заказ',
                                                               callback_data='show_my_order')],
                                         [InlineKeyboardButton(text='Связаться с кондитером',
                                                               callback_data='link_support_call')]
                                     ]
                                     )

back_button_order = InlineKeyboardMarkup(row_width=1,
                                         inline_keyboard=[
                                             [InlineKeyboardButton(text='Отменить свой заказ',
                                                                   callback_data='delete_my_order')],
                                             [InlineKeyboardButton(text='Назад',
                                                                   callback_data='return_main_menu')]
                                         ]
                                         )

back_button = InlineKeyboardMarkup(row_width=1,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text='Назад',
                                                             callback_data='return_main_menu')]
                                   ]
                                   )
