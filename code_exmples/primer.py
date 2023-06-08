import logging
import gspread
from google.oauth2 import service_account
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6107486282:AAHIGdVe5QjNOlT1bfnbv-0mAnjRh5WhjHk')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

G_sheet_C = 'D:\tornado\tornado-388014-275c2f694c9b.json'
S_name = 'tornado'


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message, state: FSMContext):
    await message.reply("Добро пожаловать в торандо. Как вас зовут?")
    await state.set_state("name")


@dp.message_handler(state="name")
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.reply("Пожалуйста введите свой возраст")
    await state.set_state("age")


@dp.message_handler(state="age")
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    await message.reply("Пожалуйста введите свой пол")
    await state.set_state("gender")


@dp.message_handler(state="gender")
async def process_gender(message: types.Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
    await message.reply("Пожалуйста введите свой мобильный телефон")
    await state.set_state("phone_number")


@dp.message_handler(state="phone_number")
async def process_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()
    await state.reset_state()
    await message.reply("Запись была произведена успешно. Спасибо, мы вам перезвоним!")

    save_to_google_sheets(data)


def save_to_google_sheets(data):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(G_sheet_C, ['https://spreadsheets.google.com/feeds'])
    gc = gspread.authorize(credentials)
    sheet = gc.open(S_name).sheet1
    next_row = len(sheet.get_all_values()) + 1
    sheet.update_cell(next_row, 1, data.get('name'))
    sheet.update_cell(next_row, 2, data.get('age'))
    sheet.update_cell(next_row, 3, data.get('gender'))
    sheet.update_cell(next_row, 4, data.get('phone_number'))


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)