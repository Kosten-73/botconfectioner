from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

choice_cb = CallbackData('choice', 'type', 'filling', 'value')

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

choice_order_ikb = InlineKeyboardMarkup(row_width=1,
                                       inline_keyboard=[
                                           [InlineKeyboardButton('Торт',
                                                                 callback_data=choice_cb.new(type='cake',
                                                                                             filling='-',
                                                                                             value='-'))],
                                           [InlineKeyboardButton('Капкейк',
                                                                 callback_data=choice_cb.new(type='cupcake',
                                                                                             filling='-',
                                                                                             value='-'))],
                                           [InlineKeyboardButton('Другое',
                                                                 callback_data=choice_cb.new(type='other',
                                                                                             filling='-',
                                                                                             value='-'))],
                                           [InlineKeyboardButton('Отмена',
                                                                 callback_data='stop_order')]
                                       ]
                                       )

filling_cake_ikb = InlineKeyboardMarkup(row_width=1,
                                       inline_keyboard=[
                                           [InlineKeyboardButton('Начинка 1',
                                                                 callback_data=choice_cb.new(type='fil_cake',
                                                                                             filling='filling1',
                                                                                             value='-'))],
                                           [InlineKeyboardButton('Начинка 2',
                                                                 callback_data=choice_cb.new(type='fil_cake',
                                                                                             filling='filling2',
                                                                                             value='-'))],
                                           [InlineKeyboardButton('Начина 3',
                                                                 callback_data=choice_cb.new(type='fil_cake',
                                                                                             filling='filling2',
                                                                                             value='-'))],
                                           [InlineKeyboardButton('Отмена',
                                                                 callback_data='stop_order')]
                                       ]
                                       )

value_cake_ikb = InlineKeyboardMarkup(row_width=1,
                                       inline_keyboard=[
                                           [InlineKeyboardButton('Бенто-торт',
                                                                 callback_data=choice_cb.new(type='val_cake',
                                                                                             filling='-',
                                                                                             value='bento'))],
                                           [InlineKeyboardButton('1 кг',
                                                                 callback_data=choice_cb.new(type='val_cake',
                                                                                             filling='-',
                                                                                             value='1kg'))],
                                           [InlineKeyboardButton('2 кг',
                                                                 callback_data=choice_cb.new(type='val_cake',
                                                                                             filling='-',
                                                                                             value='2kg'))],
                                           [InlineKeyboardButton('3 кг',
                                                                 callback_data=choice_cb.new(type='val_cake',
                                                                                             filling='-',
                                                                                             value='3kg'))],
                                           [InlineKeyboardButton('Отмена',
                                                                 callback_data='stop_order')]
                                       ]
                                       )


filling_cupcake_ikb = InlineKeyboardMarkup(row_width=1,
                                       inline_keyboard=[
                                           [InlineKeyboardButton('Начинка 1',
                                                                 callback_data=choice_cb.new(type='fil_cupcake',
                                                                                             filling='filling1',
                                                                                             value='-'))],
                                           [InlineKeyboardButton('Начинка 2',
                                                                 callback_data=choice_cb.new(type='fil_cupcake',
                                                                                             filling='filling2',
                                                                                             value='-'))],
                                           [InlineKeyboardButton('Начина 3',
                                                                 callback_data=choice_cb.new(type='fil_cupcake',
                                                                                             filling='filling2',
                                                                                             value='-'))],
                                           [InlineKeyboardButton('Отмена',
                                                                 callback_data='stop_order')]
                                       ]
                                       )

value_cupcake_ikb = InlineKeyboardMarkup(row_width=1,
                                       inline_keyboard=[
                                           [InlineKeyboardButton('2 штуки',
                                                                 callback_data=choice_cb.new(type='val_cupcake',
                                                                                             filling='-',
                                                                                             value='2pieces'))],
                                           [InlineKeyboardButton('4 штуки',
                                                                 callback_data=choice_cb.new(type='val_cupcake',
                                                                                             filling='-',
                                                                                             value='4pieces'))],
                                           [InlineKeyboardButton('6 штук',
                                                                 callback_data=choice_cb.new(type='val_cupcake',
                                                                                             filling='-',
                                                                                             value='6pieces'))],
                                           [InlineKeyboardButton('8 штук',
                                                                 callback_data=choice_cb.new(type='val_cupcake',
                                                                                             filling='-',
                                                                                             value='8pieces'))],
                                           [InlineKeyboardButton('Отмена',
                                                                 callback_data='stop_order')]
                                       ]
                                       )

accept_order_ikb = InlineKeyboardMarkup(row_width=1,
                                        inline_keyboard=[
                                            [InlineKeyboardButton('Принять и отправить кондитеру на рассмотрение',
                                                                  callback_data='accept')],
                                            [InlineKeyboardButton('Отменить заказ',
                                                                  callback_data='stop_order')]
                                        ])