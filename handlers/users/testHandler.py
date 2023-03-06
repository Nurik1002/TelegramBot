from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from states.testState import TestState
from loader import dp, db

from keyboards.inline.testInlineKeyboard import (
test_2Button,
test_4Button,
test_5Button,
test_6Button,
test_7Button,
test_8Button,
test_9Button,
test_12Button,
test_16Button,
test_17Button,
test_19Button
)
import logging



@dp.callback_query_handler(state=TestState.test1)
async def test_1(call : CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"2 : {data}")
    await state.update_data(
        {
            "id" : call.message.chat.id,
            "test_1" : data,
            "fikr_2" : None,
            "fikr_5" : None,
            "fikr_7" : None,
            "fikr_9" : None,
            "fikr_13" : None,
            "fikr_15" : None,
            "fikr_16" : None,
            "fikr_17" : None,
            "fikr_18" : None,
            "fikr_19" : None
        }
    )

    await TestState.next()
    await call.message.answer(
        """2. Farovon hayotga ega bo’lish uchun nima muhim deb hisoblaysiz?
 A. Ota-onaning moddiy qo’llab quvvatlashi.
 B. Xorijiy davlatga chiqib ishlab kelish (AQSH, Evropa, Rossiya).
 C. Ta’lim.
 D. Kasb-hunar egallash. 
 E. Dehqonchilik va chorvachilikni yo’lga qo’yish. 
 F. O’zingizning fikringiz yozib qoldiring.
""", reply_markup=test_2Button)
    await call.answer(cache_time=60)

@dp.callback_query_handler(state=TestState.test2)
async def test_2(call : CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"2 : {data}")
    await state.update_data(
        {
            "test_2" : data
        }
    )

    if data != "F":
        await TestState.next()

        await call.message.answer(
            """3. Kasb tanlashda ko’proq kimning maslahatiga suyanasiz? <b>(bir nechta variantlarni tanlash mumkin <i>2</i> ta variantni yozib yuboring!\nHarflar bilan yozib yuboring. Masalan : a b!)</b>
 A. Qarindoshlar (amakilar, tog’alarim)
 B. Yaqin do’stlarim, o’rtoqlarim.
 C. O’qituvchi (repetitor) ustozlarim. 
 D. Ota onam va opa-akalarim.
 E. O’zimning qiziqishim va internet saytlaridan olgan ma’lumotlarim.""")
        await call.answer(cache_time=60)

    else:
        await call.message.answer("Iltimos o'z fikringizni yozib yuboring!")


@dp.message_handler(state=TestState.test2)
async def test_2_E(msg : Message, state : FSMContext):
    data = msg.text
    logging.info(f"2 E : {data}")
    await state.update_data(
        {
            "fikr_2" :  str(data)
        }
    )

    await TestState.next()

    await msg.answer("""3. Kasb tanlashda ko’proq kimning maslahatiga suyanasiz? (2 ta variantni tanlashingiz mumkin!)
A. Qarindoshlar (amakilar, tog’alarim)
B. Yaqin do’stlarim, o’rtoqlarim.
C. O’qituvchi (repetitor) ustozlarim. 
D. Ota onam va opa-akalarim.
E. O’zimning qiziqishim va internet saytlaridan olgan ma’lumotlarim.""")


@dp.message_handler(state=TestState.test3)
async def test_3(msg : Message, state : FSMContext):
    data = msg.text.upper()
    vlist = ["A", "B", "C", "D", "E"]
    chek = data.split()
    chek1 = ""
    for i in chek :
        chek1 += i
    chek = chek1
    x = True
    if len(chek) > 2:
        await msg.answer("Maksimum 2 ta variant yozib yuboring!")
        x = False
    if chek[0] not in vlist:
        await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
        x = False
    if len(chek) == 2:
        if chek[1] not in vlist:
            await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
            x = False
    if x:
        logging.info(f"3 : {data}")
        await state.update_data(
            {
                "test_3" : data
            }
        )
        
        await TestState.next()
        await msg.answer("""4. Ta’lim olgan maktabingizni 5 ballik baholashda nechaga baholaysiz? (1-eng past baldan eng yuqori ball 5 ga o’sib boradi)
A. 1. 
B. 2. 
C. 3. 
D. 4.
E. 5.""", reply_markup=test_4Button)


