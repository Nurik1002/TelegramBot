from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Ro\'yxatdan o\'tish')
        ]
    ],
    resize_keyboard=True
)

menuAdmin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sorovnomada ishtirok etganlar soni")
        ],
        [
            KeyboardButton(text="Umumiy statistika"),
            #KeyboardButton(text="Tanlash bo'yicha statistika")
        ],
        [
            KeyboardButton(text="Yosh statistika"),
            KeyboardButton(text="Jins statistika"),
        ],
        [
            KeyboardButton(text="Doimiy yashash hududi statistika"),
            KeyboardButton(text="Yashash joyi statistika"),
        ],
        [
            KeyboardButton(text="Otamning ma’lumoti statistika"),
            KeyboardButton(text="Onamning ma’lumoti statistika"),
        ],
        [
            KeyboardButton(text="Ta’lim olayapman statistika")
        ],
    ],
    resize_keyboard=True
)
