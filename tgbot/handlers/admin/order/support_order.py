from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.filters.admin_check import AdminFilter
from tgbot.keyboards.admin.inlinekeyboard.order_ikb import order_callback
from tgbot.database.db_order import command_order as cmd_db
from tgbot.models.state import SupportStateGroup


async def link_to_user(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    from bot import dp, bot
    page = int(callback_data.get("page"))
    order = await cmd_db.select_all_orders()
    order_data = order[page-1]
    user_id = order_data.get('user_id')
    user_state = dp.current_state(chat=user_id, user=user_id)
    await user_state.set_state('in_support_user')
    await state.set_state('in_support_admin')
    async with state.proxy() as data:
        data['user_id'] = user_id
        data['admin_id'] = callback.message.from_user.id

    await callback.message.answer('Вы связались с пользователем')
    await bot.send_message(chat_id=user_id, text='с вами хочет связаться админ!')


async def admin_message_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    user_id = data['user_id']
    await message.copy_to(chat_id=user_id)

def register_support_order_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(link_to_user, AdminFilter(), order_callback.filter(action='link_user'))

    dp.register_message_handler(admin_message_handler, state='in_support_admin')



# проблема в состоянии пользователя!