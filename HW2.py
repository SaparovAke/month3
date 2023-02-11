from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from decouple import config

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)