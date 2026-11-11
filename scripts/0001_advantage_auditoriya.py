from lib import *

CAPTION = "Advantage+ auditoriya qachon yordam beradi, qachon pulingizni yeydi?"

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("ADVANTAGE+ AUDITORIYA", [("Meta o'zi", WHITE, 100, 0), ("mijoz topadi.", GREY, 90, 0),
               ("Har doimmi?", LIME, 130, 1)]),
        T_vs("Qachon ishlaydi?", {"title": "ISHLAYDI", "color": LIME,
               "rows": [("Pixel ma'lumoti", "50+ sotuv"), ("Kreativ", "aniq taklif"), ("Byudjet", "barqaror")]},
             {"title": "ISHLAMAYDI", "color": RED,
               "rows": [("Pixel ma'lumoti", "yangi, bo'sh"), ("Kreativ", "umumiy"), ("Byudjet", "juda kichik")]},
             ["Algoritmga ma'lumot kerak"], footnote=M, dur=6.0),
        T_list("To'g'ri ishlatish", [("Avval sinab ko'ring", "oddiy auditoriya bilan solishtiring"),
               ("Kreativ bilan yo'naltiring", "kimga ekanini videoda ayting"),
               ("Sotuvni o'lchang", "lid emas, sotuv narxi")], marker="check", dur=4.8),
        T_cta("Sizga qaysi biri", "mos — aytamiz.", SUB, BTN, "15 daqiqada kabinetni ko'rib chiqamiz", dur=3.4),
    ]
