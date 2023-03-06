from aiogram.dispatcher.filters.state import StatesGroup, State

# Yoshingiz_______
# Jinsingiz; □Erkak. □Ayol.
# Doimiy yashash hududi: □shahar , □tuman markazi,□ tumandan 5 kmdan uzoqlikda
# Yashash  joy: □ota-onam bilan, □ijarada, □yotoqxonada
# Otamning ma’lumoti: □oliy, □o’rta maxsus, □o’rta
# Onamning ma’lumoti: □oliy, □o’rta maxsus, □o’rta
# Ta’lim olayapman: □OTM, □litsey, ixtisoslashtirilgan maktab, □maktab


class UserAnketaStates(StatesGroup):
    s_yoshi = State()
    s_jinsi = State()
    s_doimiy_yashash_hududi = State()
    s_yashash_joyi = State()
    s_otamning_mal = State()
    s_onamning_mal = State()
    s_talim_olyapman = State()

