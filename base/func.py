import sqlite3
from aiogram import types
from create_bot import bot


def sql_con():
    global base, cur
    base = sqlite3.connect('skill.db')
    cur = base.cursor()
    if base:
        base.execute('CREATE TABLE IF NOT EXISTS skillbox (Profession TEXT, Description TEXT, Price TEXT, Time TEXT)')
        print('Бот подлкючился к базе')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO skillbox (Profession,Description, Price, Time) VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()


async def sql_show(message):
    for ret in cur.execute('SELECT * FROM skillbox').fetchall():
        await bot.send_message(message.from_user.id,
                               'Профессия: ' + ret[1] + '\nОписание: ' + ret[2] + '\nЦена: ' + ret[3])


async def sql_delete(state):
    async with state.proxy() as data:
        cur.execute('DELETE FROM skillbox WHERE id = ?', tuple(data.values()))
        base.commit()


async def sql_search(state, message):
    async with state.proxy() as data:
        for ret in cur.execute('SELECT * FROM skillbox WHERE Profession LIKE ?', tuple(data.values())).fetchall():
            await bot.send_message(message.from_user.id, 'Профессия: ' + ret[1])


async def sql_sravn(state, message):
    async with state.proxy() as data:
        for ret in cur.execute('SELECT * FROM skillbox WHERE Price > ?', tuple(data.values())).fetchall():
            await bot.send_message(message.from_user.id, 'Профессия: ' + ret[1])
