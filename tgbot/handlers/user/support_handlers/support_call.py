from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatType

from tgbot.keyboards.user.inlinekeyboard.support_ikb import support_callback
from tgbot.models.state import SupportStateGroup


async def accept_call(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    from bot import dp, bot
    admin_id = callback_data['admin_id']
    user_id = callback.from_user.id
    await callback.message.answer('Вы находитесь в разговоре, просто пишите сообщения для общения')

    user_state = dp.current_state(chat=user_id, user=user_id)
    await user_state.set_state(state=SupportStateGroup.in_support_user)
    await user_state.update_data(admin_id=admin_id)

    await bot.send_message(chat_id=admin_id, text='Пользователь принял запрос')

    admin_state = dp.current_state(chat=admin_id, user=admin_id)
    await admin_state.set_state(state=SupportStateGroup.in_support_admin)
    await admin_state.update_data(user_id=user_id)




def register_support_call_user_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(accept_call, support_callback.filter(action='accept'))