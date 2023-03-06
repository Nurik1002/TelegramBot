from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startKeyboard import  menuAdmin
from data.config import ADMINS
from loader import dp, db, bot
from states.adminState import Yosh, Jins, Doimi, Vaqtin, Ona, Ota, Talim
import logging
from keyboards.inline.anketaInlineKeyboard import jinsButton, doimiy_y_hButton, yashash_joyButton, ona_malButton, ota_malButton, talimButton


@dp.message_handler(CommandStart(), user_id=ADMINS)
async def admin_start(msg : types.Message):
    await msg.answer("Assalommu alaykum admin!", reply_markup=menuAdmin)

#------------------------------------------Ishtiroqchi soni------------------------------------------
@dp.message_handler(text="Sorovnomada ishtirok etganlar soni", user_id = ADMINS)
async def ishtiroqchi_soni(msg: types.Message):
    await msg.answer(text=f"So'rovnomada qatnashgan ishtirokchilar soni : {db.count_users()[0]}")
    
#------------------------------------------Umumiy statistika-------------------------------------
@dp.message_handler(text = "Umumiy statistika", user_id = ADMINS)
async def umumiy_stat(msg : types.Message):

    if db.count_users()[0] > 0:
        id = db.get_all_users()
        logging.info(f"{id}")
        test= db.get_test(id)
        data = db.get_statistic(test)
        await msg.answer(text=data)
    else:
        await msg.answer("So'rovnomada hali hechkim qatnashmadi!")

#------------------------------------------Yosh----------------------------------------------
@dp.message_handler(text = "Yosh statistika")
async def yosh_stat(msg : types.Message):
    await msg.answer("Yoshni kiriting!")
    await Yosh.yosh.set()


@dp.message_handler(state=Yosh.yosh)
async def yosh_kirit(msg : types.Message, state : FSMContext):    
    yosh = msg.text
    if yosh.isdigit():
        yosh = int(yosh)
        uid = db.select_yosh(yosh)
        test = db.get_test(uid)
        qatnashuvchi = len(test[0].split())
        data = db.get_statistic(test)
        qatnashuvchi = str(qatnashuvchi) + " ta qatnahuvchi topildi.\n"
        data = qatnashuvchi + data
        await msg.answer(text=data)
        await state.finish()
    else:
        await msg.answer("Iltimos son kiriting!")


#------------------------------------Jins statistika---------------------------------------
@dp.message_handler(text= "Jins statistika")
async def jins(msg : types.Message):
    await msg.answer(text="Jinsni tanlang", reply_markup=jinsButton)
    await Jins.jins.set()
    
@dp.callback_query_handler(state=Jins.jins)
async def get_jins(call : types.CallbackQuery, state : FSMContext):
    data = call.data
    data = db.select_jinsi(jins=data)
    test = db.get_test(data)
    qatnashuvchi = len(test[0].split())
    test = db.get_statistic(test)
    qatnashuvchi = str(qatnashuvchi) + " ta qatnahuvchi topildi.\n"
    test = qatnashuvchi + test
    await call.message.answer(text=test)
    await state.finish()

#-------------------------------------------Doimi yashash hududi statistika-----------------------------
@dp.message_handler(text = 'Doimiy yashash hududi statistika')
async def doimi(msg: types.Message):
    await msg.answer("Doimiy yashash hududini tanlang!", reply_markup=doimiy_y_hButton)
    await Doimi.doimi.set()
    
@dp.callback_query_handler(state=Doimi.doimi)
async def get_doimi(call : types.CallbackQuery, state : FSMContext):
    data = call.data
    data = db.select_doimi(doimi=data)
    test = db.get_test(data)
    qatnashuvchi = len(test[0].split())
    test = db.get_statistic(test)
    qatnashuvchi = str(qatnashuvchi) + " ta qatnahuvchi topildi.\n"
    test = qatnashuvchi + test
    await call.message.answer(text=test)
    await state.finish()
    
#-------------------------------------------Yashash joyi------------------------------------------------------

