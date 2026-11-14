from lib import *

CAPTION = "Reklamadan kelgan lidni yo'qotmaslik uchun sotuv bo'limiga 3 ta oddiy qoida."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("LID QAYERGA KETDI?", [("Reklama lid berdi,", WHITE, 100, 0), ("sotuv bo'limi esa", GREY, 90, 0),
               ("uni yo'qotdi", LIME, 130, 1)], chart=("Sotuvlar", "↓")),
        T_bars("Javob tezligi va sotuv", [("5 daqiqada", 100, "100%", TEAL), ("1 soatda", 55, "55%", BLUE),
               ("Ertasi kuni", 20, "20%", RED)], sub="lid qanchalik tez sovib qoladi", footnote=M, dur=5.0),
        T_list("3 ta oddiy qoida", [("5 daqiqa", "birinchi javob shu vaqt ichida"), ("Bitta jadval", "har bir lid yozib boriladi"),
               ("3 marta urinish", "javob bermasa, yana qo'ng'iroq")], marker="check", dur=5.0),
        T_cta("Lid yo'qolmasin,", "sotuvga aylansin.", SUB, BTN, "15 daqiqada teshiklarni ko'rsatamiz", dur=3.4),
    ]
