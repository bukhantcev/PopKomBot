from loader import dp, bot
from aiogram.types import CallbackQuery
from keyboards import kb_addaccess


@dp.callback_query_handler(text='get_access')
async def get_access(callback: CallbackQuery):
     await bot.send_message(chat_id=404354012, text=f'Запрос от:\n{callback.from_user.full_name}\n{callback.from_user.username}\n{callback.from_user.id}', reply_markup=kb_addaccess)

@dp.callback_query_handler(text='add_access')
async def get_access_yes(callback: CallbackQuery):
     new_user = callback.message.text.split('\n')[-1]
     with open('Access.txt', 'r', encoding='UTF-8') as file:
          file = file.readlines()
          file.append(f'\n{new_user}')
          with open('Access.txt', 'w', encoding='UTF-8') as fw:
               fw.write(''.join(map(str, file)))
     await bot.send_message(chat_id=new_user, text='Доступ открыт, добро пожаловать! нажми на  /start')

@dp.callback_query_handler(text='get_contact')
async def get_access_no(callback: CallbackQuery):

     await bot.send_message(chat_id=callback.from_user.id, text='Александр Буханцев\n+79265730771')