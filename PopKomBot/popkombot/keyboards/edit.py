from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

edit = InlineKeyboardMarkup(row_width=1)
bt_edit = InlineKeyboardButton(text='Изменить', callback_data='edit')
bt_view = InlineKeyboardButton(text='Посмотреть', callback_data='view')

edit.row(bt_edit)
edit.row(bt_view)