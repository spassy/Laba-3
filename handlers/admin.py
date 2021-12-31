from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from base import func
from keyboards import admin_kb
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text

ID_mod = 455096604


class id_base(StatesGroup):
    id = State()


class FSMAdmin(StatesGroup):
    prof = State()
    descrip = State()
    price = State()
    time = State()


"""Удаление строки из бд"""


async def delete(message: types.Message):
    if message.from_user.id == ID_mod:
        await id_base.id.set()
        await message.reply('Введи номер строки')
        await message.delete()
    elif message.from_user.id != ID_mod:
        await message.reply('У вас нет прав администратора!')


"""Новая строка в бд"""


async def upload(message: types.Message):
    if message.from_user.id == ID_mod:
        await FSMAdmin.prof.set()
        await message.reply('Введи название курса', reply_markup=admin_kb.button_case_admin)
    elif message.from_user.id != ID_mod:
        await message.reply('У вас нет прав администратора!')


"""Отмена команд"""


async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID_mod:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')
    elif message.from_user.id != ID_mod:
        await message.reply('У вас нет прав администратора!')


"""Ответы пользователя при загрузке"""


async def delete_com(message: types.Message, state: FSMContext):
    if message.from_user.id == ID_mod:
        async with state.proxy() as data:
            data['id'] = message.text
        await func.sql_delete(state)
        await state.finish()
        await message.reply('Строка удалена')
    elif message.from_user.id != ID_mod:
        await message.reply('У вас нет прав администратора!')


async def load_prof(message: types.Message, state: FSMContext):
    if message.from_user.id == ID_mod:
        async with state.proxy() as data:
            data['prof'] = message.text
            await message.reply('Введи описание к курсу')
            await FSMAdmin.next()
    elif message.from_user.id != ID_mod:
        await message.reply('У вас нет прав администратора!')


async def load_descrip(message: types.Message, state: FSMContext):
    if message.from_user.id == ID_mod:
        async with state.proxy() as data:
            data['descrip'] = message.text
            await message.reply('Введи цену курса')
            await FSMAdmin.next()
    elif message.from_user.id != ID_mod:
        await message.reply('У вас нет прав администратора!')


async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID_mod:
        async with state.proxy() as data:
            data['price'] = message.text
            await message.reply('Введи время курса')
            await FSMAdmin.next()
    elif message.from_user.id != ID_mod:
        await message.reply('У вас нет прав администратора!')


async def load_time(message: types.Message, state: FSMContext):
    if message.from_user.id == ID_mod:
        async with state.proxy() as data:
            data['time'] = message.text

        await func.sql_add_command(state)
        await state.finish()
    elif message.from_user.id != ID_mod:
        await message.reply('У вас нет прав администратора!')


"""Все команды админа"""


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete, commands='Удалить', State=None)
    dp.register_message_handler(upload, commands='Загрузить', State=None)
    dp.register_message_handler(cancel_handler, state='*', commands='Отменить')
    dp.register_message_handler(cancel_handler, Text(equals='Отменить', ignore_case=True), state='*')
    dp.register_message_handler(delete_com, state=id_base.id)
    dp.register_message_handler(load_prof, state=FSMAdmin.prof)
    dp.register_message_handler(load_descrip, state=FSMAdmin.descrip)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(load_time, state=FSMAdmin.time)
