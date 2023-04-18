from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

add_photo = InlineKeyboardMarkup(row_width=1)
bt_photo = InlineKeyboardButton(text='Добавить фото', callback_data='single_photo')
bt_view = InlineKeyboardButton(text='Посмотреть', callback_data='view')

add_photo.row(bt_photo)
add_photo.row(bt_view)