from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
start_markup = ReplyKeyboardMarkup()

start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
quiz_button = KeyboardButton('/quiz')

start_markup.add(start_button, info_button, quiz_button)