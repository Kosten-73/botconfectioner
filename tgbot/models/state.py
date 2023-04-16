from aiogram.dispatcher.filters.state import StatesGroup, State


class ItemStateGroup(StatesGroup):
    item_name = State()
    item_description = State()
    item_photo = State()

    item_name_edit = State()
    item_description_edit = State()
    item_photo_edit = State()

    item_await = State()