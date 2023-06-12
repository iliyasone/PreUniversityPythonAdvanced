import asyncio
from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import logging
import token
from keyboards import *


# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

connected_users = []

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    message = await message.answer("Hi!\nI'm EchoBot!\nPowered by aiogram.\nPlease, "
                         "say your name",
                         reply_markup=keyboard2)
    
    await state.set_state("q1")


@dp.message_handler(state = "q1")
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name" : name})
    await state.set_state("q2")
    await message.answer("Say your age")
    
@dp.message_handler(state = "q2")
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if age.isdigit():
        await state.update_data({"age" : int(age)})
        await state.set_state("echo")
        await message.answer("Now I am echo-bot!", 
                             reply_markup=create_keyboard(0,0))
        connected_users.append(message.from_user.id)
        await bot.send_chat_action(message.from_user.id, types.ChatActions.TYPING)
    else:
        data = await state.get_data()
        await message.answer(f"This is not a number, try another time {data['name']}")


@dp.message_handler(state = "echo")
async def echo(message: Message):
    tasks = []
    for user in connected_users:
        if message.from_user.id == user:
            continue
        tasks.append(
            message.forward(user, drop_author=True)
            )
        types.MediaGroup()
        
    await asyncio.gather(*tasks)


a = b = 0
@dp.callback_query_handler(lambda c: c.data == 'i2')
async def process_callback_button(callback_query: types.CallbackQuery):
    global a, b
    b += 1
    
    await bot.answer_callback_query(callback_query.id, 'Callback Answered!')
    #await bot.send_message(callback_query.from_user.id, 'Палец вниз')
    
    await bot.edit_message_reply_markup(callback_query.from_user.id, 
                                        callback_query.message.message_id,
                                        reply_markup=create_keyboard(a, b))
    
    

    

@dp.callback_query_handler(lambda c: c.data == 'i1')
async def process_callback_button(callback_query: types.CallbackQuery):
    global a, b
    a += 1
    
    await bot.answer_callback_query(callback_query.id, 'Callback Answered!')
    #await bot.send_message(callback_query.from_user.id, 'Палец вверх')
    
    await bot.edit_message_reply_markup(callback_query.from_user.id, 
                                        callback_query.message.message_id,
                                        reply_markup=create_keyboard(a, b))
    
    
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)