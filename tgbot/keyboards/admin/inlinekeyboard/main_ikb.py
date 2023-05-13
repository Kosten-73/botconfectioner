from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

accept_callback = CallbackData('accept', 'action')

main_menu_ikb = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text='📕Портфолио📕',
                                                               callback_data='open_portfolio')],
                                         [InlineKeyboardButton(text='📍Ваши заказы📍',
                                                               callback_data='open_order')]
                                     ]
                                     )

ikb_for_portfolio = InlineKeyboardMarkup(row_width=1,
                                         inline_keyboard=[
                                             [InlineKeyboardButton('Принять и добавить✅',
                                                                   callback_data=accept_callback.new(action='accept'))],
                                             [InlineKeyboardButton('Изменить название🔁',
                                                                   callback_data=accept_callback.new(
                                                                       action='edit_name'))],
                                             [InlineKeyboardButton('Изменить описание🔁',
                                                                   callback_data=accept_callback.new(
                                                                       action='edit_description'))],
                                             [InlineKeyboardButton('Изменить фотографию🔁',
                                                                   callback_data=accept_callback.new(
                                                                       action='edit_photo'))],
                                             [InlineKeyboardButton('Отменить создание❌',
                                                                   callback_data=accept_callback.new(
                                                                        action='reject_item'))]
                                         ])
