from lib import *

CAPTION = "Reels reklamada odam birinchi kadrga qarab to'xtaydi yoki o'tib ketadi — shuning uchun u eng muhim kadr."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("BIRINCHI KADR", [("Odam 1 soniyada", WHITE, 96, 0), ("qaror qiladi:", GREY, 90, 0),
               ("to'xtaymi?", LIME, 130, 1)], chart=("O'tib ketish", "↓")),
        T_vs("Bir xil video, boshqa 1-kadr", {"title": "Zaif", "color": RED,
               "rows": [("Kadr", "logo yoki qorong'i"), ("Matn", "yo'q"), ("Natija", "o'tib ketadi")]},
             {"title": "Kuchli", "color": TEAL,
               "rows": [("Kadr", "yuz yoki natija"), ("Matn", "katta savol"), ("Natija", "to'xtab ko'radi")]},
             ["klik narxi arzonlashadi"], footnote=M, dur=6.0),
        T_list("Kuchli 1-kadr", [("Yuz yoki mahsulot", "kadr markazida, yorug'"),
               ("Katta matn", "3–5 so'zli savol yoki raqam"),
               ("Muqova", "lentada ham shu kadr ko'rinadi")], marker="num", dur=5.4),
        T_cta("Kreativlaringizni", "tekshirib beramiz.", SUB, BTN, "qaysi kadr pulni yeyayotganini ko'rasiz", dur=3.4),
    ]
