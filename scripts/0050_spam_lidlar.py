from lib import *

CAPTION = "Soxta arizalarni kamaytirsangiz, reklama byudjeti haqiqiy mijozlarga ketadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesga qarab farq qiladi"

def scenes():
    return [
        T_hook("ARIZA KO'P, MIJOZ YO'Q?", [("100 ta ariza,", WHITE, 100, 0), ("telefon ko'tarmaydi", GREY, 86, 0),
               ("soxta lidlar", LIME, 130, 1)], chart=("Sifat", "↓")),
        T_vs("Oddiy forma vs filtrli forma",
             {"title": "Oddiy", "color": RED, "rows": [("Arizalar", "100 ta"), ("Javob beradi", "30 ta"), ("1 lid narxi", "$1")]},
             {"title": "Filtrli", "color": TEAL, "rows": [("Arizalar", "60 ta"), ("Javob beradi", "45 ta"), ("1 lid narxi", "$1.6")]},
             ["kamroq ariza — ko'proq mijoz"], footnote=M, dur=6.0),
        T_list("Spamni 3 usulda kesamiz", [("Savol", "formaga 1–2 ta saralovchi savol"),
               ("Tasdiq", "\"Higher intent\" — raqamni tekshirish"),
               ("Tezlik", "arizaga 5 daqiqada qo'ng'iroq")], marker="check", dur=4.8),
        T_cta("Lidlaringizni", "tozalab beramiz.", SUB, BTN, "15 daqiqada formani tekshiramiz", dur=3.4),
    ]
