from aiogram.dispatcher.filters.state import StatesGroup, State


class ItemStateGroup(StatesGroup):
    item_name = State()
    item_description = State()
    item_photo = State()