from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

stop_ikb = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[[InlineKeyboardButton('Отмена',
                                                                       callback_data='stop_order')]])

accept_ikb = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[
                                      [InlineKeyboardButton('Продолжить создание заказа',
                                                            callback_data='continue')],
                                      [InlineKeyboardButton('Отмена',
                                                            callback_data='stop_order')]
                                  ])

accept_order_ikb = InlineKeyboardMarkup(row_width=1,
                                        inline_keyboard=[
                                            [InlineKeyboardButton('Принять и отправить кондитеру на рассмотрение',
                                                                  callback_data='accept')],
                                            [InlineKeyboardButton('Отменить заказ',
                                                                  callback_data='stop_order')]
                                        ])

choice_category_cb = CallbackData('choice_category', 'category')

choice_category_ikb = InlineKeyboardMarkup(row_width=1,
                                           inline_keyboard=[
                                               [InlineKeyboardButton('Торт',
                                                                     callback_data=choice_category_cb.new(
                                                                         category='Торт'))],
                                               [InlineKeyboardButton('Торт в стакане',
                                                                     callback_data=choice_category_cb.new(
                                                                         category='Торт в стакане'))],
                                               [InlineKeyboardButton('Пирожное',
                                                                     callback_data=choice_category_cb.new(
                                                                         category='Пирожное'))],
                                               [InlineKeyboardButton('Отмена',
                                                                     callback_data='stop_order')]
                                           ]
                                           )