@dp.callback_query_handler(state=TestState.test4)
async def test_4(call : CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"4 : {data}")
    await state.update_data(
        {
            "test_4" : data
        }
    )


    await TestState.next()
    await call.message.answer("""5. Kelajakda qaysi sohani tanlaysiz va nima sababdan?
 A. bank, moliya
 B. ta’lim 
 C. sog’liqni saqlash
 D. shaxsiy tanlovim 
""", reply_markup=test_5Button)



@dp.callback_query_handler(state=TestState.test5)
async def test_5(call : CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"5 : {data}")
    await state.update_data(
        {
            "test_5" : data
        }
    )

    if data == "D" :
        await call.message.answer("O'z tanlovingizni yozib yuboring!")
        #await call.message.delete()
    else:
        await TestState.next()
        await call.message.answer("""6. Ushbu sohalarni tanlashga ...................... sabab bo’lishi mumkin. 
A. Oylik ish haqqi 
B. Yaqinlarim (ota-onam va qarindoshlarimning) maslahati 
C. Shaxsiy qiziqishim va shu sohani rivojlantirish 
D. Bilmadim""", reply_markup=test_6Button)
        await call.answer(cache_time=60)


@dp.message_handler(state=TestState.test5)
async def test_5_1(msg:Message, state : FSMContext):
    data = msg.text
    logging.info(f"5 D : {data}")
    await state.update_data(
        {
            "fikr_5" : data
        }
    )

    await TestState.next()
    await msg.answer("""6. Ushbu sohalarni tanlashga ...................... sabab bo’lishi mumkin. 
A. Oylik ish haqqi 
B. Yaqinlarim (ota-onam va qarindoshlarimning) maslahati 
C. Shaxsiy qiziqishim va shu sohani rivojlantirish 
D. Bilmadim""", reply_markup=test_6Button)


@dp.callback_query_handler(state=TestState.test6)
async def test_6(call :  CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"6 : {data}")
    await state.update_data(
        {
            "test_6" : data
        }
    )

    await TestState.test7.set()
    await call.message.answer("""7. Yaxshi ta’lim olmaslik jamiyatda qanday holatlarni yuzaga keltirishi mumkin, deb hisoblaysiz ?
A. qashshoqlik xavfi
B. atrof muhit ifloslanishi 
C. xorijga chiqib ishlab kelishning kuchayishi. 
D. jinoyatchilk ortib ketishi  
E. fikringiz____________""", reply_markup=test_7Button)
    await call.answer(cache_time=60)
    await TestState.test7.set()

@dp.callback_query_handler(state=TestState.test7)
async def test_7(call : CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"7 : {data}")
    await state.update_data(
        {
            "test_7" : data
        }
    )
    if data !="E":
        await TestState.next()
        await call.message.answer("""8. Qaysi sabablar ta’lim olishga  undashi mumkin ?
Men uchun asosan quyidagi sabab ta’lim olishimga ......... turtki beradi.
A. ...ko’proq pul topish
B. ...o’zim qiziqan lavozimda ishlash
C. ...shaxsiy rivojlanish (atrofdagilar tomonidan e’tirof etilish) 
D. ...oilam mendan faxrlanishi""", reply_markup=test_8Button)
        await call.answer(cache_time=60)
    else:
        await call.message.answer("Iltimos o'z fikringizni qoldiring!")


