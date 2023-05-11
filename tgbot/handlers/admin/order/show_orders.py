from aiogram import Dispatcher, types
from aiogram.types import InputMedia

from tgbot.database.db_order import command_order as cmd_db
from tgbot.keyboards.admin.inlinekeyboard.order_ikb import get_order_keyboard, order_callback, order_ikb


async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.delete()
    amount = await cmd_db.count_orders()
    await callback.message.answer(f'На текущий момент, у вас: {amount}',
                                  reply_markup=order_ikb)


async def order_index(callback: types.CallbackQuery):
    from bot import bot
    await callback.message.delete()
    orders = await cmd_db.select_all_orders()
    order_data = orders[0]
    caption = f"Никнейм: {order_data.get('user_name')}\n" \
              f"Номер телефона: {order_data.get('user_phone')}\n" \
              f"Адрес: {order_data.get('user_address')}\n" \
              f"Что заказали: {order_data.get('category')}\n" \
              f"{order_data.get('subcategory')}\n" \
              f"С начинкой: {order_data.get('filling')}\n" \
              f"Количество: {order_data.get('value')}\n" \
              f"Принят в работу: {order_data.get('accept')}"
    count_items = await cmd_db.count_orders()
    keyboard = get_order_keyboard(count_items=count_items)
    await bot.send_photo(
        chat_id=callback.message.chat.id,
        photo=order_data.get("photo"),
        caption=caption,
        parse_mode="HTML",
        reply_markup=keyboard
    )


async def order_page_handler(query: types.CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))
    order = await cmd_db.select_all_orders()
    order_data = order[page]
    caption = f"Никнейм: {order_data.get('user_name')}\n" \
              f"Номер телефона: {order_data.get('user_phone')}\n" \
              f"Адрес: {order_data.get('user_address')}\n" \
              f"Что заказали: {order_data.get('category')}\n" \
              f"{order_data.get('subcategory')}\n" \
              f"С начинкой: {order_data.get('filling')}\n" \
              f"Количество: {order_data.get('value')}\n" \
              f"Принят в работу: {order_data.get('accept')}"
    count_items = await cmd_db.count_orders()
    keyboard = get_order_keyboard(page=page, count_items=count_items)
    photo = InputMedia(type="photo", media=order_data.get("photo"), caption=caption)

    await query.message.edit_media(photo, keyboard)


def register_show_order_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(order_index, text='all_orders', is_admin=True)
    dp.register_callback_query_handler(order_page_handler, order_callback.filter(action='follow'), is_admin=True)

    dp.register_callback_query_handler(back_to_menu, text='back_to_menu_order', is_admin=True)