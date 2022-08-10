import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot
from data.config import CHANNELS
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.main import menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.username
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(tg_id=message.from_user.id,
                    username=name)

        check_button = InlineKeyboardMarkup(row_width=1)

        for channel in CHANNELS:
            chat = await bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            check_button.insert(InlineKeyboardButton(text=f"A'zo bo'lish", url=invite_link))
        check_button.add(InlineKeyboardButton(text="A'zo bo'lish", url="https://www.instagram.com/americanhouse__/"))
        check_button.add(InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="check_subs"))

        await message.answer(f"Botni ishga tushurish uchun va biz haqimizdagi yangiliklardan xabardor bo'lish uchun kanallarimizga a'zo bo'ling! \n\n",
                            reply_markup=check_button,
                            disable_web_page_preview=True)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        name = db.select_user(tg_id=message.from_user.id)[3]
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Assalomu aleykum {name}. Xush kelibsiz!", reply_markup=menu)
