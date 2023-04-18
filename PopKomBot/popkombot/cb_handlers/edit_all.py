from loader import dp, bot
from aiogram.types import CallbackQuery
from keyboards import kb_inline_3




@dp.callback_query_handler(text='edit')
async def edit_all(callback: CallbackQuery):
    print(callback.message.text.split("\n")[0])
    await bot.edit_message_text(text= callback.message.text.split('\n')[0],
                                chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=kb_inline_3)







