from lib import *

CAPTION = "Bir nechta mahsulotni ko'rsatmoqchi bo'lsangiz, karusel reklamani sinab ko'ring."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("KARUSEL REKLAMA", [("Har doim", WHITE, 100, 0), ("video kerak emas", GREY, 90, 0),
               ("ba'zan karusel yutadi", LIME, 110, 1)]),
        T_vs("Qachon nima ishlaydi?",
             {"title": "Video", "color": BLUE, "rows": [("Maqsad", "Hikoya"), ("Kuchli", "Emotsiya"), ("Mos", "Brend, ekspert")]},
             {"title": "Karusel", "color": LIME, "rows": [("Maqsad", "Tanlov"), ("Kuchli", "Ko'p mahsulot"), ("Mos", "Do'kon, katalog")]},
             ["Bir nechta mahsulot bo'lsa —", "karuselni test qiling"], dur=6.0),
        T_list("Yaxshi karusel qoidasi", [("1-kartochka", "kuchli hook, narx yoki foyda"),
               ("Har kartochka", "bitta fikr, bitta mahsulot"), ("Oxirgisi", "aniq chaqiruv: yozing")],
               marker="num", footnote=M, dur=4.8),
        T_cta("Qaysi format sizga", "mosligini aytamiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