@dp.message_handler(state=TestState.test7)
async def test_7_1(msg : Message, state :  FSMContext):
    data = msg.text
    logging.info(f"7 E : {data}")
    await state.update_data(
        {
            "fikr_7"  : data
        }
    )
    await TestState.next()
    await msg.answer("""8. Qaysi sabablar ta’lim olishga  undashi mumkin ?
Men uchun asosan quyidagi sabab ta’lim olishimga ......... turtki beradi.
A. ...ko’proq pul topish
B. ...o’zim qiziqan lavozimda ishlash
C. ...shaxsiy rivojlanish (atrofdagilar tomonidan e’tirof etilish) 
D. ...oilam mendan faxrlanishi""", reply_markup=test_8Button)

@dp.callback_query_handler(state=TestState.test8)
async def test_8(call : CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"8 : {data}")
    await state.update_data(
        {
            "test_8" : data
        }
    )

    await TestState.next()
    await call.message.answer("""9. Sifatli ta’lim tushunchasini tavsiflang....
A. zamonaviy o’quv- qurollari va texnologiyalari bilan ta’minlanganlik
B. qattiq qo’llikka asoslangan ta’limning olib borilishi (oqituvchi va o’quvchilarga nisbatan)
C. o’quvchilar asosiy vaqtini ta’lim muassasida o’tkazishadi yagona formaga amal qiladi.
D. bepul ovqatlanishning tashkil etilishi va ta’lim yotoqxonasi barcha ta’lim oluvchilarni qamrab olishi.
E. Fikrimni yozaman""", reply_markup=test_9Button)
    await call.answer(cache_time=60)

@dp.callback_query_handler(state=TestState.test9)
async def test_9(call : CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"9 : {data}")
    await state.update_data(
        {
            "test_9" : data
        }
    )
    if data != "E":
        await TestState.next()
        await call.message.answer("""10. Bir kunda necha soat bо‘sh vaqtingiz  (uyqu, maktab, OTMdagi dars va uydagi qoshimcha mashg‘ulotlardan tashqari ) bor? \
mening shaxsiy bо‘sh vaqtim _____ soat. <b>Iltimos soatni raqamda yozib qoldiring!</b>""")
    else:
        await call.message.answer(f"O'z fikringizni yozib qoldiring!")
@dp.message_handler(state=TestState.test9)
async def test_9_E(msg : Message, state : FSMContext):
    data = msg.text
    logging.info(f"9 E : {data}")
    await state.update_data(
        {
            "fikr_9" :  data
        }
    )

    await TestState.next()
    await msg.answer("""10. Bir kunda necha soat bо‘sh vaqtingiz  (uyqu, maktab, OTMdagi dars va uydagi qoshimcha mashg‘ulotlardan tashqari ) bor? \
mening shaxsiy bо‘sh vaqtim _____ soat. <b>Iltimos soatni raqamda yozib qoldiring!</b>""")

@dp.message_handler(state=TestState.test10)
async def test_10(msg : Message, state : FSMContext):
    dataint = msg.text
    if not dataint.isdigit():
        await msg.answer("Iltimos son kiriting!")
    else :
        dataint = int(dataint)
        if 1<= dataint <= 10:
            await state.update_data(
                {
                    "test_10": dataint
                }
            )
            await TestState.next()
            await msg.answer("""11. Necha yoshdan  bola vaqtini tо‘g‘ri taqsimlashda kattalar ishtirok etish kerak deb hisoblaysiz? shaxsiy fikrim _____ yoshdan?\n<b>Iltimos yoshni raqamda kiriting!</b>""")
        else:
            await msg.answer("10 soatdan kam vaqt kirting!")

