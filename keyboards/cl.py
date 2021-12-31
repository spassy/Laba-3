from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Start')
b2 = KeyboardButton('/Help')
b3 = KeyboardButton('/Show')
b4 = KeyboardButton('/Поиск')
b5 = KeyboardButton('/Фильтр')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.insert(b1).insert(b2).insert(b3).insert(b4).insert(b5)
