from aiogram import Dispatcher, types
from aiogram.types import InputMedia

from tgbot.database.db_portfolio import command_portfolio as cmd_db
from tgbot.keyboards.user.inlinekeyboard.main_menu_ikb import main_menu_ikb
from tgbot.keyboards.user.inlinekeyboard.portfolio_ikb import get_items_keyboard_user, item_callback


async def return_to_main_menu(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Главное меню бота', reply_markup=main_menu_ikb)


async def item_index(callback: types.CallbackQuery):
    from bot import bot
    await callback.message.delete()
    items = await cmd_db.select_all_item()
    item_data = items[0]
    caption = f"<b>{item_data.get('item_name')}</b>\n" \
              f"{item_data.get('item_description')}"
    count_items = await cmd_db.count_items()
    keyboard = get_items_keyboard_user(count_items=count_items)

    await bot.send_photo(
        chat_id=callback.message.chat.id,
        photo=item_data.get("item_photo"),
        caption=caption,
        parse_mode="HTML",
        reply_markup=keyboard
    )


async def item_page_handler (query: types.CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))
    items = await cmd_db.select_all_item()
    item_data = items[page]
    caption = f"<b>{item_data.get('item_name')}</b>\n" \
              f"{item_data.get('item_description')}"
    count_items = await cmd_db.count_items()
    keyboard = get_items_keyboard_user(page=page, count_items=count_items)
    photo = InputMedia(type="photo", media=item_data.get("item_photo"), caption=caption)

    await query.message.edit_media(photo, keyboard)


def register_show_portfolio_user_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(item_index, text='show_portfolio_user')
    dp.register_callback_query_handler(item_page_handler, item_callback.filter())

    dp.register_callback_query_handler(return_to_main_menu, text='return_main_menu')




