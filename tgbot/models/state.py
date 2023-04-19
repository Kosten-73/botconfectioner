from aiogram.dispatcher.filters.state import StatesGroup, State


class ItemStateGroup(StatesGroup):
    item_name = State()
    item_description = State()
    item_photo = State()

    item_name_edit = State()
    item_description_edit = State()
    item_photo_edit = State()

    item_await = State()

    item_edit_name_in_db = State()
    item_edit_description_db = State()
    item_edit_photo_in_db = State()