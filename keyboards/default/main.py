from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏛 Universitet haqida")],
        [KeyboardButton(text="🏫 American House haqida")],
        [KeyboardButton(text="📚 Fakultetlar")],
        [KeyboardButton(text="📌 Imkoniyatlaringiz")]
    ],
    resize_keyboard=True
)