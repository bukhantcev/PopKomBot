from loader import dp, bot
from aiogram.types import CallbackQuery
import openpyxl
from programs import get_list_preset
from keyboards import kb_inline_3
from keyboards import kb_exit

@dp.callback_query_handler(text='edit_preset')
async def list_preset(callback: CallbackQuery):
     cb = callback.from_user.id
     try:

        book = openpyxl.load_workbook(f'./{callback.from_user.id}/Preset.xlsx', keep_vba=True)
        sheet = book.active
        for index in range(2, sheet.max_row + 1):
            await bot.send_message(callback.message.chat.id, text=get_list_preset(index, cb), reply_markup=kb_inline_3)
        await bot.send_message(callback.message.chat.id, text='Чтобы добавить фото нужно отправить фото мне и нажать на кнопку "Добавить фото" на нужном пресете.'
                                                                  ' Чтобы добавить описание, отправь мне его в сообщении и нажми на кнопку '
                                                                  '"Добавить описание" на нужном пресете. Чтобы получить файл и выйти, жми кнопку ниже! '
                                                              'Описание к фото тоже считается)', reply_markup=kb_exit)
     except:

         await callback.answer("Необходимо сделать пресеты!")