import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware



# Создадим миддлварь, в котором полностью будет  проходить обработка сообщений
# для пользователя и операторов, которые находятся на связи.
# Отсюда сообщения в хендлеры даже направляться не будут
class SupportMiddleware(BaseMiddleware):

    async def on_pre_process_message(self, message: types.Message, data: dict):
        from bot import dp
        state = dp.current_state(chat=message.from_user.id, user=message.from_user.id)
        user_id = message.from_user.id
        state_str = str(await state.get_state())
        if state_str == 'in_support_user':
            await message.copy_to(chat_id=737006731)

            raise CancelHandler
