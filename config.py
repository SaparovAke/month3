from aiogram import Dispatcher, Bot
from decouple import config

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)