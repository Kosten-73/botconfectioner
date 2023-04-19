from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from tgbot.keyboards.user.inlinekeyboard.main_menu_ikb import main_menu_ikb


async def command_start(message: types.Message):
    await message.delete()
    await message.answer(f'Здравствуй, {message.from_user.full_name}, вас приветствует <b>BotShadrCake</b>\n'
                         f'Напиши команду /help чтобы узнать обо мне больше', parse_mode='HTML')
    await message.answer('Главное меню бота', reply_markup=main_menu_ikb)


async def command_help(message: types.Message):
    await message.delete()
    await message.answer('Здесь будет описание функций')


async def contact_katya_cb(callback: types.CallbackQuery):
    await callback.message.answer('Здесь будут ссылки для связи с тобой')


async def contact_katya_m(message: types.Message):
    await message.delete()
    await message.answer('Здесь будут ссылки для связи с тобой')


def register_start_user_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, CommandStart())
    dp.register_message_handler(command_help, CommandHelp())
    dp.register_callback_query_handler(contact_katya_cb, text='contact_to_Katya')
    dp.register_message_handler(contact_katya_m, commands='contact')


