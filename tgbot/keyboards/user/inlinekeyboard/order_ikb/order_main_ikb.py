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

categories = {
    'milk': 'Молочная продукция',
    'chocolate': 'Шоколад и какао продукты',
    'ingredients': 'Пищевые ингредиенты',
    'decor': 'Декор',
    'dyes': 'Красители',
    'packaging': 'Упаковка',
    'bags_tips': 'Кондитерские мешки, насадки',
    'print': 'Пищевая печать',
    'celebration': 'Товары для праздника',
    'inventory': 'Инвентарь'
}

choice_category_ikb = InlineKeyboardMarkup(row_width=1,
                                           inline_keyboard=[
                                               [InlineKeyboardButton(categories['milk'], callback_data=choice_category_cb.new(category='milk'))],
                                               [InlineKeyboardButton(categories['chocolate'], callback_data=choice_category_cb.new(category='chocolate'))],
                                               [InlineKeyboardButton(categories['ingredients'], callback_data=choice_category_cb.new(category='ingredients'))],
                                               [InlineKeyboardButton(categories['decor'], callback_data=choice_category_cb.new(category='decor'))],
                                               [InlineKeyboardButton(categories['dyes'], callback_data=choice_category_cb.new(category='dyes'))],
                                               [InlineKeyboardButton(categories['packaging'], callback_data=choice_category_cb.new(category='packaging'))],
                                               [InlineKeyboardButton(categories['bags_tips'], callback_data=choice_category_cb.new(category='bags_tips'))],
                                               [InlineKeyboardButton(categories['print'], callback_data=choice_category_cb.new(category='print'))],
                                               [InlineKeyboardButton(categories['celebration'], callback_data=choice_category_cb.new(category='celebration'))],
                                               [InlineKeyboardButton(categories['inventory'], callback_data=choice_category_cb.new(category='inventory'))],
                                               [InlineKeyboardButton('Отмена', callback_data='stop_order')]
                                           ]
                                           )
