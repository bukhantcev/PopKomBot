from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_addaccess = InlineKeyboardMarkup(row_width=2)
bt_add_access = InlineKeyboardButton(text='Открыть доступ', callback_data='add_access')
bt_not_access = InlineKeyboardButton(text='Отклонить', callback_data='not_access')
kb_addaccess.row(bt_add_access, bt_not_access)