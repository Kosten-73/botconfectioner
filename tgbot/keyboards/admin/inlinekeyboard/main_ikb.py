from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu_ikb = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text='Портфолио',
                                                               callback_data='open_portfolio')],
                                         [InlineKeyboardButton(text='Заказы',
                                                               callback_data='open_order')]
                                     ]
                                     )