@dp.message_handler(state=TestState.test11)
async def test_11(msg : Message, state : FSMContext):
    data = msg.text
    if data.isdigit():
        dataint = int(data)
    else:
        await msg.answer("Iltimos son kiriting!")

    if  0 < dataint <= 18:
        logging.info(f"11 : {data}")
        await state.update_data(
        {
            "test_11" : data
        }
    )

        await TestState.next()

        await msg.answer("""12. Quyidagi holatlardan qaysi biriga duch kelayapsiz yoki duch kelgansiz…
A. o’z orzuimdagi kasbni (sohani) tanlsh / o’qishni davom etirish
B. ma’qul keladigan ta’lim turini tanlash (kunduzgi, sirtqi, onlayn)
C. ish qidirish
D. yaxshi ta’minlangan yashash sharoiti va boshqa joyga ko’chish imkoniyatining mavjudligi.""", reply_markup=test_12Button)
    else:
        await msg.answer("Iltimos 18 yoshgacha kiritng!")

@dp.callback_query_handler(state=TestState.test12)
async def test_12(call : CallbackQuery, state = FSMContext ):
    data = call.data.upper()
    logging.info(f"12 : {data}")
    await state.update_data(
        {
            "test_12" : data
        }
    )

   
    await TestState.next()
    await call.message.answer("""13. Sizningcha, kasbiy muvaffaqiyatga erishishda quyidagilardan muhim hisoblanadigan ikki holatni belgilang? <b> Muhimlik darajasiga ko’ra <i>2</i> javobni yozib yuboring</b>.
A. omad  
B. diplom
C. shaxsiy harakat
D. munosabatlar, “biror kishining g’amxo’rligi”
E. insoning kelib chiqishi (biror hududga, sulolaga, millatga ta’luqlli bo’lish)
F. ta’lim mutaxasisligini tanlash
G. Fikringiz """)
    await call.answer(cache_time=60)


# ["A", "B", "C", "D", "E", "F", "G"]

@dp.message_handler(state=TestState.test13)
async def test_13(msg : Message, state : FSMContext):
    data = msg.text.upper()
    vlist = ["A", "B", "C", "D", "E", "F", "G"]
    chek = data.split()
    chek1 = ""
    for i in chek :
        chek1 += i
    chek = chek1
    x = True
    if len(chek) > 2:
        await msg.answer("Maksimum 2 ta variant yozib yuboring!")
        x = False
    if chek[0] not in vlist:
        await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
        x = False
    if len(chek) == 2:
        if chek[1] not in vlist:
            await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
            x = False
    if x:
        logging.info(f"13 : {data}")
        await state.update_data(
            {
                "test_13"  : data
        }
        )



        if "G" in data:
            await msg.answer("O'z fikringizni yozib qoldiring!")
            await TestState.test13_1.set()
        else :
            await TestState.test14.set()

            await msg.answer("""14. Quyidagi keltrilganlardan qaysi uchtalikni birinchi bo’lib muhim deb hisoblaysiz va asosiy shularga e’tibor qaratasiz? <b>(Ketma ket <i>3</i> ta variantni yozib yuboring!)</b>
A. yoshlar hayoti va turmush tarzi
B. yoshlarning kelajak mo’ljalari, kasblar, ta’lim sohalari
C. ish axtarish
D. zararli narsalarni istemol qilish (tamaki, alkogol, giyohvand)
E. zo’ravonlik (bosqinchilik, nomusni toptash)
F. sevgi-muhabbat munosabatlari
G. ishonchsizlik
H. siyosiy jarayonlar
I. yashash hududi yangiliklar (mahalla, mavzey, qishloq, ovul)
J. hordiq chiqarish""")

@dp.message_handler(state=TestState.test13_1)
async def test_13_G(msg : Message, state : FSMContext):
    data = msg.text
    logging.info(f"13 G : {data}")
    await state.update_data(
        {
            "test_13" :  data
        }
    )
    await TestState.test14.set()
    await msg.answer("""14. Quyidagi keltrilganlardan qaysi uchtalikni birinchi bo’lib muhim deb hisoblaysiz va asosiy  e’tibor qaratasiz? <b>(Ketma ket <i>3</i> ta variantni yozib yuboring!)</b>
A. yoshlar hayoti va turmush tarzi
B. yoshlarning kelajak mo’ljalari, kasblar, ta’lim sohalari
C. ish axtarish
D. zararli narsalarni istemol qilish (tamaki, alkogol, giyohvand)
E. zo’ravonlik (bosqinchilik, nomusni toptash)
F. sevgi-muhabbat munosabatlari
G. ishonchsizlik
H. siyosiy jarayonlar
I. yashash hududi yangiliklar (mahalla, mavzey, qishloq, ovul)
J. hordiq chiqarish""")

