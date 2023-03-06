from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states.userAnketaStates import UserAnketaStates
from loader import dp, db
from keyboards.inline.anketaInlineKeyboard import jinsButton, doimiy_y_hButton, yashash_joyButton, ona_malButton, ota_malButton, talimButton
import logging
from keyboards.inline.testInlineKeyboard import test_1Button
from states.testState import TestState



@dp.message_handler(text="Ro'yxatdan o'tish")
async def royxatdan_otish(msg:Message):

    await msg.answer("Yoshingizni kiriting!")
    await UserAnketaStates.s_yoshi.set()

@dp.message_handler(state=UserAnketaStates.s_yoshi)
async def set_yosh(msg : Message, state : FSMContext):
    yosh = msg.text
    if not yosh.isdigit() or 15 > int(yosh)  or int(yosh) > 25:
        await msg.answer("Iltimos son kirting yoki yosh oralig'ini to'g'ri kiriting!(Yosh oralig'i 15 yoshdan 25 yoshgacha)")
    else:
        await state.update_data(
            {
                "id" : msg.from_user.id,
                "full_name" : msg.from_user.full_name,
                "yosh" : yosh
            }
        )

        await msg.answer("Jinsingizni tanlang!", reply_markup=jinsButton)
        await UserAnketaStates.s_jinsi.set()



@dp.callback_query_handler(state=UserAnketaStates.s_jinsi)
async def get_jinsi(call:CallbackQuery, state : FSMContext):
    callback_data = call.data
    await state.update_data(
        {
            "jinsi" : callback_data
        }
    )
    await UserAnketaStates.next()


    await call.message.answer("Doimiy yashash hududingzini tanlang!", reply_markup=doimiy_y_hButton)
    await call.answer(cache_time=60)



@dp.callback_query_handler(state=UserAnketaStates.s_doimiy_yashash_hududi)
async def get_doimiy_yashash(call : CallbackQuery, state : FSMContext):
    callback_data = call.data

    await state.update_data(
        {
            "doimiy_yashash" : callback_data
        }
    )

    await UserAnketaStates.next()    
    await call.message.answer("Yashash joyingizni tanlang!", reply_markup = yashash_joyButton)
    await call.answer(cache_time=60)

@dp.callback_query_handler(state=UserAnketaStates.s_yashash_joyi)
async def get_yashash_joyi(call : CallbackQuery, state : FSMContext):
    callback_data = call.data
    await state.update_data(
        {
            "yashash_joyi" : callback_data
        }
    )

    await UserAnketaStates.next()
    await call.message.answer("Otamning ma'lumoti", reply_markup = ota_malButton)
    await call.answer(cache_time=60)

@dp.callback_query_handler(state=UserAnketaStates.s_otamning_mal)
async def get_ota_mal(call : CallbackQuery, state : FSMContext):
    callback_data = call.data
    await state.update_data(
        {
            "ota_mal" :  callback_data
        }
    )

    await UserAnketaStates.next()
    await call.message.answer("Onamning ma'lumoti", reply_markup=ona_malButton)    
    await call.answer(cache_time=60)

@dp.callback_query_handler(state=UserAnketaStates.s_onamning_mal)
async def get_ona_mal(call : CallbackQuery, state : FSMContext):
    callback_data = call.data
    await state.update_data(
        {
            "ona_mal" : callback_data
        }
    )

    await UserAnketaStates.next()
    await call.message.answer("Ta'lim olayapman", reply_markup=talimButton)
    await call.answer(cache_time=60)

@dp.callback_query_handler(state=UserAnketaStates.s_talim_olyapman)
async def get_talim(call : CallbackQuery, state : FSMContext):
    callback_data = call.data
    
    await state.update_data(
        {
            "talim" : callback_data
        }
    )
    
    data   = await state.get_data()
    qaytar = list(data.values())
    try:
        db.add_user(qaytar[0], qaytar[1],qaytar[2],qaytar[3],qaytar[4],qaytar[5], qaytar[6], qaytar[7], qaytar[8])
    except Exception as err:
        print(err)
        
    qaytar = str(qaytar)
    logging.info(qaytar)
    await call.message.answer("Testni  boshlandi!")

    await state.finish()
    await call.message.answer("""1. Ta’lim olishda quyidagi milliy internet resurslaridan qay birini qulay deb hisoblaysiz?
         A. ziyonet.uz
         B. abt.uz  
         C. ta’lim.uz 
         D. natlib.uz 
         E. Men umuman foydalanmayman
        """, reply_markup=test_1Button)
    await TestState.test1.set()



