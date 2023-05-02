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


def register_start_user_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, CommandStart())
    dp.register_message_handler(command_help, CommandHelp())
