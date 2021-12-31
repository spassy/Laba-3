from aiogram.utils import executor
from handlers import client, admin
from pars import code
from create_bot import dp
from base import func


# Говорит о выходе бота в онлайн
async def on_startup(_):
    print('Бот вышел в онлайн')
    func.sql_con()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
code.register_handlers_pars(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
