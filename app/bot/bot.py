from aiogram import Bot, Dispatcher, executor, types

from app.config import API_BOT_TOKEN

bot = Bot(API_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Hello")

@dp.message_handler()
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("site", url='https://arzongo.uz'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.answer("Hello", reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer("hello")


executor.start_polling(dp)