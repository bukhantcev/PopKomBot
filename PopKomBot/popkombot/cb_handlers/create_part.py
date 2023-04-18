from loader import dp, bot
from aiogram.types import CallbackQuery, InputFile
from programs import creat_part
import xml.etree.ElementTree as ET


@dp.callback_query_handler(text='create_part')
async def create_part(callback: CallbackQuery):
    cb = callback.from_user.id
    try:
        tree = ET.parse(f'./{callback.from_user.id}/File.xml')
        root = tree.getroot()
        index = 0
        for i in root.iter():
            if i.tag == '{http://schemas.malighting.de/grandma2/xml/MA}CuePart':
                index = 1
        if index == 1:
            creat_part(cb)
            await callback.answer('Готово')
            await bot.send_document(callback.message.chat.id, InputFile(f'{callback.from_user.id}/Partitura.xlsx'))
        else:
            await callback.answer('Что-то не то... Нужен шоу-файл MA2!')
    except:
        await callback.answer('Для начала отправь мне шоу-файл!')