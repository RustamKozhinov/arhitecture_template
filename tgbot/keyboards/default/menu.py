from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="start")
        ],
        [
            KeyboardButton(text="create"),
            KeyboardButton(text="enter")
        ],
    ],
    resize_keyboard=True
)
