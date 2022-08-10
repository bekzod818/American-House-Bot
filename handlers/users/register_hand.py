from loader import dp, bot, db
from aiogram import types
from states.register_user import Register, Slug
from keyboards.inline import ages, regions
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from keyboards.default.main import menu


@dp.message_handler(state=Register.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {'fullname': fullname}
    )
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer(f"Iltimos yosh oralig'ini tanlang", reply_markup=ages.interval)
    await Register.next()


@dp.message_handler(state=Register.age)
async def get_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(
        {'age': age}
    )
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer("Yashash hududinggizni tanlang!", reply_markup=regions.viloyatlar)
    await Register.next()


@dp.message_handler(state=Register.manzil)
async def get_manzil(message: types.Message, state: FSMContext):
    viloyat = message.text
    await state.update_data(
        {'viloyat': viloyat}
    )
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer("Telefon raqaminggizni jo'nating, Jo'natish uchun pastdagi raqamni yuborish tugmasini bosing👇🏻)", reply_markup=regions.contact)
    await Register.next()


@dp.message_handler(content_types=['contact'], state=Register.contact)
async def get_contact(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    data = await state.get_data()
    db.update_user_data(fullname=data.get('fullname'), age=data.get('age'), address=data.get('viloyat'), phone=phone,
                        tg_id=message.from_user.id)
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer("Sizning malumotlaringgiz saqlandi", reply_markup=ReplyKeyboardRemove())
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
                InlineKeyboardButton(text='📎 Batafsil ma\'lumot', url=f'{about[3]}')
            ],
            [
                InlineKeyboardButton(text='⬅️ Orqaga', callback_data='back')
            ]
        ]
    )
    await message.answer_photo(photo=about[-1], caption=about[1], reply_markup=markup)

@dp.callback_query_handler(text='back')
async def beck(call:types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer('Bosh menyuga qaytdinggiz ...',reply_markup=menu)

@dp.message_handler(text='🏫 Kompaniya haqida')
async def get_uni(message: types.Message):
    about = db.get_about(type='house')
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='📎 Batafsil ma\'lumot', url=f'{about[3]}')
            ],
            [
                InlineKeyboardButton(text='⬅️ Orqaga', callback_data='back')
            ]
        ]
    )
    await message.answer_photo(photo=about[-1], caption=about[1], reply_markup=markup)


@dp.message_handler(text='📚 Fakultetlar')
async def get_fak(message:types.Message):
    about = db.get_all_fac()
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in about:
        markup.insert(KeyboardButton(text=f'{i[1]}'))

    markup.add(KeyboardButton(text='⬅️ Orqaga'))
    await message.answer('Fakultetni tanlang ...', reply_markup=markup)
    await Slug.first.set()

@dp.callback_query_handler(state=Slug.first, text="back")
async def get_back_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Bosh menyuga qaytdinggiz...',reply_markup=menu)
    await state.finish()


@dp.message_handler(state=Slug.first, text="⬅️ Orqaga")
async def get_back_menu_default(message: types.Message, state: FSMContext):
    await message.answer('Bosh menyuga qaytdinggiz ...',reply_markup=menu)
    await state.finish()


@dp.callback_query_handler(text="back2")
async def get_fakultetlar(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    about = db.get_all_fac()
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in about:
        markup.insert(KeyboardButton(text=f'{i[1]}'))

    markup.add(KeyboardButton(text='⬅️ Orqaga'))
    
    await call.message.answer('Fakultetni tanlang ...',reply_markup=markup)
    await Slug.first.set()


@dp.message_handler(state=Slug.first)
async def get_slug_fakultet(message: types.Message, state:FSMContext):
    name = message.text
    about = db.get_fac(name=name)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"📱 Bog'lanish",url=f'{about[5]}')],
            [InlineKeyboardButton(text='⬅️ Orqaga',callback_data='back2')]
        ]
    )
    await message.answer_photo(photo=f'{about[3]}', caption=f'{about[4]}',reply_markup=markup)
    await state.finish()

@dp.message_handler(text='📌 Imkoniyatlar')
async def get_fak(message:types.Message):
    about = db.get_all_imkon()[0]
    print(about)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='⬅️ Orqaga', callback_data='back')]
        ]
    )
    await message.answer_photo(photo=about[1],caption=about[2],reply_markup=markup)