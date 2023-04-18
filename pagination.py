async def item_index(message: types.Message):
    from bot import bot
    items = await cmd_db.select_all_item()
    item_data = items[0]
    caption = f"Вы выбрали <b>{item_data.get('item_name')}</b>" \
              f"{item_data.get('item_description')}"
    count_items = await cmd_db.count_items()
    print(count_items)
    keyboard = get_items_keyboard(count_items=count_items)  # Page: 0

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=item_data.get("item_photo"),
        caption=caption,
        parse_mode="HTML",
        reply_markup=keyboard
    )

async def fruit_page_handler(query: types.CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))
    items = await cmd_db.select_all_item()
    item_data = items[page]
    caption = f"Вы выбрали <b>{item_data.get('item_name')}</b>" \
              f"{item_data.get('item_description')}"
    count_items = await cmd_db.count_items()
    keyboard = get_items_keyboard(page=page, count_items=count_items)

    photo = InputMedia(type="photo", media=item_data.get("item_photo"), caption=caption)

    await query.message.edit_media(photo, keyboard)

def register_show_portfolio_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(item_index, commands=['test'])
    dp.register_callback_query_handler(fruit_page_handler, item_callback.filter())


item_callback = CallbackData('item', 'page')

def get_items_keyboard(page: int = 0, count_items: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    has_next_page = count_items > page + 1

    if page != 0:
        keyboard.add(
            InlineKeyboardButton(
                text="< Назад",
                callback_data=item_callback.new(page=page - 1)
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text=f"• {page + 1}",
            callback_data="dont_click_me"
        )
    )

    if has_next_page:
        keyboard.add(
            InlineKeyboardButton(
                text="Вперёд >",
                callback_data=item_callback.new(page=page + 1)
            )
        )

    return keyboard