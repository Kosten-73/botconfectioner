from aiogram import Dispatcher, types

from tgbot.keyboards.admin.inlinekeyboard.support_ikb import support_call_id_callback
from tgbot.keyboards.user.keyboard.support_kb import get_stop_sup_kb
from tgbot.models.state import SupportStateGroup


async def cancel_sup_call(callback: types.CallbackQuery, callback_data: dict):
    from bot import bot, dp
    await callback.message.edit_text('Вы отклонили запрос на диалог')
    user_id = callback_data.get('user_id')
    user_state = dp.current_state(user=user_id, chat=user_id)
    message = await user_state.get_data('message_id')
    await bot.delete_message(chat_id=user_id, message_id=message.get('message_id'))
    await user_state.finish()

    await bot.send_message(chat_id=user_id, text='Кондитер отклонил ваш запрос на диалог, попробуйте позже')


async def accept_sup_call(callback: types.CallbackQuery, callback_data: dict):
    from bot import dp, bot
    await callback.answer()
    await callback.message.delete()
    user_id = callback_data['user_id']
    admin_id = callback.from_user.id
    await callback.message.answer('Вы находитесь в разговоре, просто пишите сообщения для общения',
                                  reply_markup=get_stop_sup_kb)

    user_state = dp.current_state(chat=user_id, user=user_id)
    await user_state.set_state(state=SupportStateGroup.in_support_user)
    await user_state.update_data(admin_id=admin_id)

    message = await user_state.get_data('message_id')
    await bot.delete_message(chat_id=user_id, message_id=message.get('message_id'))
    await bot.send_message(chat_id=user_id, text='Кондитер принял ваш запрос, для общения пишите в чат',
                           reply_markup=get_stop_sup_kb)

    admin_state = dp.current_state(chat=admin_id, user=admin_id)
    await admin_state.set_state(state=SupportStateGroup.in_support_admin)
    await admin_state.update_data(user_id=user_id)


def register_support_main_admin_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(cancel_sup_call, support_call_id_callback.filter(action='cancel'))
    dp.register_callback_query_handler(accept_sup_call, support_call_id_callback.filter(action='accept'))