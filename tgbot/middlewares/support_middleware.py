import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import ReplyKeyboardRemove

from tgbot.models.state import SupportStateGroup


class SupportMiddleware(BaseMiddleware):

    async def on_pre_process_message(self, message: types.Message, data: dict):
        from bot import dp, bot
        state = dp.current_state(chat=message.from_user.id, user=message.from_user.id)
        state_str = str(await state.get_state())
        if state_str == 'SupportStateGroup:in_support_admin':
            if message.text == 'Завершить разговор':
                data = await state.get_data()
                user_id = data.get('user_id')
                await bot.send_message(chat_id=user_id, text='Кондитер прекратил разговор',
                                       reply_markup=ReplyKeyboardRemove())
                user_state = dp.current_state(chat=user_id, user=user_id)
                await user_state.finish()

                await message.answer('Вы прекратили разговор с пользователем',
                                     reply_markup=ReplyKeyboardRemove())
                await state.finish()
                return

            data = await state.get_data()
            user_id = data.get('user_id')
            await message.copy_to(user_id)

            raise CancelHandler()
        elif state_str == 'SupportStateGroup:in_support_user':
            if message.text == 'Завершить разговор':
                data = await state.get_data()
                admin_id = data.get('admin_id')
                await bot.send_message(chat_id=admin_id, text='Пользователь завершил разговор',
                                       reply_markup=ReplyKeyboardRemove())
                admin_state = dp.current_state(chat=admin_id, user=admin_id)
                await admin_state.finish()

                await message.answer('Вы прекратили разговор с кондитером',
                                     reply_markup=ReplyKeyboardRemove())
                await state.finish()
                return

            data = await state.get_data()
            admin_id = data.get('admin_id')
            await message.copy_to(admin_id)

            raise CancelHandler()
