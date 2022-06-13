from loader import dp
from aiogram.types import Message
# from keyboards.default import menu
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите товар из меню ниже",
                         reply_markup=menu)


@dp.message_handler(Text(equals=["start", "create", "enter"]))
async def get_button(message: Message):
    await message.answer(f"Вы выбрали {message.text}, Спасибо ",
                         reply_markup=ReplyKeyboardRemove())
