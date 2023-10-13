from aiogram import Bot, Dispatcher, executor, types

from app.config import API_BOT_TOKEN

bot = Bot(API_BOT_TOKEN)
#bot = Bot("6673848683:AAHBkgTNi27SKTtcqjxN1NeEim2TfZTlXd4")
dp = Dispatcher(bot)

users = {}

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Hello")
    if message.from_user.id not in users:
        users[message.from_user.id] = {'step': 1}
    else:
        # Если пользователь уже существует, увеличиваем значение step
        users[message.from_user.id]['step'] = 1

@dp.message_handler()
async def brains(message: types.Message):
    if users[message.from_user.id]['step'] == 1:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("site", url='https://arzongo.uz'))
        markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
        await message.answer("Hello", reply_markup=markup)
        users[message.from_user.id]['step'] += 1
        return

    if users[message.from_user.id]['step'] == 2:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(types.KeyboardButton("Site"))
        await message.answer("Hello", reply_markup=markup)
        users[message.from_user.id]['step'] += 1
        return

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer("hello")


executor.start_polling(dp)