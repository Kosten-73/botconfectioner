from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.admin.inlinekeyboard.order_ikb import order_callback, support_user_callback
from tgbot.database.db_order import command_order as cmd_db
from tgbot.keyboards.admin.inlinekeyboard.support_ikb import cancel_sup_admin_ikb
from tgbot.keyboards.user.inlinekeyboard.support_ikb import get_keyboard_accept_sup_user_ikb
from tgbot.models.state import SupportStateGroup


async def cancel_sup_admin(callback: types.CallbackQuery, state: FSMContext):
    from bot import dp, bot
    await callback.message.edit_text('Вы отменили диалог с пользователем')
    data = await state.get_data('user_id')
    await bot.send_message(chat_id=data['user_id'], text='К сожалению, кондитер уже отменил диалог')
    await state.finish()


async def link_to_user(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    from bot import dp, bot
    await callback.message.answer('Вы отправили запрос на диалог пользователю, ожидайте его ответ',
                                  reply_markup=cancel_sup_admin_ikb)
    page = int(callback_data.get("page"))
    order = await cmd_db.select_all_orders()
    order_data = order[page-1]
    admin_id = callback.from_user.id
    user_id = order_data.get('user_id')
    await bot.send_message(chat_id=user_id, text='С вами хочет связаться кондитер,'
                                                 'нажмите на кнопку чтобы открыть диалог',
                           reply_markup=get_keyboard_accept_sup_user_ikb(admin_id=admin_id))
    admin_state = dp.current_state(chat=admin_id, user=admin_id)
    await admin_state.set_state(state=SupportStateGroup.wait_accept_to_user)
    async with admin_state.proxy() as data:
        data['user_id'] = user_id

    await state.set_state('wait_accept_sup')
    async with state.proxy() as data:
        data['user_id'] = user_id


async def link_to_user_new_order(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    from bot import dp, bot
    await callback.message.answer('Вы отправили запрос на диалог пользователю, ожидайте его ответ',
                                  reply_markup=cancel_sup_admin_ikb)

    admin_id = callback.from_user.id
    user_id = callback_data.get('user_id')
    await bot.send_message(chat_id=user_id, text='С вами хочет связаться кондитер,'
                                                 'нажмите на кнопку чтобы открыть диалог',
                           reply_markup=get_keyboard_accept_sup_user_ikb(admin_id=admin_id))
    admin_state = dp.current_state(chat=admin_id, user=admin_id)
    await admin_state.set_state(state=SupportStateGroup.wait_accept_to_user)
    async with admin_state.proxy() as data:
        data['user_id'] = user_id

    await state.set_state('wait_accept_sup')
    async with state.proxy() as data:
        data['user_id'] = user_id


def register_support_call_admin_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(link_to_user, order_callback.filter(action='link_user'), is_admin=True)
    dp.register_callback_query_handler(cancel_sup_admin, state='wait_accept_sup',
                                       text='stop_wait', is_admin=True)
    dp.register_callback_query_handler(link_to_user_new_order, support_user_callback.filter(), is_admin=True)
