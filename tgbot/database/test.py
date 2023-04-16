import asyncio

import tgbot.config
from tgbot.database.db_api import db
from tgbot.database.db_portfolio import command_portfolio

async def test():
    await db.set_bind(tgbot.config.POSTGRES_URL)
    await db.gino.drop_all()
    await db.gino.create_all()

    await command_portfolio.add_item('One', 'Test', 'photo')


asyncio.get_event_loop().run_until_complete(test())
