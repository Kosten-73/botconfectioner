from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from tgbot.config import load_config


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.from_user.id in load_config().tg_bot.admin_ids:
            return True
        else:
            await message.answer('У вас нет доступа к этой команде')
            return False
