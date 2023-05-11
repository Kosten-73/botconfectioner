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


class OrderStateGroup(StatesGroup):
    category = State()
    subcategory = State()

    filling = State()
    value = State()

    photo = State()

    await_accept = State()
    contact_user = State()
    address_user = State()
    await_create = State()

class SupportStateGroup(StatesGroup):
    wait_accept_to_user = State()
    in_support_user = State()
    in_support_admin = State()