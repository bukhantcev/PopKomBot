from loader import dp
from aiogram.types import Message
import os



@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.answer("Пришли мне шоу файл в XML!")
    try:
        os.mkdir(f'{message.from_user.id}')
    except:
        print('Папка уже создана')