@dp.message_handler(state=TestState.test14)
async def test_14(msg : Message, state : FSMContext):
    data = msg.text.upper()
    vlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    chek = data.split()
    chek1 = ""
    for i in chek :
        chek1 += i
    chek = chek1
    x = True
    if len(chek) > 3:
        await msg.answer("Maksimum 3 ta variant yozib yuboring!")
        x = False
    if chek[0] not in vlist:
        await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
        x = False
    if len(chek) == 2:
        if chek[1] not in vlist:
            await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
            x = False
    if len(chek) == 3:
        if chek[2] not in vlist:
            await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
            x = False
    if x:
        logging.info(f"14 : {data}")
        await state.update_data(
            {
                "test_14" : data
            }
        )
        await TestState.next()

        await msg.answer("""15. Umuman olganda, qaysi turdagi axborotlarga nisbatan ehtiyojingiz bor? <b>(bir vaqtda uchta <i>  3 ta </i> javobni belgilashingiz mumkin) </b>
A. ta’lim/ ta’lim olish
B. kasblar
C. ishga taklif
D. amaliy hayot (transport, kasbiy ish soatlarining har xilligi)
E. sport va hordiq chiqarish
F. sog’lik (ehtiyot korlik nuqtai-nazaridan…)
G. turar joy
H. xorijga chiqish rejalari (ta’lim olish, ishlash, sayohat uchun)
I. oz fikrimni yozib qoldiraman """)

@dp.message_handler(state=TestState.test15)
async def test_15(msg : Message, state : FSMContext):
    data = msg.text.upper()
    chek = data.split()
    vlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    chek1 = ""
    for i in chek :
        chek1 += i
    chek = chek1
    x = True
    if len(chek) > 3:
        await msg.answer("Maksimum 3 ta variant yozib yuboring!")
        x = False
    if chek[0] not in vlist:
        await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
        x = False
    if len(chek) == 2:
        if chek[1] not in vlist:
            await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
            x = False
    if len(chek) == 3:
        if chek[2] not in vlist:
            await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
            x = False
    if x:
        logging.info(f"15 : {data}")
        await state.update_data(
            {
                "test_15" : data
            }
        )


        if "I" in data:
            await msg.answer("O'z fikringizni yozib qoldiring!")
            await TestState.test15_1.set()
        else:
            await TestState.test16.set()

                
            await msg.answer("""16. Badiy asar, kino, serial,filmlarda ta’lim orqali insonni barkamolikka etaklovchi, motivasiya beruvchi g’oyalar, fikrlarini keltira olasizmi <b>(film, asar nomini yoki qahramon nomini keltiring)</b>?
A. Ha. (O'z fikringizni yozib qoldiring)
B. Yo’q. duch kelmaganman.
C. Qiziqmayman.""", reply_markup=test_16Button)

@dp.message_handler(state=TestState.test15_1)
async def test_15_I(msg : Message, state : FSMContext):
    data = msg.text
    logging.info(f"15 I : {data}")
    await state.update_data(
        {
            "fikr_15" : data
        }
    )
    await TestState.test16.set()
    await msg.answer("""16. Badiy asar, kino, serial,filmlarda ta’lim orqali insonni barkamolikka etaklovchi, motivasiya beruvchi g’oyalar, fikrlarini keltira olasizmi <b>(film, asar nomini yoki qahramon nomini keltiring)</b>?
A. Ha. (O'z fikringizni yozib qoldiring)
B. Yo’q. duch kelmaganman.
C. Qiziqmayman.""", reply_markup=test_16Button)

