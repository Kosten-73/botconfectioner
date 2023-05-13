from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

subctg_brownie_cb = CallbackData('subcategory_brownie', 'subcategory')

choice_subcategory_brownie_ikb = InlineKeyboardMarkup(row_width=1,
                                                      inline_keyboard=[
                                                          [InlineKeyboardButton('Мороженное(бисквитное)',
                                                                                callback_data=subctg_brownie_cb.new(
                                                                                    subcategory='Мороженное(бисквитное)'))],
                                                          [InlineKeyboardButton('Кейпопсы',
                                                                                callback_data=subctg_brownie_cb.new(
                                                                                    subcategory='Кейпопсы'))],
                                                          [InlineKeyboardButton('Муссовое пирожное(сердце)',
                                                                                callback_data=subctg_brownie_cb.new(
                                                                                    subcategory='Мус пирожное(сердце)'))],
                                                          [InlineKeyboardButton('Муссовое пирожное(квадрат)',
                                                                                callback_data=subctg_brownie_cb.new(
                                                                                    subcategory='Мус пирожное(квадрат)'))],
                                                          [InlineKeyboardButton('Отмена',
                                                                                callback_data='stop_order')]
                                                      ]
                                                      )

choice_filling_brownie_cb = CallbackData('filling_brownie', 'filling')

choice_brownie_ikb = InlineKeyboardMarkup(row_width=1,
                                          inline_keyboard=[
                                              [InlineKeyboardButton('Начинка 1',
                                                                    callback_data=choice_filling_brownie_cb.new(
                                                                        filling='Начинка 1'))],
                                              [InlineKeyboardButton('Отмена',
                                                                    callback_data='stop_order')]
                                          ])

choice_value_cb = CallbackData('choice_value', 'value')

choice_value_brownie_ikb = InlineKeyboardMarkup(row_width=1,
                                                inline_keyboard=[
                                                    [InlineKeyboardButton('6 штук',
                                                                          callback_data=choice_value_cb.new(
                                                                              value='6 штук'))],
                                                    [InlineKeyboardButton('8 штук',
                                                                          callback_data=choice_value_cb.new(
                                                                              value='8 штук'))],
                                                    [InlineKeyboardButton('10штук',
                                                                          callback_data=choice_value_cb.new(
                                                                              value='10 штук'))],
                                                    [InlineKeyboardButton('Отмена',
                                                                          callback_data='stop_order')]
                                                ]
                                                )
