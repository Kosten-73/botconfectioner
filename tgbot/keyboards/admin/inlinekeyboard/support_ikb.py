from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cancel_sup_admin_ikb = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [InlineKeyboardButton('Отменить',
                                                          callback_data='stop_wait')]
                                ])

support_call_id_callback = CallbackData('support', 'user_id', 'action')


def get_accept_to_sup_call_ikb(user_id: int = None) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(
        text='Принять',
        callback_data=support_call_id_callback.new(user_id=user_id,
                                                   action='accept')
    ))

    keyboard.add(InlineKeyboardButton(
        text='Отклонить',
        callback_data=support_call_id_callback.new(user_id=user_id,
                                                   action='cancel')
    ))
    return keyboard