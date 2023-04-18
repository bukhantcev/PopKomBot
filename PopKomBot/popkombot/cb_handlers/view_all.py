import ast

from loader import dp, bot
from aiogram.types import CallbackQuery, InputMediaPhoto, Message, InputFile
from keyboards import kb_inline_3




@dp.callback_query_handler(text='view')

async def view_all(callback: CallbackQuery):
    with open(f"./{callback.from_user.id}/List_preset.txt", "r", encoding='UTF-8') as f:
        my_dict = ast.literal_eval(str(f.read()))
        photo = my_dict.get(callback.message.text.split('\n')[0])[0]
        descr = my_dict.get(callback.message.text.split('\n')[0])[1]
    title = callback.message.text.split('\n')[0]
    descr = f'{title}\n\n{descr}'
    await bot.send_photo(photo=photo, chat_id=callback.message.chat.id, caption=descr)
    print(photo, descr)
    print(callback.message.chat.id)





