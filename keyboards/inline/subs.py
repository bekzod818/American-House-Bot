from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.config import CHANNELS
from loader import bot

check_button = InlineKeyboardMarkup(row_width=1)

# for channel in CHANNELS:
#     chat = bot.get_chat(channel)
#     invite_link = chat.export_invite_link()
#     check_button.insert(InlineKeyboardButton(text=f"{chat.title}", url=invite_link))

# check_button.add(InlineKeyboardButton(text="✔️ Obunani tekshirish", callback_data="check_subs"))