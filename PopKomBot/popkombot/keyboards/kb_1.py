from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

kb_1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


bt = KeyboardButton(text='Получить')
kb_1.row(bt)