from loader import dp, bot
from aiogram.types import CallbackQuery, Message, InputFile
from programs import create_presets
import xml.etree.ElementTree as ET
from keyboards import kb_inline_2


@dp.callback_query_handler(text='create_preset')
async def create_preset(callback: CallbackQuery):
    cb = callback.from_user.id

    try:
        tree = ET.parse(f'./{callback.from_user.id}/File.xml')
        root = tree.getroot()
        index = 0
        for i in root.iter():
            if i.tag == '{http://schemas.malighting.de/grandma2/xml/MA}Preset':
                index = 1
        if index == 1:
            create_presets(cb)

            await callback.answer('Готово')
            await bot.send_document(callback.message.chat.id, InputFile(f'{callback.from_user.id}/Preset.xlsx'), reply_markup=kb_inline_2)
        else:
            await callback.answer('Что-то не то... Нужен шоу-файл MA2!')
    except:
        await callback.answer("Для начала отправь мне шоу-файл!")