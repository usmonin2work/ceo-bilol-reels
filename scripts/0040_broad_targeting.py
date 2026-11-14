from lib import *

CAPTION = "Qiziqishlarsiz keng auditoriya ba'zan tor targetingdan ham arzon mijoz olib keladi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("QIZIQISHLARSIZ REKLAMA", [("Hech qanday", WHITE, 100, 0), ("qiziqish tanlamadik.", GREY, 90, 0),
               ("Sotuv oshdi", LIME, 130, 1)]),
        T_vs("Bir xil byudjet", {"title": "TOR", "color": RED,
               "rows": [("Auditoriya", "50 ming"), ("Ko'rish narxi", "qimmat"), ("Algoritm", "cheklangan")]},
             {"title": "KENG", "color": LIME,
               "rows": [("Auditoriya", "2 mln+"), ("Ko'rish narxi", "arzonroq"), ("Algoritm", "o'zi qidiradi")]},
             ["Kreativ auditoriyani tanlaydi"], footnote=M, dur=6.0),
        T_list("Qachon ishlaydi?", [("Pixelda ma'lumot bor", "sotuvlar kuzatilgan"),
               ("Kreativ aniq", "videoda kimga ekanini ayting"),
               ("Sabr bor", "3–5 kun o'rganishga bering")], marker="check", dur=4.8),
        T_cta("Sizga keng yoki tor —", "birga hal qilamiz.", SUB, BTN, "15 daqiqada kabinetni ko'rib chiqamiz", dur=3.4),
    ]
