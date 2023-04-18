from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_inline_2 = InlineKeyboardMarkup(row_width=1)
bt_edit = InlineKeyboardButton(text='Добавить фото или описание', callback_data='edit_preset')

kb_inline_2.row(bt_edit)