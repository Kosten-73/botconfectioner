from aiogram import Dispatcher

from tgbot.config import POSTGRES_URL


import asyncio
from gino import Gino

db = Gino()

class Items(db.Model):
    __tablename__ = 'portfolio'

    id = db.Column(db.Integer(), primary_key=True)
    item_name = db.Column(db.String(100))
    item_description = db.Column(db.Text())
    item_photo = db.Column(db.String(255))

class OrdersUser(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.BigInteger())
    user_name = db.Column(db.String(255))
    user_phone = db.Column(db.String(50))
    user_address = db.Column(db.String(255))

    product = db.Column(db.String(100))
    filling = db.Column(db.String(100))
    value = db.Column(db.String(50))
    photo = db.Column(db.String(255))
    accept = db.Column(db.String(2), default='❌')

async def on_startup_database(dp: Dispatcher):
    await db.set_bind(POSTGRES_URL)
    # await db.gino.drop_all()
    await db.gino.create_all()


