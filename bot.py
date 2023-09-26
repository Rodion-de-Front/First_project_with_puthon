import telebot
from telebot import types
from fastapi import FastAPI

# токен бота
API_TOKEN = '6673848683:AAHBkgTNi27SKTtcqjxN1NeEim2TfZTlXd4'

# cоздаем экземпляр бота
bot = telebot.TeleBot(API_TOKEN)

# словарь с шагами пользователей
bot_states = {}

# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот-эхо. Отправь мне любое сообщение, и я повторю его.")
    bot_states[message.chat.id] = 2

# Обработчик для всех остальных сообщений
@bot.message_handler()
def bot_brains(message):

    if bot_states[message.chat.id] == 2:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Go to site", url='https://google.com'))
        btn2 = types.InlineKeyboardButton('Удалить d', callback_data='delete')
        btn3 = types.InlineKeyboardButton ('Измениь J', callback_data='edit')
        markup.row(btn2, btn3)
        bot.send_message(message.chat.id, "Gthtqnb", reply_markup=markup)

# Обработчик для инлайн кнопок
@bot.callback_query_handler(func=lambda callback: True)
def click_on_button(callback):
    if callback.data == "delete":
        bot.send_message(callback.message.chat.id, "Suck")

# Запуск непрерывной работы бота
bot.polling(none_stop=True)


app = FastAPI()


@app.get("/get")
async def get_request():
    return {"message": "Hello World"}

@app.get("/get2")
async def post_reguest():
    return {"success": "true"}
