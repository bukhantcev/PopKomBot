from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

kb_exit = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
bt_exit = KeyboardButton(text='Получить файлы и выйти')

kb_exit.row(bt_exit)