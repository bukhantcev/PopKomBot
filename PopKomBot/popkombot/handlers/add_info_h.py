from loader import dp
from aiogram.types import Message


@dp.message_handler()
async def add_info(message: Message):
    my_file = open(f"./{message.from_user.id}/Description.txt", "w+", encoding='UTF-8')
    my_file.write(message.text)
    my_file.close()

    await message.answer(text='Нажми на кнопку "Добавить описание" для нужного пресета и твой текст улетит куда нужно!')