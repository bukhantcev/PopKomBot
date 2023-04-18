from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

add_view = InlineKeyboardMarkup(row_width=1)
bt_view = InlineKeyboardButton(text='Посмотреть', callback_data='view')

add_view.row(bt_view)