from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_inline_1 = InlineKeyboardMarkup(row_width=2)
bt_part = InlineKeyboardButton(text='Сделать партитуру', callback_data='create_part')
bt_preset = InlineKeyboardButton(text='Сделать пресеты', callback_data='create_preset')
kb_inline_1.row(bt_part, bt_preset)