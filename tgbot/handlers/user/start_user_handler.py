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
    await message.answer('<b>BotShadrcake</b> для начала работы, введите команду /start\n'
                         'Краткое описание функций:\n'
                         '<u><b>Посмотреть мои работы</b></u>- здесь вы можете ознакомится с портфолио кондитера\n'
                         '<u><b>Сделать заказ</b></u> - здесь вы можете оформить свой заказ\n'
                         '<u><b>Посмотреть мой текущий заказ</b></u> - здесь вы можете посмотреть ваш текущий заказ,'
                         ' если вы уже оформили его\n'
                         '<u><b>Связаться с кондитером</b></u> - нажав на эту кнопку, вы сможете напрямую'
                         ' связаться с кондитером и поговорить с ним внутри бота\n')


def register_start_user_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, CommandStart(), state='*')
    dp.register_message_handler(command_help, CommandHelp())
