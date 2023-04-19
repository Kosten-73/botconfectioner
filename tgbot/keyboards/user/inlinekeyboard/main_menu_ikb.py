from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu_ikb = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text='Посмотреть мои работы',
                                                               callback_data='show_portfolio_user')],
                                         [InlineKeyboardButton(text='Сделать заказ',
                                                               callback_data='make_to_order')],
                                         [InlineKeyboardButton(text='Связаться с кондитером',
                                                               callback_data='contact_to_Katya')],
                                     ]
                                     )
