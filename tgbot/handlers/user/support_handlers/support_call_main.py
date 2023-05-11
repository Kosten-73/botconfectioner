from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from tgbot.config import support_id
from tgbot.keyboards.admin.inlinekeyboard.support_ikb import get_accept_to_sup_call_ikb
from tgbot.keyboards.user.inlinekeyboard.support_ikb import get_cancel_wait_sup_keyboard, support_callback


async def stop_wait_sup_call(callback: types.CallbackQuery, callback_data: dict):
    from bot import dp, bot
    admin_id = callback_data.get('admin_id')
    await bot.send_message(chat_id=admin_id, text='Человек передумал с вами разговаривать',
                           reply_markup=ReplyKeyboardRemove())

    await callback.message.edit_text('Вы отменили разговор с кондитером')


async def link_to_support_call(callback: types.CallbackQuery, state: FSMContext):
    from bot import bot, dp
    user_id = callback.from_user.id
    admin_id = support_id
    admin_state = dp.current_state(chat=admin_id, user=admin_id)
    admin_state_now = await admin_state.get_state()
    if admin_state_now is not None:
        await callback.message.answer('Извините, кондитер сейчас занят, попробуйте позже')
        return

    await bot.send_message(chat_id=admin_id, text='С вами хочет пообщаться человек',
                           reply_markup=get_accept_to_sup_call_ikb(user_id=user_id))

    user_state = dp.current_state(chat=user_id, user=user_id)
    await user_state.set_state('wait_to_accept')
    await callback.message.answer('Ожидайте ответа от кондитера или нажмите отмена',
                                  reply_markup=get_cancel_wait_sup_keyboard(admin_id=admin_id))


def register_support_main_user_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(link_to_support_call, text='link_support_call')
    dp.register_callback_query_handler(stop_wait_sup_call, support_callback.filter(action='stop_wait_user'))