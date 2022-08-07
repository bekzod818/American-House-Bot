from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


interval = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="17 yoshdan - 22 yoshgacha", callback_data="17-22")],
        [InlineKeyboardButton(text="22 yoshdan - 35 yoshgacha", callback_data="22-35")]
    ]
)