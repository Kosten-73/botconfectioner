from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from tgbot.config import support_id
from tgbot.keyboards.admin.inlinekeyboard.order_ikb import get_link_to_user_keyboard
from tgbot.keyboards.user.inlinekeyboard.main_menu_ikb import main_menu_ikb
from tgbot.keyboards.user.inlinekeyboard.order_ikb.order_main_ikb import choice_category_ikb, accept_order_ikb
from tgbot.keyboards.user.keyboard.order_kb import get_contact_kb
from tgbot.models.state import OrderStateGroup
from tgbot.database.db_order import command_order as cmd_db

async def stop_order(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback.answer('Вы отменили создание заказа')
    await callback.message.delete()
    await callback.message.answer('Главное меню бота', reply_markup=main_menu_ikb)


async def stop_order_kb(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer('Вы отменили создание заказа')
    await message.answer('Главное меню бота', reply_markup=main_menu_ikb)


async def start_make_order(callback: types.CallbackQuery):
    await callback.message.edit_text('Что вы хотите заказать?',
                                     reply_markup=choice_category_ikb)
    await OrderStateGroup.category.set()


async def get_phone_user(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.answer('Нажмите на кнопку чтобы прислать номер телефона',
                                  reply_markup=get_contact_kb)

    await OrderStateGroup.contact_user.set()

async def enter_phone_user(message: types.Message, state: FSMContext):
    await message.delete()
    user_phone = message.contact.phone_number
    user_id = message.from_user.id
    user_name = message.from_user.username
    async with state.proxy() as data:
        data['user_phone'] = user_phone
        data['user_id'] = user_id
        data['user_name'] = user_name
    await message.answer('Теперь напишите ваш адрес', reply_markup=ReplyKeyboardRemove())
    await OrderStateGroup.address_user.set()


async def send_address(message: types.Message, state: FSMContext):
    await message.delete()
    address = message.text
    async with state.proxy() as data:
        data['user_address'] = address

    await message.answer(f"Ваш id:{data['user_id']}\n"
                         f"Ваш никнейм:{data['user_name']}\n"
                         f"Адрес доставки:{data['user_address']}\n"
                         f"Ваш номер телефона:{data['user_phone']}\n"
                         f"Ваш заказ:")
    await message.answer_photo(photo=data['photo'],
                               caption=f"Категория: {data['category']}\n"
                                       f"Подкатегория: {data['subcategory']}\n"
                                       f"Начинка: {data['filling']}\n"
                                       f"Размер: {data['value']}\n")
    await message.answer('Выберете действие', reply_markup=accept_order_ikb)
    await OrderStateGroup.await_create.set()


async def create_order(callback: types.CallbackQuery, state: FSMContext):
    from bot import bot
    async with state.proxy() as data:
        user_id = data['user_id']
        user_name = data['user_name']
        user_phone = data['user_phone']
        user_address = data['user_address']
        category = data['category']
        subcategory = data['subcategory']
        filling = data['filling']
        value = data['value']
        photo = data['photo']
    await cmd_db.add_order_db(user_id=user_id, user_name=user_name, user_phone=user_phone,
                              user_address=user_address, category=category, subcategory=subcategory, filling=filling, value=value,
                              photo=photo)
    await callback.answer('Ваш заказа успешно создан и отправлен кондитеру, с вами свяжутся здесь', show_alert=True)
    await callback.message.delete()
    await callback.message.answer('Главное меню бота', reply_markup=main_menu_ikb)
    await state.finish()

    await bot.send_photo(chat_id=support_id, photo=data['photo'],
                         caption=f"Вам поступил новый заказ!"
                         f"Никнейм заказчика:{data['user_name']}\n"
                         f"Адрес доставки:{data['user_address']}\n"
                         f"Номер телефона:{data['user_phone']}\n"
                         f"Что заказали: {data['category']}\n"
                         f"{data['subcategory']}\n"
                         f"Начинка:{data['filling']}\n"
                         f"Количество:{data['value']}",
                         reply_markup=get_link_to_user_keyboard(user_id=user_id))


def register_main_make_order_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_make_order, text='make_order')
    dp.register_callback_query_handler(stop_order, text='stop_order', state='*')
    dp.register_message_handler(stop_order_kb, text='Отмена', state='*')

    dp.register_callback_query_handler(get_phone_user, text='continue', state=OrderStateGroup.await_accept)
    dp.register_message_handler(enter_phone_user, state=OrderStateGroup.contact_user,
                                content_types=types.ContentTypes.CONTACT)

    dp.register_message_handler(send_address, state=OrderStateGroup.address_user)
    dp.register_callback_query_handler(create_order, state=OrderStateGroup.await_create, text='accept')