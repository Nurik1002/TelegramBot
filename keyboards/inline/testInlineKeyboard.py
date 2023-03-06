from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# #------------------------------------------------------------------------------------------------------------
# #Jinsi □Erkak. □Ayol
# jinsi_dict = [
#     "Erkak" ,
#     "Ayol"
# ]
#
# jinsButton = InlineKeyboardMarkup(row_width=1)
# for key in jinsi_dict:
#     jinsButton.insert(InlineKeyboardButton(text=key, callback_data=key))

ABCDE = ["A", "B", "C","D", "E"]
ABCDEF = ["A", "B", "C","D", "E", "F"]
variantlar = ["A", "B", "C","D", "E", "F", "G", "H", "I", "J"]

#--------------------------------1ss-----------------------------------------------
test_1Button = InlineKeyboardMarkup(row_width=2)
for i in ABCDE:
    test_1Button.insert(InlineKeyboardButton(text=i, callback_data=i))

#-------------------------------2------------------------------------------------
test_2Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_2Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "F":
        break

#-------------------------------4-----------------------------------------------
test_4Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_4Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "E":
        break
#----------------------------------5-------------------------------------------------
test_5Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_5Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "D":
        break
#---------------------------------6-------------------------------------------------
test_6Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_6Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "D":
        break
#--------------------------------7---------------------------------------------------
test_7Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_7Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "E":
        break
#--------------------------------8---------------------------------------------------
test_8Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_8Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "D":
        break
#--------------------------------9---------------------------------------------------
test_9Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_9Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "E":
        break
#---------------------------------12--------------------------------------------------
test_12Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_12Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "D":
        break


#---------------------------------15----------------------------------------------------

test_15Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_15Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "I":
        break
#--------------------------------16-----------------------------------------------------
test_16Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_16Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "C":
        break
#-------------------------------17--------------------------------------------------------
test_17Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_17Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "E":
        break


#-------------------------------19-------------------------------------------------------
test_19Button = InlineKeyboardMarkup(row_width=2)
for i in variantlar:
    test_19Button.insert(InlineKeyboardButton(text=i, callback_data=i))
    if i == "E":
        break