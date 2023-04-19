from aiogram import Dispatcher, types
from aiogram.types import InputMedia

from tgbot.filters.admin_check import AdminFilter
from tgbot.database.db_portfolio import command_portfolio as cmd_db
from tgbot.keyboards.admin.inlinekeyboard.portfolio_ikb import get_items_keyboard, item_callback, portfolio_ikb


async def return_menu_portfolio(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Меню портфолио',
                                  reply_markup=portfolio_ikb)

async def item_index(callback: types.CallbackQuery):
    from bot import bot
    await callback.message.delete()
    items = await cmd_db.select_all_item()
    item_data = items[0]
    caption = f"<b>{item_data.get('item_name')}</b>\n" \
              f"{item_data.get('item_description')}"
    count_items = await cmd_db.count_items()
    keyboard = get_items_keyboard(count_items=count_items)
    
    await bot.send_photo(
        chat_id=callback.message.chat.id,
        photo=item_data.get("item_photo"),
        caption=caption,
        parse_mode="HTML",
        reply_markup=keyboard
    )


async def item_page_handler(query: types.CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))
    items = await cmd_db.select_all_item()
    item_data = items[page]
    caption = f"<b>{item_data.get('item_name')}</b>\n" \
              f"{item_data.get('item_description')}"
    count_items = await cmd_db.count_items()
    keyboard = get_items_keyboard(page=page, count_items=count_items)
    photo = InputMedia(type="photo", media=item_data.get("item_photo"), caption=caption)

    await query.message.edit_media(photo, keyboard)


def register_show_portfolio_admin_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(item_index, AdminFilter(), text='show_portfolio')
    dp.register_callback_query_handler(item_page_handler, AdminFilter(), item_callback.filter(action='following'))

    dp.register_callback_query_handler(return_menu_portfolio, AdminFilter(), text='return_menu_portfolio')

