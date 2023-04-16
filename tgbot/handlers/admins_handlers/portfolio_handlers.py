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
    await message.answer('А теперь отправь фото')
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
    await state.finish()


async def edit_name(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.answer('Пришлите другое название')
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
    await callback.message.answer('Пришлите другое описание')
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
    dp.register_message_handler(cancel_cmd, AdminFilter(), state='*', content_types=types.ContentType.ANY,
                                text='Отмена')
    dp.register_callback_query_handler(menu_portfolio, AdminFilter(), text='open_portfolio')

    dp.register_callback_query_handler(add_item, AdminFilter(), text='add_new_item')
    dp.register_message_handler(add_name, AdminFilter(), state=ItemStateGroup.item_name)
    dp.register_message_handler(add_description, AdminFilter(), state=ItemStateGroup.item_description)
    dp.register_message_handler(add_photo, AdminFilter(), content_types=types.ContentType.PHOTO,
                                state=ItemStateGroup.item_photo)

    dp.register_callback_query_handler(accept_item, AdminFilter(), accept_callback.filter(action='accept'), state='*')

    dp.register_callback_query_handler(edit_name, AdminFilter(), accept_callback.filter(action='edit_name'), state='*')
    dp.register_message_handler(add_edit_name, AdminFilter(), state=ItemStateGroup.item_name_edit)

    dp.register_callback_query_handler(edit_description, AdminFilter(), accept_callback.filter(action='edit_description'),state='*')
    dp.register_message_handler(add_edit_description, AdminFilter(), state=ItemStateGroup.item_description_edit)

    dp.register_callback_query_handler(edit_photo, AdminFilter(),
                                       accept_callback.filter(action='edit_photo'), state='*')
    dp.register_message_handler(add_edit_photo, AdminFilter(), state=ItemStateGroup.item_photo_edit,
                                content_types=types.ContentType.PHOTO)

    dp.register_callback_query_handler(reject_item, AdminFilter(), accept_callback.filter(action='reject_item'),
                                       state='*')
