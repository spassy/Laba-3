from aiogram import types, Dispatcher
from create_bot import dp
from keyboards import kb_client
from base import func
from create_bot import bot

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class profes(StatesGroup):
    prof = State()


class price(StatesGroup):
    pr = State()


"""Поиск по профессии"""


async def search_prof(message: types.Message):
    await profes.prof.set()
    await message.reply('По какому слову искать?')


"""Фильр по цене"""


async def search_srav(message: types.Message):
    await price.pr.set()
    await message.reply('Ниже какой цены ищете?')


"""Ответ поиска по профессии"""


async def srh_prof(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['prof'] = message.text
    await func.sql_search(state, message)
    await state.finish()


"""Ответ фильра по цене"""


async def show_curs_srav(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pr'] = message.text
    await func.sql_sravn(state, message)
    await state.finish()


"""Старт бота"""


async def command_start(message: types.Message):
    try:
        await message.answer('Что хочешь?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение ЛС')


"""Помощь бота"""


async def command_help(message: types.Message):
    await message.answer(
        'Если хочешь увидеть все курсы, нажми ''/show''\nЕсли хочешь найти курс по слову, нажми ''/Поиск'' (При вводе '
        'слова испольуй %. Например: %IOS%)')


"""Показать все курсы"""


async def show_curs(message: types.Message):
    await func.sql_show(message)


"""Все команды клиента"""


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(search_prof, commands=['Поиск'], State=None)
    dp.register_message_handler(search_srav, commands=['Фильтр'], State=None)
    dp.register_message_handler(command_start, commands=['Start'])
    dp.register_message_handler(command_help, commands=['Help'])
    dp.register_message_handler(show_curs, commands=['Show'])
    dp.register_message_handler(srh_prof, state=profes.prof)
    dp.register_message_handler(show_curs_srav, state=price.pr)
