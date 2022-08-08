from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏛 Universitet haqida")],
        [KeyboardButton(text="🏫 American House haqida")],
        [KeyboardButton(text="📚 Fakultetlar")],
        [KeyboardButton(text="📌 Imkoniyatlar")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)