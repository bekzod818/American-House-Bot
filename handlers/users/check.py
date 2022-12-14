from loader import dp, bot, db
from data.config import CHANNELS
from utils.misc import subscription
from aiogram import types
# from keyboards.default.new import menu
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.register_user import Register


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer("Kanallarga obunalar tekshirilmoqda")
    final_status = True
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        # print(status)
        if status:
            final_status *= status
            result += f"ā <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        
        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f"ā <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lmagansiz.\n\n")
    
    if final_status:
        await call.message.delete()
        data = db.select_user(tg_id=call.from_user.id)
        if None not in data:
            msg = f"Salom xush kelibsiz\nš¤ <b>{call.from_user.full_name}</b>!\nBizning ma'lumotlar š½"
            await call.message.answer(msg)
        else:
            msg = f"Assalomu alaykum! Marhamat ism-familyanggizni kiriting"
            await call.message.answer(msg)
            await Register.full_name.set()
    else:
        await call.message.delete()
        check_button = InlineKeyboardMarkup(row_width=1)

        for channel in CHANNELS:
            chat = await bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            check_button.insert(InlineKeyboardButton(text=f"A'zo bo'lish", url=invite_link))
        check_button.add(InlineKeyboardButton(text="A'zo bo'lish", url="https://www.instagram.com/americanhouse__/"))
        check_button.add(InlineKeyboardButton(text="ā Tasdiqlash", callback_data="check_subs"))
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=check_button)