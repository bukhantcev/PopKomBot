from aiogram.utils import executor
from handlers import dp
from cb_handlers import dp
from  loader import  bot
from keyboards import kb_exit



async def on_start(_):
    print('Бот запущен!')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)

