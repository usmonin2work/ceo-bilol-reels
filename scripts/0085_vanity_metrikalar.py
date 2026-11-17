from lib import *

CAPTION = "Ko'p like va ko'rishlar chiroyli ko'rinadi, lekin reklama samarasini faqat arizalar va sotuvlar ko'rsatadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("ALDOVCHI RAQAMLAR", [("50 000 ko'rish,", WHITE, 100, 0), ("2 000 like —", GREY, 90, 0),
               ("sotuv esa 0", LIME, 120, 1)], chart=("Sotuvlar", "↓")),
        T_vs("Hisobotda nimaga qaraysiz?",
             {"title": "Chiroyli", "color": RED, "rows": [("Ko'rishlar", "50 000"), ("Like", "2 000"), ("Sotuv", "0")]},
             {"title": "Foydali", "color": LIME, "rows": [("Ko'rishlar", "8 000"), ("Arizalar", "60"), ("Sotuv", "12")]},
             ["Like emas,", "ariza va sotuvni sanang"], footnote=M, dur=6.0),
        T_list("Asosiy ko'rsatkichlar", [("Ariza narxi", "bitta lid qanchaga tushdi"),
               ("Sotuvga o'tish", "lidlarning necha foizi sotib oldi"),
               ("Daromad", "reklamaga sarflangan pul qaytdimi")], marker="check", dur=5.6),
        T_cta("Hisobotingizni", "birga tekshiramiz.", SUB, BTN, "haqiqiy natijani ko'rsatamiz", dur=3.4),
    ]
