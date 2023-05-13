from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

subctg_glass_cb = CallbackData('subcategory_glass', 'subcategory')

choice_subctg_cake_glass_ikb = InlineKeyboardMarkup(row_width=1,
                                                            inline_keyboard=[
                                                                [InlineKeyboardButton('Трайфлы бисквитные',
                                                                                      callback_data=subctg_glass_cb.new(
                                                                                          subcategory='Трайфлы бисквитные'))],
                                                                [InlineKeyboardButton('Трайфлы муссовые',
                                                                                      callback_data=subctg_glass_cb.new(
                                                                                          subcategory='Трайфлы муссовые'))],
                                                                [InlineKeyboardButton('Бенто-торт в стакане',
                                                                                      callback_data=subctg_glass_cb.new(
                                                                                          subcategory='Бенто-торт в стакане'))],
                                                                [InlineKeyboardButton('Капкейки',
                                                                                      callback_data=subctg_glass_cb.new(
                                                                                          subcategory='Капкейки'))],
                                                                [InlineKeyboardButton('Отмена',
                                                                                      callback_data='stop_order')]
                                                            ]
                                                            )

choice_filling_glass_cb = CallbackData('filling_glass', 'filling')

choice_biscuit_trifles_filling_glass_ikb = InlineKeyboardMarkup(row_width=1,
                                                   inline_keyboard=[
                                                       [InlineKeyboardButton('Начинка 1',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 1'))],
                                                       [InlineKeyboardButton('Начинка 2',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 2'))],
                                                       [InlineKeyboardButton('Начинка 3',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 3'))],
                                                       [InlineKeyboardButton('Начинка 4',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 4'))],
                                                       [InlineKeyboardButton('Начинка 5',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 5'))],
                                                       [InlineKeyboardButton('Начинка 6',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 6'))],
                                                       [InlineKeyboardButton('Начинка 7',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 7'))],
                                                       [InlineKeyboardButton('Отмена',
                                                                             callback_data='stop_order')]
                                                       ])

choice_mousse_trifles_filling_ikb = InlineKeyboardMarkup(row_width=1,
                                                         inline_keyboard=[
                                                       [InlineKeyboardButton('Начинка 1',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 1'))],
                                                       [InlineKeyboardButton('Начинка 2',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 2'))],
                                                       [InlineKeyboardButton('Начинка 3',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 3'))],
                                                       [InlineKeyboardButton('Начинка 4',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 4'))],
                                                       [InlineKeyboardButton('Начинка 5',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 5'))],
                                                       [InlineKeyboardButton('Начинка 6',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 6'))],
                                                       [InlineKeyboardButton('Начинка 7',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 7'))],
                                                       [InlineKeyboardButton('Отмена',
                                                                             callback_data='stop_order')]
                                                       ])

choice_bento_cake_in_glass_ikb = InlineKeyboardMarkup(row_width=1,
                                                   inline_keyboard=[
                                                       [InlineKeyboardButton('Начинка 1',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 1'))],
                                                       [InlineKeyboardButton('Начинка 2',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 2'))],
                                                       [InlineKeyboardButton('Начинка 3',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 3'))],
                                                       [InlineKeyboardButton('Отмена',
                                                                             callback_data='stop_order')]
                                                       ])

choice_cupcake_in_glass_ikb = InlineKeyboardMarkup(row_width=1,
                                                   inline_keyboard=[
                                                       [InlineKeyboardButton('Начинка 1',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 1'))],
                                                       [InlineKeyboardButton('Начинка 2',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 2'))],
                                                       [InlineKeyboardButton('Начинка 3',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 3'))],
                                                       [InlineKeyboardButton('Начинка 4',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 4'))],
                                                       [InlineKeyboardButton('Начинка 5',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 5'))],
                                                       [InlineKeyboardButton('Начинка 6',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 6'))],
                                                       [InlineKeyboardButton('Начинка 7',
                                                                             callback_data=choice_filling_glass_cb.new(
                                                                                 filling='Начинка 7'))],
                                                       [InlineKeyboardButton('Отмена',
                                                                             callback_data='stop_order')]
                                                       ])

choice_value_cb = CallbackData('choice_value', 'value')

choice_value_cake_glass_ikb = InlineKeyboardMarkup(row_width=1,
                                                     inline_keyboard=[
                                                         [InlineKeyboardButton('4 штуки',
                                                                               callback_data=choice_value_cb.new(
                                                                                   value='4 штуки'))],
                                                         [InlineKeyboardButton('6 штук',
                                                                               callback_data=choice_value_cb.new(
                                                                                   value='6 штук'))],
                                                         [InlineKeyboardButton('8 штук',
                                                                               callback_data=choice_value_cb.new(
                                                                                   value='8 штук'))],
                                                         [InlineKeyboardButton('Отмена',
                                                                               callback_data='stop_order')]
                                                     ]
                                                     )

choice_value_bento_cake_glass_ikb = InlineKeyboardMarkup(row_width=1,
                                                   inline_keyboard=[
                                                       [InlineKeyboardButton('Бенто-торт(400гр)',
                                                                             callback_data=choice_value_cb.new(
                                                                                 value='Бенто-торт(400гр)'))],
                                                       [InlineKeyboardButton('Отмена',
                                                                             callback_data='stop_order')]
                                                   ]
                                                   )
