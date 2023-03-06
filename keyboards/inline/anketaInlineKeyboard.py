from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#------------------------------------------------------------------------------------------------------------
#Jinsi □Erkak. □Ayol
jinsi_dict = [
    "Erkak" ,
    "Ayol"
]

jinsButton = InlineKeyboardMarkup(row_width=1)
for key in jinsi_dict:
    jinsButton.insert(InlineKeyboardButton(text=key, callback_data=key))

#-------------------------------------------------------------------------------------------------------------
# Doimiy yashash hududi
# □shahar , □tuman markazi,□ tumandan 5 kmdan uzoqlikda
doimiy_y_h = [
    "Shahar",
    "Tuman markazi",
    "Tumandan 5 km uzoqlikda"
]

doimiy_y_hButton = InlineKeyboardMarkup(row_width=1)
for key in doimiy_y_h:
    doimiy_y_hButton.insert(InlineKeyboardButton(text=key, callback_data=key))

#-------------------------------------------------------------------------------------------------------------
#Yashash  joy
# □ota-onam bilan, □ijarada, □yotoqxonada

yashash_joy_dict = [
    "Otam-onam bilan" ,
    "Ijarada" ,
    "Yotoqxonada"
]

yashash_joyButton = InlineKeyboardMarkup(row_width=1)
for key in yashash_joy_dict:
    yashash_joyButton.insert(InlineKeyboardButton(text=key, callback_data=key))
#--------------------------------------------------------------------------------------------------------------
# Otamning ma’lumoti:
# Onamning ma’lumoti:
# □oliy, □o’rta maxsus, □o’rta
malumot_dict = [
    "Oliy" ,
    "O'rta maxsus" ,
    "O'rta"
]
ota_malButton = InlineKeyboardMarkup(row_width=1)
ona_malButton = InlineKeyboardMarkup(row_width=1)

for  key in malumot_dict:
    ona_malButton.insert(InlineKeyboardButton(text=key, callback_data=key))
    ota_malButton.insert(InlineKeyboardButton(text=key, callback_data=key))
#--------------------------------------------------------------------------------------------------------------
#Ta’lim olayapman:
# □OTM, □litsey, ixtisoslashtirilgan maktab, □maktab
talim_dict =[
    "OTM",
    "Ixtisoslashtirilgan maktab" ,
    "Maktab",
]

talimButton = InlineKeyboardMarkup(row_width=1)
for key in talim_dict:
    talimButton.insert(InlineKeyboardButton(text=key, callback_data=key))
#-------------------------------------------------------------------------------------------------------------

