from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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