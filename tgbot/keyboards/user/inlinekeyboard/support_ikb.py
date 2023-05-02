from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

accept_sup = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [InlineKeyboardButton('Принять',
                                                          callback_data='accept_supper')],
                                ])