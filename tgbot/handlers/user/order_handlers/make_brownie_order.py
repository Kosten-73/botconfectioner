from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.user.inlinekeyboard.order_ikb.order_browie_Ikb import choice_subcategory_brownie_ikb, \
    subctg_brownie_cb, choice_value_brownie_ikb, choice_filling_brownie_cb, \
    choice_value_cb, choice_brownie_ikb
from tgbot.keyboards.user.inlinekeyboard.order_ikb.order_main_ikb import choice_category_cb, stop_ikb, accept_ikb
from tgbot.misc.info_item import brownie_info, ice_cream_biscuit_filling_info, keypops_filling_info, \
    square_cake_heart_info, mousse_cake_heart_info
from tgbot.models.state import OrderStateGroup


async def choice_subcategory_brownie_order(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await callback.message.edit_text(text=brownie_info,
                                     reply_markup=choice_subcategory_brownie_ikb)
    category = callback_data.get('category')
    async with state.proxy() as data:
        data['category'] = category
    await OrderStateGroup.subcategory.set()


async def choice_filling_brownie_order(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    subcategory = callback_data.get('subcategory')
    async with state.proxy() as data:
        data['subcategory'] = subcategory

    if subcategory == 'Мороженное(бисквитное)':
        filling_info = ice_cream_biscuit_filling_info
        filling_ikb = choice_brownie_ikb
    elif subcategory == 'Кейпопсы':
        filling_info = keypops_filling_info
        filling_ikb = choice_brownie_ikb
    elif subcategory == 'Мус пирожное(сердце)':
        filling_info = mousse_cake_heart_info
        filling_ikb = choice_brownie_ikb
    elif subcategory == 'Мус пирожное(квадрат)':
        filling_info = square_cake_heart_info
        filling_ikb = choice_brownie_ikb
    else:
        return

    await callback.message.edit_text(text=filling_info, reply_markup=filling_ikb)
    await OrderStateGroup.filling.set()


async def choice_value_cake_brownie_order(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    filling = callback_data.get('filling')
    async with state.proxy() as data:
        data['filling'] = filling
        await callback.message.edit_text(text='Выберете необходимое количество',
                                         reply_markup=choice_value_brownie_ikb)

    await OrderStateGroup.value.set()


def register_make_brownie_order_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(choice_subcategory_brownie_order,
                                       choice_category_cb.filter(category='Пирожное'),
                                       state=OrderStateGroup.category)

    dp.register_callback_query_handler(choice_filling_brownie_order, subctg_brownie_cb.filter(),
                                       state=OrderStateGroup.subcategory)

    dp.register_callback_query_handler(choice_value_cake_brownie_order, choice_filling_brownie_cb.filter(),
                                       state=OrderStateGroup.filling)