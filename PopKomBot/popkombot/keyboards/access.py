from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_access = InlineKeyboardMarkup(row_width=2)
bt_get_access = InlineKeyboardButton(text='Запросить доступ', callback_data='get_access')
bt_contact = InlineKeyboardButton(text='Связаться с разработчиком', callback_data='get_contact')
kb_access.row(bt_get_access, bt_contact)