@dp.callback_query_handler(state=TestState.test16)
async def test_16(call : CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"16 : {data}")
    await state.update_data(
        {
            "test_16" : data
        }
    )

    if data == "A":
        await call.message.answer("O'z fikringizni yozib qoldiring!")
    else :
        await TestState.next()
        await call.message.answer("""17. Televizor va internet insonga qanchalik darajada ruhiy taskin berishi mumkin?
A. 30-40% 
B. 40-50% 
C. 50-60%. 
D.60-80% 
E. shaxsiy fikrim ____ % (foizni kiriting!)""", reply_markup=test_17Button)
        await call.answer(cache_time=60)

@dp.message_handler(state=TestState.test16)
async def test_16_1(msg : Message, state : FSMContext):
    data = msg.text
    logging.info(f"16 E : {data}")
    await state.update_data(
        {
            "fikr_16"  : data
        }
    )
    await TestState.next()
    await msg.answer("""17. Televizor va internet insonga qanchalik darajada ruhiy taskin berishi mumkin?
A. 30-40% 
B. 40-50% 
C. 50-60%. 
D.60-80% 
E. shaxsiy fikrim ____ % (foizni kiriting!)""", reply_markup=test_17Button)

@dp.callback_query_handler(state=TestState.test17)
async def test_17(call : CallbackQuery, state : FSMContext):
    data = call.data.upper()
    logging.info(f"17 : {data}")
    await state.update_data(
        {
            "test_17" : data
        }
    )

    if data == "E":
        await call.message.answer("O'z fikringizni yozib qoldiring!")

    else:
        await TestState.next()
        await call.message.answer("""18. So'ngi vaqtlarda ta’limga ta’luqli qaysi ijtimoiy tarmoqlarni ko'proq kuzatyapsiz <b>(3 ta variantni yozib qoldirishingiz ham mumkin!)</b> ?
A. Youtube 
B. Telegram 
C. TIkTok 
D. Instagram 
C. Twitter 
E. Facebook
G. Mening tanlovim """)

@dp.message_handler(state=TestState.test17)
async def test_17_1(msg : Message, state : FSMContext):
    data = msg.text
    if not data.isdigit():
        await msg.answer("Iltimos son kirting!")
    else:
        logging.info(f"17 E : {data}")
        await state.update_data(
            {
                "fikr_17" :  data
            }
        )
        await TestState.next()
        await msg.answer("""18. So'ngi vaqtlarda ta’limga ta’luqli qaysi ijtimoiy tarmoqlarni ko'proq kuzatyapsiz <b>(3 ta variantni yozib qoldirishingiz ham mumkin!)</b> ?
A. Youtube 
B. Telegram 
C. TIkTok 
D. Instagram 
C. Twitter 
E. Facebook
G. Mening tanlovim """)

@dp.message_handler(state=TestState.test18)
async def test_18(msg : Message, state : FSMContext):
    data = msg.text.upper()
    vlist = ["A", "B", "C", "D", "E", "F", "G"]
    chek = data.split()
    chek1 = ""
    for i in chek :
        chek1 += i
    chek = chek1
    x = True
    if len(chek) > 3:
        await msg.answer("Maksimum 3 ta variant yozib yuboring!")
        x = False
    if chek[0] not in vlist:
        await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
        x = False
    if len(chek) == 2:
        if chek[1] not in vlist:
            await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
            x = False
    if len(chek) == 3:
        if chek[2] not in vlist:
            await msg.answer("Iltimos varintlardan chetga chiqmang qayta yuboring!")
            x = False
    if x:
        logging.info(f"18 : {data}")
        await state.update_data(
                {
                    "test_18" : data
                }
            )
        if "G" in data:
            await msg.answer("Tanlovingiznin yozib qoldiring!")
            await TestState.test18_1.set()
        else:
            await TestState.test19.set()
            await msg.answer("""19. Ta’lim olishda ustuvorlik kasb etadigan muhim omil bu ……………..
A. kelajakka ichonch bilan kirib borish
B. mahalla manfaatiga xizmat qilish
C. ta’limning qaysidir sohasiga hissa qo’shish
D. xorijiy sayohat va o’zim iqtisdoiy imkoniyatlarimni kuchaytirish
E. Shaxsiy fikrim""", reply_markup=test_19Button)

