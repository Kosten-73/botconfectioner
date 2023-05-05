import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from tgbot.models.state import SupportStateGroup


class SupportMiddleware(BaseMiddleware):

    async def on_pre_process_message(self, message: types.Message, data: dict):
        from bot import dp
        state = dp.current_state(chat=message.from_user.id, user=message.from_user.id)
        state_str = str(await state.get_state())
        if state_str == 'SupportStateGroup:in_support_admin':
            data = await state.get_data()
            user_id = data.get('user_id')
            await message.copy_to(user_id)

            raise CancelHandler()
        elif state_str == 'SupportStateGroup:in_support_user':
            data = await state.get_data()
            admin_id = data.get('admin_id')
            await message.copy_to(admin_id)

            raise CancelHandler()
