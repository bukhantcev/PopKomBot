from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

add_info = InlineKeyboardMarkup(row_width=1)
bt_info = InlineKeyboardButton(text='Добавить описание', callback_data='single_info')
bt_view = InlineKeyboardButton(text='Посмотреть', callback_data='view')

add_info.row(bt_info)
add_info.row(bt_view)