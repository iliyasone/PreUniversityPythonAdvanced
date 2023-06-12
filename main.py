from __future__ import annotations
#from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import logging
from keyboards import *





# Initialize bot and dispatcher
bot = Bot(token= "6145666899:AAGOGm8anLXoldGuUfcxrNBoKjIF8u4gJxI")
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
    current_user = message.from_user.id
    waiting_users.add(current_user)
    await message.answer(waiting_users)
    
    if len(waiting_users) >= 2:
        for another_user in waiting_users:
            if another_user == current_user:
                continue
            else:
                break
        waiting_users.remove(current_user)
        waiting_users.remove(another_user)            
        
        
        another_user_state = dp.current_state(chat=another_user, user=another_user)

        await state.set_state("chatting")
        await another_user_state.set_state("chatting")
        
        await state.update_data({"target" : another_user})
        await another_user_state.update_data({"target" : current_user})
        
        
        await bot.send_message(current_user, "Найден собеседник! Начинайте общаться")
        await bot.send_message(another_user, "Найден собеседник! Начинайте общаться")


@dp.message_handler(state='chatting')
async def chatting_proc(message: types.Message, state: FSMContext):
    another_user_data = await state.get_data()
    another_user = another_user_data['target']
    await bot.send_message(another_user, message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
    
