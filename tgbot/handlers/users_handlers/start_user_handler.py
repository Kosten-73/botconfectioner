from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp


async def command_start(message: types.Message):
    await message.delete()
    await message.answer(f'Здравствуй, {message.from_user.full_name}, вас приветствует BotShadrCake'
                         f'Напиши команду /help чтобы узнать обо мне больше')


async def command_help(message: types.Message):
    await message.delete()
    await message.answer('Здесь будет описание функций')


def register_start_user_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, CommandStart())
    dp.register_message_handler(command_help, CommandHelp())

