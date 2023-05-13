from aiogram import Bot, types


async def set_default_commands(bot: Bot):
    await bot.set_my_commands([
        types.BotCommand('start', 'Запуск бота'),
        types.BotCommand('help', 'Помощь по боту'),
        types.BotCommand('contact', 'Как можно еще связаться с кондитером')
    ])