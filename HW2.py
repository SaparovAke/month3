from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

@db.message_handler(commands=['hello', 'salam'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name}')
    await message.reply('пока что всё')

@db.message_handler(commands='quiz')
async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    ques = 'Кто ты воин?'
    answer = [
        'Бетмэн - Темный рыцарь',
        'Спанч Боб - Квадратные штаны',
        'Томас Шелби - глава Острых козырьков',
        'Ахилес - сын Пелея',
        'Диктор канала "Мастерская настроения"',
        'Оптимус Прайм - Последний Прайм',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        explanation='Ты Ахилес - Сын Пелея',
        open_period=10,
        reply_markup=markup
    )

@db.callback_query_handler(text='button')
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    ques = 'Откуда мем?'
    answer = [
        'Бетмэн',
        'Спанч Боб Квадратные штаны',
        'Человек-паук',
        'Халк',
        'Бесстыжие',
        'Неуязвимый',
    ]
    photo = open('media/bat.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='This is Batman, because I am Batman',
        open_period=10,
        reply_markup=markup
    )

@db.callback_query_handler(text='button')
async def quiz3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    ques = 'Откуда мем?'
    answer = [
        'Корпорация монстров',
        'Спанч Боб Квадратные штаны',
        'Человек-паук',
        'Халк',
        'Бесстыжие',
        'Неуязвимый',
    ]
    photo = open('media/spidermem.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation='Это человек паук',
        open_period=10,
        reply_markup=markup
    )
@db.callback_query_handler(text='button')
async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    ques = 'Откуда мем?'
    answer = [
        'Неуязвимый',
        'Спанч Боб Квадратные штаны',
        'Человек-паук',
        'Халк',
        'Бесстыжие',
        'Корпорация монстров'
    ]
    photo = open('media/корпорация монстров.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=-1,
        explanation='Это Корпорация монстров',
        open_period=10,
        reply_markup=markup
    )

@db.callback_query_handler(text='button')
async def quiz5(call: types.CallbackQuery):
    ques = 'Откуда мем?'
    answer = [
        'Великий Гетсби',
        'Спанч Боб Квадратные штаны',
        'Халк',
        'Бесстыжие',
        'Освобождённый Джанго'
        'Титаник',
    ]
    photo = open('media/освобожденный джанго.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=-2,
        explanation='Это освобождённый джанго',
        open_period=10
    )

@db.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)