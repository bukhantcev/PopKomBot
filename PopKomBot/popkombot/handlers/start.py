from loader import dp
from aiogram.types import Message
import os
from keyboards import kb_access



@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    with open('Access.txt', 'r', encoding='UTF-8') as f:
        access = f.readlines()
    if str(message.from_user.id) in access:
        await message.answer("Пришли мне шоу файл в XML!")
        try:
            os.mkdir(f'{message.from_user.id}')
            print(f'Папка для {message.from_user.id} создана')
        except:
            print(f'Папка для {message.from_user.id} создана')
            print(f'Пользователь {message.from_user.id} допущен')
    else:
        await message.answer('Нет доступа', reply_markup=kb_access)



