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


@dp.message_handler(commands=['start'], state='*')
async def first_process(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать в анонимный чат бот! Введите свой возраст")
    await state.set_state("age")

@dp.message_handler(state='age')
async def age_process(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        await state.update_data({'age' : int(text)})
        await message.answer('Отлично. Нажмите /find чтобы найти собеседника')
        await state.set_state('find')
    else:
        await message.reply("Вы ввели не число. Повторите попытку")
        
waiting_users: set[int] = set()

@dp.message_handler(commands=['find'],state='find')
async def find_process(message: types.Message, state: FSMContext):
    await message.answer("Поиск собеседника...")
    waiting_users.add(message.from_user.id)
    await message.answer(waiting_users)
    
    if len(waiting_users) >= 2:
        for another_user in waiting_users:
            if another_user == message.from_user.id:
                continue
            else:
                break
        another_user
        await state.set_state("chatting")
        
        
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)