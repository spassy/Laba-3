# Создание телеграм бота

## *Что делает телеграм бот?*
*Телеграм бот имеет возможность отвечать на простейшие команды пользователя такие, как `/start, /help, /show, /поиск, /фильтр`. Данные команды позваляют пользователю просматривать курсы по программированию Skillbox, искать курсы по названию курса, фильтр курсов по цене и помощь пользователю. Также в боте реализованы функции администратора. Администратор имеет возможность использовать такие команды, как `/Загрузить, /Отменить, /Удалить`. Данные команды поозваляют администратору загружать новые данные в базу данных, удалять информацию из базы данных и отменять какие либо действия, в случае если передумал загружать или удалять. Администратор проверяется по id пользователя.*

## *Как запустить проект?*
*Для запуска проекта необходимо:*
 
 * Создать папку на вашем компьютере и переместить все файлы проекта туда
 * Установить библиотки: `aiogram.utils, handlers, pars, create_bot, base` - для main.py ![alt tag](https://sun9-21.userapi.com/impg/EmhRlHmeD0SBCAevNJKsP1rmAQO87vCfKh-8Wg/uhsgWzm8hXQ.jpg?size=700x312&quality=96&sign=22eef45ea3daf3698b7f91b9f11065a3&type=album)
 * Установить библиотки: `aiogram, aiogram.dispatcher, aiogram.contrib.fsm_storage.memory` - для create_bot.py ![alt tag](https://sun9-12.userapi.com/impg/GxDqlLenTapgWwudxzqE9YloY3doF-i-nnHD9w/lTEj3HQfTFc.jpg?size=1132x194&quality=96&sign=59213242b3a158f4cf9c80eff6f65fb0&type=album)
 * Установить библиотки: `aiogram.dispatcher, aiogram.dispatcher.filters.state, aiogram, base, keyboards, aiogram.dispatcher.filters` - для admin.py ![alt tag](https://sun9-45.userapi.com/impg/E6OGwU5co2Wck0hb_Wa3c4V5MxJm0Bs9d_butQ/ndBD-DhNkd0.jpg?size=1280x449&quality=96&sign=a5868a6d688204586c53faf9cb811b1f&type=album)
 * Установить библиотки: `aiogram.types` - для admin_kb.py 
 
 ![alt tag](https://sun9-34.userapi.com/impg/9XbLS9Pf4GD84WY-nXu57AwuIxsiBcfMyboGig/o_HXaNFzPFQ.jpg?size=1280x87&quality=96&sign=9775130cce6f34cc7991bdf926862420&type=album![image](https://user-images.githubusercontent.com/96590022/147823609-682add4c-8a24-4277-a1fe-5433a42a96ed.png))
 * Установить библиотки: `sqlite3, create_bot` - для func.py 
 
 ![alt tag](https://sun9-45.userapi.com/impg/tSq98t9GANQR-3MncV4IwRXXdH4A92yai5muRQ/isgmkJYo9hc.jpg?size=470x224&quality=96&sign=a87de4c01895739452e3f42bc78e632c&type=album)
 *  Установить библиотки: `sqlite3, create_bot` - для client.py ![alt tag](https://sun1-18.userapi.com/impg/wlk-B1Q_zlxDT2I1BibI6XaJQSpxMLfOWoPJaQ/cT7_PgRn0Cg.jpg?size=1040x364&quality=96&sign=b0c105fe7d012abc7b20436ecea3fd69&type=album)
 *  Установить библиотки: `aiogram, keyboards, base, aiogram.dispatcher, aiogram.dispatcher.filters.state` - для client.py ![alt tag](https://sun1-18.userapi.com/impg/wlk-B1Q_zlxDT2I1BibI6XaJQSpxMLfOWoPJaQ/cT7_PgRn0Cg.jpg?size=1040x364&quality=96&sign=b0c105fe7d012abc7b20436ecea3fd69&type=album)
 *  Установить библиотки: `keyboards.cl` - для init.py в папке keyboards![alt tag](https://sun9-57.userapi.com/impg/t8h-zZSqCGs7hagd3KdNQUVkpNirOAWUhVG_0g/a68KRM4N_TI.jpg?size=704x88&quality=96&sign=1b8276c1dc3ccd675fb1325e8a0c6b89&type=album)
 *  Установить библиотки: `aiogram.types` - для cl.py ![alt tag](https://sun9-13.userapi.com/impg/Lw5_SyWuogrfUZmiphkvizJYtVxT82C6UIV_Og/rKF-A8dbOww.jpg?size=1280x60&quality=96&sign=395b354f8227e66c78f7d9679d5a7ce3&type=album)
 * Открыть файл `main.py` 
 * Запустить файл `main.py`
