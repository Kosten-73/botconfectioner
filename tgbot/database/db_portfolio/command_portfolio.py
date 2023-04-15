from tgbot.database.db_api import Items


async def add_item_db(item_name: str, item_description: str, item_photo: str):
    item = Items(item_name=item_name, item_description=item_description, item_photo=item_photo)
    await item.create()