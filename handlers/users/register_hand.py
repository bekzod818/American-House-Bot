from loader import dp, bot, db
from aiogram import types
from states.register_user import Register, Slug
from keyboards.inline import ages, regions
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
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
    db.update_user_data(fullname=data.get('fullname'), age=data.get('age'), address=data.get('viloyat'), phone=phone,
                        tg_id=message.from_user.id)
    await message.answer("Barcha ma'lumotlar muvaffaqiyatli saqlandi", reply_markup=ReplyKeyboardRemove())
    kupon = db.get_coupon()
    await message.answer_photo(photo=kupon[0][1], caption=kupon[0][2], reply_markup=menu)
    await state.finish()


@dp.message_handler(text='🏛 Universitet haqida')
async def get_uni(message: types.Message):
    about = db.get_about(type='univer')
    print(about)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Batafsil malumot', url=f'{about[3]}')
            ],
            [
                InlineKeyboardButton(text='Orqaga', callback_data='back')
            ]
        ]
    )
    await message.answer(text=about[1], reply_markup=markup)

@dp.callback_query_handler(text='back')
async def beck(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Kerakli tugmani bosing',reply_markup=menu)

@dp.message_handler(text='🏫 American House haqida')
async def get_uni(message: types.Message):
    about = db.get_about(type='house')
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Batafsil malumot', url=f'{about[3]}')
            ],
            [
                InlineKeyboardButton(text='Orqaga', callback_data='back')
            ]
        ]
    )
    await message.answer(text=about[1], reply_markup=markup)

@dp.message_handler(text='📚 Fakultetlar')
async def get_fak(message:types.Message):
    about = db.get_all_fac()
    keyboards = []
    for i in about:
        row = []
        row.append(InlineKeyboardButton(text=f'{i[1]}',callback_data=f'{i[2]}'))
        keyboards.append(row)
    row = []
    row.append(InlineKeyboardButton(text='Orqaga',callback_data='back'))
    keyboards.append(row)
    markup = InlineKeyboardMarkup(inline_keyboard=keyboards)
    await message.answer('Fakultetni tanlang!',reply_markup=markup)
    await Slug.first.set()

@dp.callback_query_handler(state=Slug.first)
async def get_slug(call:types.CallbackQuery,state:FSMContext):
    SLUG = call.data
    await call.message.delete()
    about = db.get_fac(slug=SLUG)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"Aloqa qilish",url=f'{about[5]}')],
            [InlineKeyboardButton(text='Orqaga',callback_data='back')]
        ]
    )
    await call.message.answer_photo(photo=f'{about[3]}',caption=f'{about[4]}',reply_markup=markup)
    await state.finish()

@dp.message_handler(text='📌 Imkoniyatlaringiz')
async def get_fak(message:types.Message):
    about = db.get_all_imkon()[0]
    print(about)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Orqaga',callback_data='back')]
        ]
    )
    await message.answer_photo(photo=about[1],caption=about[2],reply_markup=markup)