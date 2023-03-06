from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startKeyboard import menuStart, menuAdmin
from data.config import ADMINS
from loader import dp, bot

# @dp.message_handler(CommandStart(), user_id = ADMINS)
# async def bot_start_admin(msg : types.Message):
#     await msg.answer("Assalomu alaykum admin!", reply_markup=menuAdmin)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu allaykum, biz “O’zbekistonada yoshlar ta’lim qadriyati mo’ljallarini shakllantirishning ijtimoiy omillari” mavzusida so'rovnoma o’tkazmoqdamiz, tadqiqotda yoshlarning ta’limga nisbatan qiziqish va qadriyatlarini o’rganishga yo'naltirilgan bo’lib, bir necha daqiqa ajratishingizni so’raymiz. To’g’ri va noto’g’ri javoblar yo’q, biz faqat sizning shaxsiy fikringiz bilan qiziqamiz. So'rovnomada ishtirok etsangiz, yordamingiz uchun minnatdor bo'lamiz. (Ushbu so'rovnoma 16 yoshdan 20 yoshgacha bo'lgan yoshlarga mo'ljallangan!)", reply_markup=menuStart)
    await message.answer("Testni boshlash uchun <b>Ro'yxatdan o'tish</b> tugmasini bosing!")
