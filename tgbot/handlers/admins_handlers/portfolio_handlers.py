from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.filters.admin_check import AdminFilter
from tgbot.keyboards.admin.inlinekeyboard.portfolio_ikb import portfolio_ikb
from tgbot.keyboards.admin.keyboard.main_kb import cancel_kb
from tgbot.models.state import ItemStateGroup

from tgbot.database.db_portfolio import command_portfolio as cmd_db


async def menu_portfolio(callback: types.CallbackQuery):
    await callback.message.edit_text('Меню портфолио', reply_markup=portfolio_ikb)


async def cancel_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Вы отменили создание', reply_markup=portfolio_ikb)


async def add_new_item(callback: types.CallbackQuery):
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
    name = data['item_name']
    description = data['item_description']
    photo = data['item_photo']

    await cmd_db.add_item_db(item_name=name, item_description=description, item_photo=photo)

    await message.answer_photo(photo=photo,
                               caption=f'название: {name}\n'
                                       f'описание: {description}')
    await state.finish()


def register_portfolio_admin_handlers (dp: Dispatcher):
    dp.register_callback_query_handler(menu_portfolio, AdminFilter(), text='open_portfolio')
    dp.register_callback_query_handler(add_new_item, AdminFilter(), text='add_new_item')
    dp.register_message_handler(cancel_cmd, AdminFilter(), state='*', content_types=types.ContentType.ANY,
                                text='Отмена')

    dp.register_message_handler(add_name, AdminFilter(), state=ItemStateGroup.item_name)
    dp.register_message_handler(add_description, AdminFilter(), state=ItemStateGroup.item_description)
    dp.register_message_handler(add_photo, AdminFilter(), content_types=types.ContentType.PHOTO,
                                state=ItemStateGroup.item_photo)

