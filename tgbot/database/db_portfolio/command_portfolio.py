from tgbot.database.db_api import Items, db


async def add_item_db(item_name: str, item_description: str, item_photo: str):
    item = Items(item_name=item_name, item_description=item_description, item_photo=item_photo)
    await item.create()


async def select_all_item():
    users = await Items.query.gino.all()
    return [user.to_dict() for user in users]


async def count_items():
    total = await db.func.count(Items.id).gino.scalar()
    return total
