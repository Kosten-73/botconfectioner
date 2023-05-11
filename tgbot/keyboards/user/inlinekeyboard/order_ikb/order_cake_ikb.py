from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

choice_subctg_cb = CallbackData('choice_subcategory_cake', 'subcategory')

choice_subcategory_cake_ikb = InlineKeyboardMarkup(row_width=1,
                                                   inline_keyboard=[
                                                       [InlineKeyboardButton('Бисквитный торт',
                                                                             callback_data=choice_subctg_cb.new(
                                                                                 subcategory='Бисквитный торт'))],
                                                       [InlineKeyboardButton('Бенто-торт',
                                                                             callback_data=choice_subctg_cb.new(
                                                                                 subcategory='Бенто-торт'))],
                                                       [InlineKeyboardButton('Муссовый торт',
                                                                             callback_data=choice_subctg_cb.new(
                                                                                 subcategory='Муссовый торт'))],
                                                       [InlineKeyboardButton('Отмена',
                                                                             callback_data='stop_order')]
                                                   ]
                                                   )

choice_filling_cake_cb = CallbackData('choice_filling_cake', 'filling')

choice_filling_cake_biscuit_ikb = InlineKeyboardMarkup(row_width=1,
                                                       inline_keyboard=[
                                                           [InlineKeyboardButton('Начинка 1',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 1'))],
                                                           [InlineKeyboardButton('Начинка 2',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 2'))],
                                                           [InlineKeyboardButton('Начинка 3',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 4'))],
                                                           [InlineKeyboardButton('Начинка 4',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 5'))],
                                                           [InlineKeyboardButton('Начинка 5',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 6'))],
                                                           [InlineKeyboardButton('Начинка 6',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 7'))],
                                                           [InlineKeyboardButton('Начинка 7',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 8'))],
                                                           [InlineKeyboardButton('Начинка 8',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 9'))],
                                                           [InlineKeyboardButton('Начинка 9',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 10'))],
                                                           [InlineKeyboardButton('Начинка 10',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 11'))],
                                                           [InlineKeyboardButton('Начинка 11',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 12'))],
                                                           [InlineKeyboardButton('Начинка 12',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 13'))],
                                                           [InlineKeyboardButton('Начинка 13',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 14'))],
                                                           [InlineKeyboardButton('Начинка 14',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 15'))],
                                                           [InlineKeyboardButton('Начинка 15',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 16'))],
                                                           [InlineKeyboardButton('Начинка 16',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 17'))],
                                                           [InlineKeyboardButton('Начинка 17',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 18'))],
                                                           [InlineKeyboardButton('Начинка 18',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 19'))],
                                                           [InlineKeyboardButton('Начинка 19',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 20'))],
                                                           [InlineKeyboardButton('Начинка 20',
                                                                                 callback_data=choice_filling_cake_cb.new(
                                                                                     filling='Начинка 1'))],
                                                           [InlineKeyboardButton('Отмена',
                                                                                 callback_data='stop_order')]
                                                       ]
                                                       )

choice_filling_bento_cake_ikb = InlineKeyboardMarkup(row_width=1,
                                                     inline_keyboard=[
                                                         [InlineKeyboardButton('Начинка 1',
                                                                               callback_data=choice_filling_cake_cb.new(
                                                                                   filling='Начинка 1'))],
                                                         [InlineKeyboardButton('Начинка 2',
                                                                               callback_data=choice_filling_cake_cb.new(
                                                                                   filling='Начинка 2'))],
                                                         [InlineKeyboardButton('Начинка 3',
                                                                               callback_data=choice_filling_cake_cb.new(
                                                                                   filling='Начинка 3'))],
                                                         [InlineKeyboardButton('Начинка 4',
                                                                               callback_data=choice_filling_cake_cb.new(
                                                                                   filling='Начинка 4'))],
                                                         [InlineKeyboardButton('Начинка 5',
                                                                               callback_data=choice_filling_cake_cb.new(
                                                                                   filling='Начинка 5'))],
                                                         [InlineKeyboardButton('Отмена',
                                                                               callback_data='stop_order')]
                                                     ]
                                                     )

choice_filling_cake_mousse_ikb = InlineKeyboardMarkup(row_width=1,
                                                      inline_keyboard=[
                                                          [InlineKeyboardButton('Начинка 1',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 1'))],
                                                          [InlineKeyboardButton('Начинка 2',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 2'))],
                                                          [InlineKeyboardButton('Начинка 3',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 3'))],
                                                          [InlineKeyboardButton('Начинка 4',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 4'))],
                                                          [InlineKeyboardButton('Начинка 5',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 5'))],
                                                          [InlineKeyboardButton('Начинка 6',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 6'))],
                                                          [InlineKeyboardButton('Начинка 7',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 7'))],
                                                          [InlineKeyboardButton('Начинка 8',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 8'))],
                                                          [InlineKeyboardButton('Начинка 9',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 9'))],
                                                          [InlineKeyboardButton('Начинка 10',
                                                                                callback_data=choice_filling_cake_cb.new(
                                                                                    filling='Начинка 10'))],
                                                          [InlineKeyboardButton('Отмена',
                                                                                callback_data='stop_order')]
                                                      ]
                                                      )

choice_value_cake_cb = CallbackData('choice_value_cake', 'value')

choice_value_cake_bis_mus_ikb = InlineKeyboardMarkup(row_width=1,
                                                     inline_keyboard=[
                                                         [InlineKeyboardButton('1 кг',
                                                                               callback_data=choice_value_cake_cb.new(
                                                                                   value='1 кг'))],
                                                         [InlineKeyboardButton('2 кг',
                                                                               callback_data=choice_value_cake_cb.new(
                                                                                   value='2 кг'))],
                                                         [InlineKeyboardButton('3 кг',
                                                                               callback_data=choice_value_cake_cb.new(
                                                                                   value='3 кг'))],
                                                         [InlineKeyboardButton('Отмена',
                                                                               callback_data='stop_order')]
                                                     ]
                                                     )

choice_value_bento_cake_ikb = InlineKeyboardMarkup(row_width=1,
                                                   inline_keyboard=[
                                                       [InlineKeyboardButton('Бенто-торт(400гр)',
                                                                             callback_data=choice_value_cake_cb.new(
                                                                                 value='Бенто-торт(400гр)'))],
                                                       [InlineKeyboardButton('Отмена',
                                                                             callback_data='stop_order')]
                                                   ]
                                                   )
