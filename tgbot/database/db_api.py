from aiogram import Dispatcher

from tgbot.config import POSTGRES_URL


import asyncio
from gino import Gino

db = Gino()

class Items(db.Model):
    __tablename__ = 'portfolio'

    id = db.Column(db.Integer(), primary_key=True)
    item_name = db.Column(db.String(50))
    item_description = db.Column(db.String(100))
    item_photo = db.Column(db.String(255))


async def on_startup_database(dp: Dispatcher):
    await db.set_bind(POSTGRES_URL)
    await db.gino.create_all()


