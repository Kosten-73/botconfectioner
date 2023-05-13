from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext

from tgbot.filters.admin_check import AdminFilter
from tgbot.keyboards.admin.inlinekeyboard.main_ikb import ikb_for_portfolio, accept_callback
from tgbot.keyboards.admin.inlinekeyboard.portfolio_ikb import portfolio_ikb
from tgbot.keyboards.admin.keyboard.main_kb import cancel_kb
from tgbot.models.state import ItemStateGroup

from tgbot.database.db_portfolio import command_portfolio as cmd_db


async def menu_portfolio(callback: types.CallbackQuery):
    await callback.message.edit_text('Меню портфолио', reply_markup=portfolio_ikb)


async def cancel_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer('Вы отменили создание', reply_markup=portfolio_ikb)


async def add_item(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Напишите название', reply_markup=cancel_kb)
    await ItemStateGroup.item_name.set()


async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['item_name'] = message.text
    await message.answer('А теперь описание')
    await ItemStateGroup.item_description.set()


async def add_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['item_description'] = message.text
    await message.answer('Отправь фото')
    await ItemStateGroup.item_photo.set()


async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['item_photo'] = message.photo[0].file_id
    await message.answer_photo(photo=data['item_photo'],
                               caption=f"название: {data['item_name']}\n"
                                       f"описание: {data['item_description']}", reply_markup=ikb_for_portfolio)
    await ItemStateGroup.item_await.set()


async def accept_item(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete_reply_markup()
    async with state.proxy() as data:
        name = data['item_name']
        description = data['item_description']
        photo = data['item_photo']
    await cmd_db.add_item_db(item_name=name, item_description=description, item_photo=photo)
    await callback.message.answer('Меню портфолио', reply_markup=portfolio_ikb)
    await state.finish()


async def edit_name(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.answer('Пришлите новое название')
    await ItemStateGroup.item_name_edit.set()


async def add_edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['item_name'] = message.text
    await message.answer_photo(photo=data['item_photo'],
                               caption=f"название: {data['item_name']}\n"
                                       f"описание: {data['item_description']}", reply_markup=ikb_for_portfolio)

    await ItemStateGroup.item_await.set()


async def edit_description(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.answer('Пришлите новое описание')
    await ItemStateGroup.item_description_edit.set()


async def add_edit_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['item_description'] = message.text
    await message.answer_photo(photo=data['item_photo'],
                               caption=f"название: {data['item_name']}\n"
                                       f"описание: {data['item_description']}", reply_markup=ikb_for_portfolio)

    await ItemStateGroup.item_await.set()


async def edit_photo(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.answer('Пришлите новую фотографию')
    await ItemStateGroup.item_photo_edit.set()


async def add_edit_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['item_photo'] = message.photo[0].file_id
    await message.answer_photo(photo=data['item_photo'],
                               caption=f"название: {data['item_name']}\n"
                                       f"описание: {data['item_description']}", reply_markup=ikb_for_portfolio)

    await ItemStateGroup.item_await.set()


async def reject_item(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup()
    await callback.answer('Вы отменили создание', show_alert=True)
    await callback.message.answer('Меню портфолио', reply_markup=portfolio_ikb)
    await state.finish()


def register_portfolio_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_cmd, state='*', content_types=types.ContentType.ANY,
                                text='Отмена', is_admin=True)
    dp.register_callback_query_handler(menu_portfolio, text='open_portfolio', is_admin=True)

    dp.register_callback_query_handler(add_item, text='add_new_item', is_admin=True)
    dp.register_message_handler(add_name, state=ItemStateGroup.item_name, is_admin=True)
    dp.register_message_handler(add_description, state=ItemStateGroup.item_description, is_admin=True)
    dp.register_message_handler(add_photo, content_types=types.ContentType.PHOTO,
                                state=ItemStateGroup.item_photo, is_admin=True)

    dp.register_callback_query_handler(accept_item, accept_callback.filter(action='accept'), state='*', is_admin=True)

    dp.register_callback_query_handler(edit_name, accept_callback.filter(action='edit_name'), state='*', is_admin=True)
    dp.register_message_handler(add_edit_name, state=ItemStateGroup.item_name_edit, is_admin=True)

    dp.register_callback_query_handler(edit_description, accept_callback.filter(action='edit_description'), state='*', is_admin=True)
    dp.register_message_handler(add_edit_description, state=ItemStateGroup.item_description_edit, is_admin=True)

    dp.register_callback_query_handler(edit_photo,
                                       accept_callback.filter(action='edit_photo'), state='*', is_admin=True)
    dp.register_message_handler(add_edit_photo, state=ItemStateGroup.item_photo_edit,
                                content_types=types.ContentType.PHOTO, is_admin=True)

    dp.register_callback_query_handler(reject_item, accept_callback.filter(action='reject_item'),
                                       state='*', is_admin=True)
