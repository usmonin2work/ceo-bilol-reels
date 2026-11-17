from lib import *

CAPTION = "Reklamaning birinchi oyida sotuv emas, avval ariza narxi va arizadan sotuvga o'tish foizini maqsad qilib qo'yamiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("BIRINCHI OY", [("Reklamadan birinchi oyda", WHITE, 88, 0), ("nimani kutish kerak?", GREY, 90, 0),
               ("Aniq raqamlarni", LIME, 110, 1)], chart=("Maqsad", "?")),
        T_list("1-oy maqsadlari", [("Ariza narxi", "masalan, 25 000 so'mdan oshmasin"),
               ("Arizalar soni", "masalan, oyiga 120 ta"),
               ("Sotuvga o'tish", "masalan, arizalarning 15%")], footnote=M, dur=5.6),
        T_flow("Oyma-oy reja", [("1-oy", "Test va raqamlar", BLUE), ("2-oy", "Yaxshisini kuchaytirish", ORANGE),
               ("3-oy", "Barqaror sotuv", LIME)], dur=5.6),
        T_cta("Birinchi oy maqsadlarini", "birga belgilaymiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
