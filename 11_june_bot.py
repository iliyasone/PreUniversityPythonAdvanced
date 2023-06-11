from env import TOKEN
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import logging
from keyboards import *


# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def first_process(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать в анонимный чат бот! Введите свой возраст")
    await state.set_state("age")

@dp.message_handler(state='age')
async def age_process(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        await state.update_data(age = int(text))
    else:
        message.reply("Вы ввели не число. Повторите попытку")
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)