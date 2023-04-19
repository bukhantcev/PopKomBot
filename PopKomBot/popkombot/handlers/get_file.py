

from loader import dp, bot
from aiogram.types import ContentType, Message
from keyboards import kb_inline_1, kb_access



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def get_file(message: Message):
    with open('Access.txt', 'r', encoding='UTF-8') as f:
        access = f.readlines()
    if str(message.from_user.id) in access:
        if message.document.mime_type == 'text/xml':
            await message.answer('Ждите...')
            await message.document.download(destination_file=f'{message.from_user.id}/File.xml')
            await bot.edit_message_text(text='Файл получен', chat_id=message.chat.id, message_id=message.message_id + 1, reply_markup=kb_inline_1)
            # await message.answer('Файл получен.', reply_markup=kb_inline_1)




        else:
            await message.answer('Это не XML файл, отправь другой!')
    else:
        await message.answer('Нет доступа', reply_markup=kb_access)
