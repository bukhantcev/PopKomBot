from aiogram import types

from loader import dp
from aiogram.types import Message, InputFile
import os
from programs import test_file




@dp.message_handler(text= 'Получить файлы и выйти')
async def find_exit(message: Message):
    ms = message.from_user.id
    if f'{message.from_user.id}\\Preset.xlsx' in test_file(ms):
        await message.answer_document(InputFile(f'{message.from_user.id}/Preset.xlsx'))
    if f'{message.from_user.id}\\Partitura.xlsx' in test_file(ms):
        await message.answer_document(InputFile(f'{message.from_user.id}/Partitura.xlsx'))
    await message.answer("Ну всё, пока!))", reply_markup=types.ReplyKeyboardRemove())


    try:
        os.remove(f'./{message.from_user.id}/Preset.xlsx')
    except:
        print('Файла Preset.xlsx не сушествует')
    try:
        os.remove(f'./{message.from_user.id}/Partitura.xlsx')
    except:
        print('Файла Partitura.xlsx не сушествует')
    try:
        os.remove(f'./{message.from_user.id}/Photo.jpg')
    except:
        print('Файла Photo.jpg не сушествует')
    try:
        os.remove(f'./{message.from_user.id}/Description.txt')
    except:
        print('Файла Description.txt не сушествует')
    try:
        os.remove(f'./{message.from_user.id}/File.xml')
    except:
        print('Файла File.xml не сушествует')
    try:
        os.remove(f'./{message.from_user.id}/List_preset.txt')
    except:
        print('Файла List_preset не сушествует')
    try:
        os.remove(f'./{message.from_user.id}/Photo_id.txt')
    except:
        print('Файла Photo_id.txt не сушествует')
    try:
        os.rmdir(f'{message.from_user.id}')
    except:
        print('Папки не существует')
    new_user = message.from_user.id
    with open('Access.txt', 'r', encoding='UTF-8') as file:
        file = file.readlines()
        file.remove(str(new_user))
        for i in file:
            if i == '\n':
                file.remove(i)
        with open('Access.txt', 'w', encoding='UTF-8') as fw:
            fw.write(''.join(map(str, file)))
    print('End')
