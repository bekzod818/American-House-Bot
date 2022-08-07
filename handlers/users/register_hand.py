from loader import dp, bot, db
from aiogram import types
from states.register_user import Register
from keyboards.inline import ages, regions
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.main import menu


@dp.message_handler(state=Register.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {'fullname': fullname}
    )
    await message.answer(f"{fullname} yoshingiz oraliqini tanglang", reply_markup=ages.interval)
    await Register.next()

@dp.callback_query_handler(state=Register.age)
async def get_age(call: types.CallbackQuery, state: FSMContext):
    age = call.data
    await call.message.delete()
    await state.update_data(
        {'age': age}
    )
    await call.answer(f"{age} yosh oraliqi tanlandi")
    await call.message.answer("Manzilingizni to'liq holatda kiriting", reply_markup=regions.viloyatlar)
    await Register.next()

@dp.callback_query_handler(state=Register.manzil)
async def get_manzil(call: types.CallbackQuery, state: FSMContext):
    viloyat = call.data
    await call.message.delete()
    await state.update_data(
        {'viloyat': viloyat}
    )
    await call.answer(f"{viloyat} tanlandi")
    await call.message.answer("Telefon raqamingizni tasdiqlang", reply_markup=regions.contact)
    await Register.next()

@dp.message_handler(content_types=['contact'], state=Register.contact)
async def get_contact(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    data = await state.get_data()
    db.update_user_data(fullname=data.get('fullname'), age=data.get('age'), address=data.get('viloyat'), phone=phone, tg_id=message.from_user.id)
    await message.answer("Barcha ma'lumotlar muvaffaqiyatli saqlandi", reply_markup=ReplyKeyboardRemove())
    kupon = db.get_coupon()
    await message.answer_photo(photo=kupon[0][1], caption=kupon[0][2], reply_markup=menu)
    await state.finish()

