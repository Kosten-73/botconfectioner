from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.admin.inlinekeyboard.main_ikb import main_menu_ikb


async def command_start (message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer(f'Здравствуйте, администратор {message.from_user.full_name}\n'
                         f'нажмите команду /help_admin для того чтобы узнать больше')
    await message.answer('Главное меню администратора:',
                         reply_markup=main_menu_ikb)


async def command_help(message: types.Message):
    await message.delete()
    await message.answer('Для открытия панели администратора введите команду: /admin_start\n'
                         '<b>📕Портфолио📕</b> - Здесь вы сможете просмотреть и добавить работу в свое портфолио,'
                         'а так же редактировать уже существующие работы.\n'
                         '<b>📍Ваши заказы📍</b> - здесь вы можете просмотреть текущие заказы, принять новый заказ,'
                         'а так же связаться с заказчиком по средствам диалога')


async def open_admin_panel_cb(callback: types.CallbackQuery):
    await callback.message.edit_text('Главное меню администратора:',
                                     reply_markup=main_menu_ikb)


def register_start_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start_admin', is_admin=True)
    dp.register_message_handler(command_help, commands='help_admin', is_admin=True)
    dp.register_callback_query_handler(open_admin_panel_cb, text='back', is_admin=True, state='*')
