from aiogram import Dispatcher, types

from tgbot.filters.admin_check import AdminFilter
from tgbot.database.db_order import command_order as cmd_db
from tgbot.keyboards.admin.inlinekeyboard.order_ikb import order_ikb, order_callback


async def open_list_order(callback: types.CallbackQuery):
    amount = await cmd_db.count_orders()
    await callback.message.edit_text(f'На текущий момент, у вас: {amount}',
                                     reply_markup=order_ikb)


async def delete_order(callback: types.CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))
    orders = await cmd_db.select_all_orders()
    order_data = orders[page - 1]
    user_id = order_data.get("user_id")
    await cmd_db.delete_order(user_id)
    await callback.answer('Заказ удален', show_alert=True)


async def accept_pay_order(callback: types.CallbackQuery, callback_data: dict):
    from bot import bot
    page = int(callback_data.get("page"))
    orders = await cmd_db.select_all_orders()
    order_data = orders[page - 1]
    user_id = order_data.get("user_id")
    accept = '✅'
    await cmd_db.update_state_order(user_id, accept)
    await callback.answer('Заказ принят в работу, заказчику отправлено уведомление', show_alert=True)
    await bot.send_photo(chat_id=user_id, photo=order_data.get('photo'),
                         caption=f"Кондитер принял ваш заказа в работу\n"
                                 f"Никнейм: {order_data.get('user_name')}\n" \
                                 f"Номер телефона: {order_data.get('user_phone')}\n" \
                                 f"Адрес: {order_data.get('user_address')}\n" \
                                 f"Что заказали: {order_data.get('product')}\n" \
                                 f"С начинкой: {order_data.get('filling')}\n" \
                                 f"Количество: {order_data.get('value')}\n" \
                                 f"Принят в работу: {accept}")


def register_main_order_handlers (dp: Dispatcher):
    dp.register_callback_query_handler(open_list_order, text='open_order', is_admin=True)
    dp.register_callback_query_handler(delete_order, order_callback.filter(action='delete_order'), is_admin=True)
    dp.register_callback_query_handler(accept_pay_order,
                                       order_callback.filter(action='accept_pay_order'), is_admin=True)
