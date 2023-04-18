from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_inline_3 = InlineKeyboardMarkup(row_width=2)
bt_add_photo = InlineKeyboardButton(text='Добавить фото', callback_data='add_photo')
bt_add_info = InlineKeyboardButton(text='Добавить описание', callback_data='add_info')

kb_inline_3.row(bt_add_photo, bt_add_info)