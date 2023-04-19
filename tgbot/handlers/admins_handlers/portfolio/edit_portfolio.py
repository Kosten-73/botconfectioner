import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMedia

from tgbot.filters.admin_check import AdminFilter
from tgbot.database.db_portfolio import command_portfolio as cmd_db
from tgbot.keyboards.admin.inlinekeyboard.portfolio_ikb import get_items_keyboard, item_callback, portfolio_ikb
from tgbot.models.state import ItemStateGroup


async def item_delete_handler(callback: types.CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))
    items = await cmd_db.select_all_item()
    item_data = items[page - 1]
    item_name = item_data.get("item_name")
    await cmd_db.delete_item(item_name)
    await callback.answer('Объект удален', show_alert=True)


async def edit_name_item(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await callback.answer('Отправь новое название', show_alert=True)
    page = int(callback_data.get("page"))
    await ItemStateGroup.item_edit_name_in_db.set()
    async with state.proxy() as data:
        data['page'] = page


async def enter_new_name_item(message: types.Message, state: FSMContext):
    await message.delete()
    async with state.proxy() as data:
        data['item_name'] = message.text
    new_item_name = data['item_name']
    page = data['page']
    items = await cmd_db.select_all_item()
    item_data = items[page - 1]
    item_name = item_data.get("item_name")

    await cmd_db.update_name_item(item_name=item_name, new_item_name=new_item_name)
    await state.finish()
    delete_msg = await message.answer('Имя успешно изменено')
    await asyncio.sleep(5)
    await delete_msg.delete()


async def edit_description_item(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await callback.answer('Отправь новое описание', show_alert=True)
    page = int(callback_data.get("page"))
    await ItemStateGroup.item_edit_description_db.set()
    async with state.proxy() as data:
        data['page'] = page


async def enter_new_description_item(message: types.Message, state: FSMContext):
    await message.delete()
    async with state.proxy() as data:
        data['item_description'] = message.text
    new_item_description = data['item_description']
    page = data['page']
    items = await cmd_db.select_all_item()
    item_data = items[page - 1]
    item_name = item_data.get("item_name")
    await cmd_db.update_description_item(item_name=item_name, new_item_description=new_item_description)

    await state.finish()
    delete_msg = await message.answer('Описание успешно изменено')
    await asyncio.sleep(5)
    await delete_msg.delete()


async def edit_photo_item(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await callback.answer('Отправь новое фото', show_alert=True)
    page = int(callback_data.get("page"))
    await ItemStateGroup.item_edit_photo_in_db.set()
    async with state.proxy() as data:
        data['page'] = page


async def enter_new_photo_item(message: types.Message, state: FSMContext):
    await message.delete()
    async with state.proxy() as data:
        data['item_photo'] = message.photo[0].file_id
    new_item_photo = data['item_photo']
    page = data['page']
    items = await cmd_db.select_all_item()
    item_data = items[page - 1]
    item_name = item_data.get("item_name")
    await cmd_db.update_photo_item(item_name=item_name, new_item_photo=new_item_photo)

    await state.finish()
    delete_msg = await message.answer('Фото успешно изменено')
    await asyncio.sleep(5)
    await delete_msg.delete()


def register_edit_portfolio_admin_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(item_delete_handler, AdminFilter(), item_callback.filter(action='delete'))

    dp.register_callback_query_handler(edit_name_item, AdminFilter(), item_callback.filter(action='edit_name'))
    dp.register_message_handler(enter_new_name_item, AdminFilter(), state=ItemStateGroup.item_edit_name_in_db)

    dp.register_callback_query_handler(edit_description_item, AdminFilter(), item_callback.filter(action='edit_description'))
    dp.register_message_handler(enter_new_description_item, AdminFilter(), state=ItemStateGroup.item_edit_description_db)

    dp.register_callback_query_handler(edit_photo_item, AdminFilter(),
                                       item_callback.filter(action='edit_photo'))
    dp.register_message_handler(enter_new_photo_item, AdminFilter(),
                                state=ItemStateGroup.item_edit_photo_in_db, content_types=types.ContentTypes.PHOTO)