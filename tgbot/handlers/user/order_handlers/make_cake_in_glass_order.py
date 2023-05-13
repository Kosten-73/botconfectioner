from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.user.inlinekeyboard.order_ikb.order_cake_glass_ikb import \
    choice_biscuit_trifles_filling_glass_ikb, choice_mousse_trifles_filling_ikb, choice_bento_cake_in_glass_ikb, \
    choice_cupcake_in_glass_ikb, subctg_glass_cb, choice_subctg_cake_glass_ikb, choice_value_cake_glass_ikb, \
    choice_value_bento_cake_glass_ikb, choice_value_cb, choice_filling_glass_cb
from tgbot.keyboards.user.inlinekeyboard.order_ikb.order_main_ikb import choice_category_cb, stop_ikb, accept_ikb
from tgbot.misc.info_item import cake_in_glass_info, biscuit_trifles_filling_info, mousse_trifles_filling_info, \
    bento_cake_in_glass_info, cupcake_in_glass_info
from tgbot.models.state import OrderStateGroup


async def choice_subcategory_cake_in_glass_order(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await callback.message.edit_text(text=cake_in_glass_info,
                                     reply_markup=choice_subctg_cake_glass_ikb)
    category = callback_data.get('category')
    async with state.proxy() as data:
        data['category'] = category
    await OrderStateGroup.subcategory.set()


async def choice_filling_cake_in_glass_order(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    subcategory = callback_data.get('subcategory')
    async with state.proxy() as data:
        data['subcategory'] = subcategory

    if subcategory == 'Трайфлы бисквитные':
        filling_info = biscuit_trifles_filling_info
        filling_ikb = choice_biscuit_trifles_filling_glass_ikb
    elif subcategory == 'Трайфлы муссовые':
        filling_info = mousse_trifles_filling_info
        filling_ikb = choice_mousse_trifles_filling_ikb
    elif subcategory == 'Бенто-торт в стакане':
        filling_info = bento_cake_in_glass_info
        filling_ikb = choice_bento_cake_in_glass_ikb
    elif subcategory == 'Капкейки':
        filling_info = cupcake_in_glass_info
        filling_ikb = choice_cupcake_in_glass_ikb
    else:
        return

    await callback.message.edit_text(text=filling_info, reply_markup=filling_ikb)
    await OrderStateGroup.filling.set()


async def choice_value_cake_in_glass_order(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    filling = callback_data.get('filling')
    async with state.proxy() as data:
        data['filling'] = filling
        subcategory = data['subcategory']
    if subcategory in ['Трайфлы бисквитные', 'Трайфлы муссовые', 'Капкейки']:
        await callback.message.edit_text(text='Выберете необходимое колличество',
                                         reply_markup=choice_value_cake_glass_ikb)

    elif subcategory == 'Бенто-торт в стакане':
        await callback.message.edit_text(text='Выберете размер торта',
                                         reply_markup=choice_value_bento_cake_glass_ikb)
    else:
        return
    await OrderStateGroup.value.set()


def register_make_cake_in_glass_order_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(choice_subcategory_cake_in_glass_order,
                                       choice_category_cb.filter(category='Торт в стакане'),
                                       state=OrderStateGroup.category)

    dp.register_callback_query_handler(choice_filling_cake_in_glass_order, subctg_glass_cb.filter(),
                                       state=OrderStateGroup.subcategory)

    dp.register_callback_query_handler(choice_value_cake_in_glass_order, choice_filling_glass_cb.filter(),
                                       state=OrderStateGroup.filling)