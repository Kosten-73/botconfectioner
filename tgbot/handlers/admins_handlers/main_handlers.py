from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from tgbot.filters.admin_check import AdminFilter
from tgbot.keyboards.admin.inlinekeyboard.main_ikb import main_menu_ikb
from tgbot.keyboards.admin.keyboard.main_kb import main_menu_kb


async def command_start(message: types.Message):
    await message.delete()
    await message.answer(f'Здравствуйте, администратор {message.from_user.full_name}\n'
                         f'нажмите команду /help для того чтобы узнать больше',
                         reply_markup=main_menu_kb)


async def command_help(message: types.Message):
    await message.delete()
    await message.answer('Здесь будет описание для админа')


async def open_admin_panel(message: types.Message):
    await message.answer('Админ панель:',
                         reply_markup=main_menu_ikb)


async def open_admin_panel_cb(callback: types.CallbackQuery):
    await callback.message.edit_text('Админ панель:',
                                  reply_markup=main_menu_ikb)


def register_start_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, AdminFilter(), commands='start_admin')
    dp.register_message_handler(command_help, AdminFilter(), commands='help_admin')
    dp.register_message_handler(open_admin_panel, AdminFilter(), text='Открыть панель управление')
    dp.register_callback_query_handler(open_admin_panel_cb, AdminFilter(), text='back')
