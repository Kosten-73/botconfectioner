from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

support_callback = CallbackData('accept', 'admin_id', 'action')


def get_keyboard_accept_sup_user_ikb(admin_id: int = None):
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(InlineKeyboardButton(
        text='Принять',
        callback_data=support_callback.new(admin_id=admin_id,
                                           action='accept')
    ))

    keyboard.add(InlineKeyboardButton(
        text='Отменить',
        callback_data=support_callback.new(admin_id=admin_id,
                                           action='cancel')
    ))

    return keyboard


def get_cancel_wait_sup_keyboard(admin_id: int = None):
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(InlineKeyboardButton(
        text='Отменить',
        callback_data=support_callback.new(admin_id=admin_id,
                                           action='stop_wait_user')
    ))
    return keyboard