@dp.message_handler(state=TestState.test18_1)
async def test_18_1(msg : Message, state : FSMContext):
    data = msg.text
    logging.info(f"18 G : {data}")
    await state.update_data(
        {
            "fikr_18" :  data
        }
    )
    await TestState.next()

    await msg.answer("""19. Ta’lim olishda ustuvorlik kasb etadigan muhim omil bu ……………..
A. kelajakka ichonch bilan kirib borish
B. mahalla manfaatiga xizmat qilish
C. ta’limning qaysidir sohasiga hissa qo’shish
D. xorijiy sayohat va o’zim iqtisdoiy imkoniyatlarimni kuchaytirish
E. Shaxsiy fikrim""", reply_markup=test_19Button)


@dp.callback_query_handler(state=TestState.test19)
async def test_19(call  : CallbackQuery, state  :FSMContext):
    data = call.data.upper()
    logging.info(f"19 : {data}")
    logging.info(f"19 : {data}")

    await state.update_data(
        {
            "test_19" : data
        }
    )

    if data == "E" :
        await call.message.answer("O'z fikringizni qoldiring!")
        await TestState.test19_1.set()
    else :
        data = await state.get_data()
        qaytar = str(list(data.values()))
        logging.info(qaytar)
        data = await state.get_data()
        try : 
            db.add_test(data["id"], data["test_1"],data["test_2"],data["test_3"],data["test_4"],data["test_5"],data["test_6"],data["test_7"],data["test_8"],data["test_9"],data["test_10"],data["test_11"],data["test_12"],data["test_13"],data["test_14"],data["test_15"],data["test_16"],data["test_17"],data["test_18"],data["test_19"],data["fikr_2"],data["fikr_5"], data["fikr_7"],data["fikr_9"], data["fikr_13"], data["fikr_15"],data["fikr_16"], data["fikr_17"], data["fikr_18"],data["fikr_19"])
        except Exception as err:
            logging.info(str(err))
        await call.message.answer("So’rovnomada xolis ishtirokingiz uchun minnatdorchilik bildiramiz…")
        await state.finish()


@dp.message_handler(state=TestState.test19_1)
async def test_19_1(msg : Message, state : FSMContext):
    data  = msg.text
    logging.info(f"19 E : {data}")
    await state.update_data(
        {
            "fikr_19" :  data
        }
    )

    await msg.answer("So’rovnomada xolis ishtirokingiz uchun minnatdorchilik bildiramiz…")

    data = await state.get_data()
    logging.info(str(data.values()))
    try : 
        db.add_test(data["id"], data["test_1"],data["test_2"],data["test_3"],data["test_4"],data["test_5"],data["test_6"],data["test_7"],data["test_8"],data["test_9"],data["test_10"],data["test_11"],data["test_12"],data["test_13"],data["test_14"],data["test_15"],data["test_16"],data["test_17"],data["test_18"],data["test_19"],data["fikr_2"],data["fikr_5"], data["fikr_7"],data["fikr_9"], data["fikr_13"], data["fikr_15"],data["fikr_16"], data["fikr_17"], data["fikr_18"],data["fikr_19"])
    except Exception as err:
        logging.info(str(err))
    qaytar = str(list(data.values()))
    logging.info(qaytar)
    await state.finish()




