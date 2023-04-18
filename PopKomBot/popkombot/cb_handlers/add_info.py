from loader import dp, bot
from aiogram.types import CallbackQuery
from keyboards import add_photo, edit
from programs import add_info_preset_list
import ast
import os


@dp.callback_query_handler(text='single_info')
async def add_info(callback: CallbackQuery):
    cb = callback.from_user.id
    try:
        with open(f"./{callback.from_user.id}/Description.txt", "r", encoding='UTF-8') as f:
            add_info_preset_list(callback.message.text.split('\n')[0], str(f.read()), cb)

        await bot.edit_message_text(text=f'{callback.message.text}\nОписание добавлено',
                                    chat_id= callback.message.chat.id, message_id= callback.message.message_id,
                                    reply_markup= add_photo if len(callback.message.reply_markup.inline_keyboard[0]) == 2 else edit)

        try:

            my_file = open(f'./{callback.from_user.id}/List_preset.txt', 'r', encoding='UTF-8')
            dict_preset = ast.literal_eval(str(my_file.read()))
            with open(f'./{callback.from_user.id}/Description.txt', 'r', encoding='UTF-8') as d:
                descr = dict_preset.get(callback.message.text.split('\n')[0], ['', ''])
                descr[1] = str(d.read())
            my_file.close()
            my_file = open(f"./{callback.from_user.id}/List_preset.txt", "w", encoding='UTF-8')
            dict_preset[callback.message.text.split('\n')[0]] = descr
            my_file.write(str(dict_preset))
            my_file.close()
        except:
            dict_preset = {}
            with open(f'./{callback.from_user.id}/Description.txt', 'r', encoding='UTF-8') as d:
                descr = ['', '']
                descr[1] = str(d.read())
            my_file = open(f"./{callback.from_user.id}/List_preset.txt", "w+", encoding='UTF-8')
            dict_preset[callback.message.text.split('\n')[0]] = descr
            my_file.write(str(dict_preset))
            my_file.close()
        print(callback.message)
        os.remove(f"./{callback.from_user.id}/Description.txt")
    except:
        await callback.answer('Необходимо создать описание!')






@dp.callback_query_handler(text='add_info')
async def add_info(callback: CallbackQuery):
    cb = callback.from_user.id
    try:
        with open(f"./{callback.from_user.id}/Description.txt", "r", encoding='UTF-8') as f:
            add_info_preset_list(callback.message.text.split('\n')[0], str(f.read()), cb)

        await bot.edit_message_text(text=f'{callback.message.text}\nОписание добавлено',
                                    chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                    reply_markup=add_photo if len(
                                        callback.message.reply_markup.inline_keyboard[0]) == 2 else edit)

        try:

            my_file = open(f'./{callback.from_user.id}/List_preset.txt', 'r', encoding='UTF-8')
            dict_preset = ast.literal_eval(str(my_file.read()))
            with open(f'./{callback.from_user.id}/Description.txt', 'r', encoding='UTF-8') as d:
                descr = dict_preset.get(callback.message.text.split('\n')[0], ['', ''])
                descr[1] = str(d.read())
            my_file.close()
            my_file = open(f"./{callback.from_user.id}/List_preset.txt", "w", encoding='UTF-8')
            dict_preset[callback.message.text.split('\n')[0]] = descr
            my_file.write(str(dict_preset))
            my_file.close()
        except:
            dict_preset = {}
            with open(f'./{callback.from_user.id}/Description.txt', 'r', encoding='UTF-8') as d:
                descr = ['', '']
                descr[1] = str(d.read())
            my_file = open(f"./{callback.from_user.id}/List_preset.txt", "w+", encoding='UTF-8')
            dict_preset[callback.message.text.split('\n')[0]] = descr
            my_file.write(str(dict_preset))
            my_file.close()
        print(callback.message)
        os.remove(f"./{callback.from_user.id}/Description.txt")
    except:
        await callback.answer('Необходимо создать описание!')







