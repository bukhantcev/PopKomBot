from loader import dp
from aiogram.types import ContentType, Message





@dp.message_handler(content_types=ContentType.PHOTO)
async def get_foto(message: Message):
        await message.photo[-1].download(destination_file=f'./{message.from_user.id}/Photo.jpg')
        await message.answer('Фото получено.')

        my_photo = open(f"./{message.from_user.id}/Photo_id.txt", "w+", encoding='UTF-8')
        my_photo.write(message.photo[-1].file_id)
        my_photo.close()



        await message.answer('Выбери пресет и нажми "Добавить фото" и "Добавить описание" если есть.')

        try:
            my_file = open(f"./{message.from_user.id}/Description.txt", "w+", encoding='UTF-8')
            my_file.write(message.caption)
            my_file.close()
        except:
            await message.answer('Отправь мне описание')

