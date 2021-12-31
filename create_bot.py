from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5064692777:AAHOnnEfXR7NOeanheYcxOG6e8_f0kYA4pk')
dp = Dispatcher(bot, storage=storage)