@dp.message_handler(text="Yashash joyi statistika")
async def yashash(msg: types.Message):
    await msg.answer(text="Yashash joyini tanlang", reply_markup=yashash_joyButton)
    await Vaqtin.vaqtin.set()
    
@dp.callback_query_handler(state=Vaqtin.vaqtin)
async def get_yashash(call : types.CallbackQuery, state : FSMContext):
    data = call.data
    data = db.select_vaqtinchalik(data)
    test = db.get_test(data)
    qatnashuvchi = len(test[0].split())
    test = db.get_statistic(test)
    qatnashuvchi = str(qatnashuvchi) + " ta qatnahuvchi topildi.\n"
    test = qatnashuvchi + test
    await call.message.answer(text=test)
    await state.finish()
    
#-----------------------------------------Ota ma'lumoti------------------------------------------------------

@dp.message_handler(text = "Otamning ma’lumoti statistika")
async def ota(msg: types.Message):
    await  msg.answer("Otamning ma’lumotini tanlang!" ,reply_markup=ota_malButton)
    await Ota.ota.set()

@dp.callback_query_handler(state=Ota.ota)
async def get_ota(call : types.CallbackQuery, state : FSMContext):
    data = call.data
    data = db.select_ota(data)
    test = db.get_test(data)
    qatnashuvchi = len(test[0].split())
    test = db.get_statistic(test)
    qatnashuvchi = str(qatnashuvchi) + " ta qatnahuvchi topildi.\n"
    test = qatnashuvchi + test
    await call.message.answer(text=test)
    await state.finish()
    
#---------------------------------------Ona ma'lumoti---------------------------------------------------

@dp.message_handler(text = "Onamning ma’lumoti statistika")
async def ota(msg: types.Message):
    await  msg.answer("Onamning ma’lumotini tanlang!" ,reply_markup=ona_malButton)
    await Ona.ona.set()

@dp.callback_query_handler(state=Ona.ona)
async def get_ota(call : types.CallbackQuery, state : FSMContext):
    data = call.data
    data = db.select_ona(data)
    test = db.get_test(data)
    qatnashuvchi = len(test[0].split())
    test = db.get_statistic(test)
    qatnashuvchi = str(qatnashuvchi) + " ta qatnahuvchi topildi.\n"
    test = qatnashuvchi + test
    await call.message.answer(text=test)
    await state.finish()
#--------------------------------------------Ta'lim -------------------------------------------------------------

@dp.message_handler(text = "Ta’lim olayapman statistika")
async def talim(msg : types.Message):
    await msg.answer("Ta’lim olayapman tanlang!", reply_markup=talimButton)
    await Talim.talim.set()
    
@dp.callback_query_handler(state=Talim.talim)
async def get_talim(call : types.CallbackQuery, state : FSMContext):
    data = call.data
    data = db.select_talim(data)
    test = db.get_test(data)
    qatnashuvchi = len(test[0].split())
    test = db.get_statistic(test)
    qatnashuvchi = str(qatnashuvchi) + " ta qatnahuvchi topildi.\n"
    test = qatnashuvchi + test
    await call.message.answer(text=test)
    await state.finish()
    
#-------------------------------------Statistika finish- --------------------------------------------------------
    








@dp.message_handler(text = "all user", user_id = ADMINS)
async def all_user(msg : types.Message):
    data = db.get_allUser()
    await msg.answer(text=data)

@dp.message_handler(text = "clear users", user_id = ADMINS)
async def clear_user(msg : types.Message):
    db.delete_users()
    await msg.answer("Barcha fo'ydalanuvchilar o'chirildi!")

@dp.message_handler(text = "all test", user_id = ADMINS)
async def all_test(msg : types.Message):
    data = db.get_all_test()
    await msg.answer(text=data)
    
@dp.message_handler(text = "delete tests", user_id = ADMINS)
async def del_test(msg: types.Message):
    db.delete_tests()
    await msg.answer("Barcha testlar o'chirildi!")