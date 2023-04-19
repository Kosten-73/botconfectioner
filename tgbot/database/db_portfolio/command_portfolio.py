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


async def delete_item(item_name):
    item = await Items.query.where(Items.item_name == item_name).gino.first()
    print(item)
    await item.delete()


async def update_name_item(item_name, new_item_name):
    item = await Items.query.where(Items.item_name == item_name).gino.first()
    await item.update(item_name=new_item_name).apply()


async def update_description_item(item_name, new_item_description):
    item = await Items.query.where(Items.item_name == item_name).gino.first()
    await item.update(item_description=new_item_description).apply()


async def update_photo_item(item_name, new_item_photo):
    item = await Items.query.where(Items.item_name == item_name).gino.first()
    await item.update(item_photo=new_item_photo).apply()