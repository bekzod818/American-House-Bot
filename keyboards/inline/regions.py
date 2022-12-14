from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

data = [
{"id":"1","name_uz":"Qoraqalpog'iston Respublikasi","name_oz":"?���?����?����� ������������","name_ru":"���������� ��������������"},
{"id":"2","name_uz":"Andijon viloyati","name_oz":"������� �������","name_ru":"����������� �������"},
{"id":"3","name_uz":"Buxoro viloyati","name_oz":"������ �������","name_ru":"��������� �������"},
{"id":"4","name_uz":"Jizzax viloyati","name_oz":"������ �������","name_ru":"���������� �������"},
{"id":"5","name_uz":"Qashqadaryo viloyati","name_oz":"?��?���� �������","name_ru":"��������������� �������"},
{"id":"6","name_uz":"Navoiy viloyati","name_oz":"������ �������","name_ru":"���������� �������"},
{"id":"7","name_uz":"Namangan viloyati","name_oz":"�������� �������","name_ru":"������������ �������"},
{"id":"8","name_uz":"Samarqand viloyati","name_oz":"�����?��� �������","name_ru":"������������� �������"},
{"id":"9","name_uz":"Surxandaryo viloyati","name_oz":"��������� �������","name_ru":"���������������� �������"},
{"id":"10","name_uz":"Sirdaryo viloyati","name_oz":"������ �������","name_ru":"������������� �������"},
{"id":"11","name_uz":"Toshkent viloyati","name_oz":"������� �������","name_ru":"����������� �������"},
{"id":"12","name_uz":"Farg'ona viloyati","name_oz":"���?��� �������","name_ru":"���������� �������"},
{"id":"13","name_uz":"Xorazm viloyati","name_oz":"������ �������","name_ru":"���������� �������"},
{"id":"14","name_uz":"Toshkent shahri","name_oz":"������� ��?��","name_ru":"����� �������"}]

viloyatlar = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
viloyatlar.row("Qoraqalpog'iston Respublikasi")
viloyatlar.row("Andijon viloyati", "Buxoro viloyati")
viloyatlar.row("Farg'ona viloyati", "Xorazm viloyati")
viloyatlar.row("Surxandaryo viloyati", "Toshkent shahri")
viloyatlar.row("Qashqadaryo viloyati")
viloyatlar.row("Samarqand viloyati", "Sirdaryo viloyati")
viloyatlar.row("Navoiy viloyati", "Namangan viloyati")
viloyatlar.row("Jizzax viloyati", "Toshkent viloyati")

contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)]
    ],
    resize_keyboard=True
)