from lib import *

CAPTION = "«1000+ mijoz» degan raqam faqat aniq va tekshirsa bo'ladigan bo'lsa, reklamaga ishonch qo'shadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("RAQAMLAR ISHONTIRADIMI?", [("«1000+ mijoz»", WHITE, 110, 0), ("hamma shunday yozadi —", GREY, 80, 0),
               ("kim ishonadi?", LIME, 120, 1)], chart=("Ishonch", "?")),
        T_vs("Qaysi biri ishontiradi?",
             {"title": "Umumiy", "color": RED, "rows": [("Mijozlar", "1000+"), ("Natija", "zo'r"), ("Isbot", "yo'q")]},
             {"title": "Aniq", "color": LIME, "rows": [("Mijozlar", "1 247"), ("Natija", "+38%"), ("Isbot", "keys")]},
             ["Yaxlit raqam emas,", "aniq va isbotli raqam"], footnote=M, dur=6.0),
        T_list("Raqam qachon ishlaydi", [("Aniq bo'lsa", "1 247 — 1000+ dan ishonchliroq"),
               ("Isboti bo'lsa", "keys, sharh yoki skrinshot bilan"),
               ("Mijozga yaqin bo'lsa", "uning muammosiga oid natija")], marker="check", dur=5.6),
        T_cta("Reklamangizdagi dalillarni", "birga kuchaytiramiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
