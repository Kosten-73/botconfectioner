from aiogram import Bot, types


async def set_default_commands(bot: Bot):
    await bot.set_my_commands([
        types.BotCommand('help', 'Помощь по боту'),
        types.BotCommand('show_portfolio', 'Показать мои работы'),
        types.BotCommand('make_order', 'Сделать заказ')
    ])