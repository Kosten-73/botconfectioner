from aiogram import Dispatcher, types

from tgbot.filters.admin_check import AdminFilter
from tgbot.keyboards.admin.inlinekeyboard.main_ikb import main_menu_ikb


async def command_start (message: types.Message):
    await message.delete()
    await message.answer(f'Здравствуйте, администратор {message.from_user.full_name}\n'
                         f'нажмите команду /help для того чтобы узнать больше')
    await message.answer('Админ панель:',
                         reply_markup=main_menu_ikb)


async def command_help(message: types.Message):
    await message.delete()
    await message.answer('Здесь будет описание для админа')


async def open_admin_panel_cb(callback: types.CallbackQuery):
    await callback.message.edit_text('Админ панель:',
                                     reply_markup=main_menu_ikb)


def register_start_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start_admin', is_admin=True)
    dp.register_message_handler(command_help, commands='help_admin', is_admin=True)
    dp.register_callback_query_handler(open_admin_panel_cb, text='back', is_admin=True)
