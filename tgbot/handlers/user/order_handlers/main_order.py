from aiogram import Dispatcher, types
from tgbot.keyboards.user.inlinekeyboard.main_menu_ikb import back_button, back_button_order, main_menu_ikb
from tgbot.database.db_order import command_order as cmd_db


async def show_my_order(callback: types.CallbackQuery):
    orders = await cmd_db.select_one_order(user_id=callback.from_user.id)
    if not orders:
        await callback.answer('На данный момент у вас нет заказов')
        return False
    await callback.message.delete()
    order_data = orders[0]
    photo = order_data['photo']
    caption = f"Никнейм: {order_data['user_name']}\n" \
              f"Номер телефона: {order_data['user_phone']}\n" \
              f"Адрес: {order_data['user_address']}\n" \
              f"Что заказали: {order_data['category']}\n" \
              f"{order_data['subcategory']}\n" \
              f"С начинкой: {order_data['filling']}\n" \
              f"Количество: {order_data['value']}\n" \
              f"Принят в работу: {order_data['accept']}"
    if order_data['accept'] == '❌':
        await callback.message.answer_photo(photo=photo,
                                            caption=caption,
                                            reply_markup=back_button_order)
        return False
    else:
        await callback.message.answer_photo(photo=photo,
                                            caption=caption,
                                            reply_markup=back_button)


async def delete_my_order(callback: types.CallbackQuery):
    await callback.message.delete()
    user_id = callback.from_user.id
    await cmd_db.delete_order(user_id)
    await callback.answer('Ваш заказ удалено до принятия его в работу', show_alert=True)
    await callback.message.answer('Главное меню бота', reply_markup=main_menu_ikb)


def register_main_order_user_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(show_my_order, text='show_my_order')
    dp.register_callback_query_handler(delete_my_order, text='delete_my_order')