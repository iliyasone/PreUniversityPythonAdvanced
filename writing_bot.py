from aiogram import Bot, Dispatcher, types
from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

storage = MemoryStorage()



# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start','help'], state='*')
async def start_or_help_handler(message: types.Message, state: FSMContext):
    await message.reply("Добро пожаловать в тестового бота. Введите ваше имя")
    await state.set_state("name")

@dp.message_handler(state = 'name')
async def proc_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name" : name})
    await message.reply("Введите ваш возраст")
    await state.set_state("age")
    
@dp.message_handler(state = 'age')
async def proc_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data({"age" : age})
    await message.reply("Спасибо!")
    data = await state.get_data()
    
    await message.answer(f"Вы {data['name']}, {data['age']}")
    await state.set_state("free")
    
@dp.message_handler(state = "free")
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)




