from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel_sup_admin_ikb = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [InlineKeyboardButton('Отменить',
                                                          callback_data='stop_wait')]
                                ])