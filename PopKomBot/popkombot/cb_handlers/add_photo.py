import ast

from loader import dp, bot
from aiogram.types import CallbackQuery, Message
from keyboards import add_info, edit, add_view
from programs import add_photo_preset_list
import os



@dp.callback_query_handler(text='single_photo')
async def add_photo(callback: CallbackQuery):
    cb = callback.from_user.id
    try:
        add_photo_preset_list(callback.message.text.split('\n')[0], cb)
        await bot.edit_message_text(text=f'{callback.message.text}\nфото добавлено',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                    reply_markup=add_info if len(
                                        callback.message.reply_markup.inline_keyboard[0]) == 2 else edit)





        try:

            my_file = open(f'./{callback.from_user.id}/List_preset.txt', 'r', encoding='UTF-8')
            dict_preset = ast.literal_eval(str(my_file.read()))
            with open('./files/Photo_id.txt', 'r', encoding='UTF-8') as d:
                descr = dict_preset.get(callback.message.text.split('\n')[0], ['', ''])
                descr[0] = str(d.read())
            my_file.close()
            my_file = open(f"./{callback.from_user.id}/List_preset.txt", "w", encoding='UTF-8')
            dict_preset[callback.message.text.split('\n')[0]] = descr
            my_file.write(str(dict_preset))
            my_file.close()
        except:
            dict_preset = {}

            descr = ['', '']
            with open(f'./{callback.from_user.id}/Photo_id.txt', 'r', encoding='UTF-8') as d:
                descr[0] = str(d.read())
            my_file = open(f"./{callback.from_user.id}/List_preset.txt", "w+", encoding='UTF-8')
            dict_preset[callback.message.text.split('\n')[0]] = descr
            my_file.write(str(dict_preset))
            my_file.close()
        print(descr)
        os.remove(f"./{callback.from_user.id}/Photo.jpg")
        os.remove(f"./{callback.from_user.id}/Photo_id.txt")
    except:
        await callback.answer(text="Сначала нужно отправить фото!")

@dp.callback_query_handler(text='add_photo')
async def add_photo(callback: CallbackQuery):
    cb = callback.from_user.id
    try:
        add_photo_preset_list(callback.message.text.split('\n')[0], cb)
        await bot.edit_message_text(text=f'{callback.message.text}\nфото добавлено',
                                    chat_id= callback.message.chat.id, message_id= callback.message.message_id,
                                    reply_markup= add_info if len(callback.message.reply_markup.inline_keyboard[0]) == 2 else edit)





        try:

            my_file = open(f'./{callback.from_user.id}/List_preset.txt', 'r', encoding='UTF-8')
            dict_preset = ast.literal_eval(str(my_file.read()))
            with open(f'./{callback.from_user.id}/Photo_id.txt', 'r', encoding='UTF-8') as d:
                descr = dict_preset.get(callback.message.text.split('\n')[0], ['', ''])
                descr[0] = str(d.read())
            my_file.close()
            my_file = open(f"./{callback.from_user.id}/List_preset.txt", "w", encoding='UTF-8')
            dict_preset[callback.message.text.split('\n')[0]] = descr
            my_file.write(str(dict_preset))
            my_file.close()
        except:
            dict_preset = {}

            descr = ['', '']
            with open(f'./{callback.from_user.id}/Photo_id.txt', 'r', encoding='UTF-8') as d:
                descr[0] = str(d.read())
            my_file = open(f"./{callback.from_user.id}/List_preset.txt", "w+", encoding='UTF-8')
            dict_preset[callback.message.text.split('\n')[0]] = descr
            my_file.write(str(dict_preset))
            my_file.close()
        print(descr)
        os.remove(f"./{callback.from_user.id}/Photo.jpg")
        os.remove(f"./{callback.from_user.id}/Photo_id.txt")
    except:
        await callback.answer(text="Сначала нужно отправить фото!")
